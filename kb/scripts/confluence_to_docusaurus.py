#!/usr/bin/env python3
"""Confluence Markdown export -> Docusaurus migration helper.

Designed for the CloudFire/Atlassian export structure discussed in ChatGPT.
Version 2.0: renders video attachments referenced with Markdown image syntax as HTML video elements instead of images, preventing Docusaurus image metadata failures; retains all v1.9 fixes.
Uses only the Python standard library.

Safety:
- default mode is DRY RUN (no destination files are written)
- --apply is required to create output
- the source tree is never modified

Output with --apply:
  <output>/docs/...               normalized Markdown tree
  <output>/static/kb-assets/...   copied/renamed assets
  <output>/migration-report.md    migration report
  <output>/migration-report.json  machine-readable report
"""
from __future__ import annotations

import argparse
import hashlib
import difflib
import html
import json
import os
import re
import shutil
import sys
import tempfile
import unicodedata
import urllib.parse
import zipfile
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

MACRO_CATEGORIES = {
    "Account Manager": "account-manager",
    "Overview di Cortex": "overview-di-cortex",
    "Partner Portal": "partner-portal",
    "Project Manager": "project-manager",
    "Registrazione": "registrazione",
}

# Obvious export mojibake observed in the supplied archive.
MOJIBAKE_REPLACEMENTS = {
    "a╠Ç": "à",
}

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".tif", ".tiff", ".ico"}
VIDEO_EXTS = {".mp4", ".mov", ".webm", ".m4v"}
SKIP_NAMES = {".DS_Store"}
COMMON_HTML_TAGS = {
    "a", "abbr", "address", "article", "aside", "audio", "b", "blockquote", "br", "button", "canvas",
    "caption", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", "details", "dfn", "div",
    "dl", "dt", "em", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6",
    "header", "hr", "i", "iframe", "img", "input", "ins", "kbd", "label", "legend", "li", "link", "main", "map",
    "mark", "meta", "nav", "noscript", "object", "ol", "optgroup", "option", "p", "picture", "pre", "q", "s",
    "samp", "script", "section", "select", "small", "source", "span", "strong", "style", "sub", "summary", "sup",
    "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "u",
    "ul", "var", "video", "wbr",
}

MD_LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\((<[^>]+>|(?:\\.|[^()\\]|\([^()]*\))*)\)")
CALLOUT_START_RE = re.compile(r"^\s*>\s*\[!(NOTE|INFO|WARNING|TIP|CAUTION)\]\s*$", re.I)
CONFLUENCE_PAGE_RE = re.compile(r"(?:https?://[^/]+)?/wiki/spaces/KB/pages/(\d+)/([^?#)]+)", re.I)
CONFLUENCE_CREATE_RE = re.compile(r"(?:https?://[^/]+)?/wiki/pages/createpage\.action", re.I)
ATLASSIAN_SHORT_RE = re.compile(r"https?://[^/]*atlassian\.net/(?:l/cp/|wiki/x/)", re.I)


def fix_mojibake(s: str) -> str:
    for bad, good in MOJIBAKE_REPLACEMENTS.items():
        s = s.replace(bad, good)
    return unicodedata.normalize("NFC", s)


def slugify(s: str, fallback: str = "page") -> str:
    s = fix_mojibake(s)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or fallback


def norm_key(s: str) -> str:
    """Aggressive matching key for titles/slugs."""
    s = urllib.parse.unquote_plus(s)
    s = fix_mojibake(s)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def is_ignored_path(p: Path) -> bool:
    return any(part == "__MACOSX" or part.startswith("._") for part in p.parts) or p.name in SKIP_NAMES


def visible_files(directory: Path) -> Iterable[Path]:
    for p in directory.iterdir():
        if not is_ignored_path(p):
            yield p


def file_nonempty_markdown(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return False
    # Ignore whitespace/frontmatter-only pages as empty containers.
    stripped = re.sub(r"\A\s*---\s*.*?\s*---\s*", "", text, flags=re.S).strip()
    return bool(stripped)


def find_export_root(source: Path) -> Path:
    """Find directory containing the five macro category .md/folder pairs."""
    # Canonicalize the path first. On macOS, /var is a symlink to /private/var;
    # mixing the two spellings breaks pathlib.relative_to().
    source = source.resolve()
    candidates = [source]
    for p in source.rglob("*"):
        if p.is_dir() and len(p.relative_to(source).parts) <= 4 and not is_ignored_path(p):
            candidates.append(p)
    best = None
    best_score = -1
    for d in candidates:
        names = {fix_mojibake(p.name) for p in visible_files(d)}
        score = 0
        for macro in MACRO_CATEGORIES:
            if macro in names:
                score += 2
            if f"{macro}.md" in names:
                score += 1
        if "Knowledge Base.md" in names:
            score += 1
        if score > best_score:
            best, best_score = d, score
    if best is None or best_score < 5:
        raise RuntimeError(f"Non riesco a identificare la root dell'export sotto: {source}")
    return best


def sibling_page_for_dir(d: Path) -> Optional[Path]:
    if d.parent == d:
        return None
    wanted = fix_mojibake(d.name)
    for p in visible_files(d.parent):
        if p.is_file() and p.suffix.lower() == ".md" and fix_mojibake(p.stem) == wanted:
            return p
    return None


def is_real_category_dir(d: Path, root: Path) -> bool:
    if d == root:
        return True
    if d.parent == root and fix_mojibake(d.name) in MACRO_CATEGORIES:
        return True
    return sibling_page_for_dir(d) is not None


def relative_url(from_file: Path, to_file: Path) -> str:
    rel = os.path.relpath(to_file, from_file.parent)
    return Path(rel).as_posix()


def split_dest_and_title(raw: str) -> Tuple[str, str]:
    raw = raw.strip()
    # Markdown may use <destination> and optional quoted title.
    if raw.startswith("<") and ">" in raw:
        end = raw.find(">")
        return raw[1:end], raw[end + 1 :]
    # Only split a title if whitespace is followed by a quote/apostrophe/paren title.
    m = re.match(r"^(\S+)(\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))$", raw)
    if m:
        return m.group(1), m.group(2)
    return raw, ""


@dataclass
class Page:
    source: Path
    rel: Path
    title: str
    macro: Optional[str]
    real_dirs: List[str]
    synthetic_dirs: List[str]
    is_category_page: bool
    content_nonempty: bool
    output_rel: Path = Path()
    skipped: bool = False
    skip_reason: str = ""
    content_hash: str = ""


@dataclass
class Report:
    pages_total: int = 0
    pages_written: int = 0
    pages_skipped: int = 0
    categories_generated: int = 0
    assets_referenced: int = 0
    assets_copied: int = 0
    assets_fixed_path: int = 0
    assets_missing: List[dict] = field(default_factory=list)
    assets_ambiguous: List[dict] = field(default_factory=list)
    video_embeds_converted: int = 0
    links_total: int = 0
    links_resolved: int = 0
    links_unresolved: List[dict] = field(default_factory=list)
    links_externalized: List[dict] = field(default_factory=list)
    callouts_converted: int = 0
    placeholders_converted: int = 0
    heading_pages_normalized: int = 0
    headings_shifted: int = 0
    heading_ids_added: int = 0
    anchor_links_seen: int = 0
    anchors_repaired: int = 0
    anchors_unresolved: List[dict] = field(default_factory=list)
    duplicate_pages_skipped: List[dict] = field(default_factory=list)
    root_orphans: List[dict] = field(default_factory=list)
    filename_mojibake_fixed: int = 0
    old_home_skipped: bool = False
    warnings: List[str] = field(default_factory=list)


class Migrator:
    def __init__(self, root: Path, output: Path, apply: bool, atlassian_base: str):
        # Keep a canonical root. This avoids macOS /var vs /private/var
        # mismatches after TemporaryDirectory extraction and Path.resolve().
        self.root = root.resolve()
        self.output = output
        self.docs_out = output / "docs"
        self.static_out = output / "static" / "kb-assets"
        self.apply = apply
        self.atlassian_base = atlassian_base.rstrip("/")
        self.pages: List[Page] = []
        self.page_by_source: Dict[Path, Page] = {}
        self.alias_index: Dict[str, List[Page]] = defaultdict(list)
        self.asset_basename_index: Dict[str, List[Path]] = defaultdict(list)
        self.asset_output: Dict[Path, str] = {}
        self.report = Report()
        self.category_dirs: Set[Tuple[str, ...]] = set()
        self.category_has_index: Set[Tuple[str, ...]] = set()
        self.category_labels: Dict[Tuple[str, ...], str] = {}
        self._used_output_paths: Set[Path] = set()
        self._page_by_output_rel: Dict[Path, Page] = {}
        self._page_by_route: Dict[str, Page] = {}
        self._anchor_index: Dict[Path, dict] = {}

    def scan(self) -> None:
        # Asset index across full root.
        for p in self.root.rglob("*"):
            if p.is_file() and not is_ignored_path(p) and p.suffix.lower() != ".md":
                self.asset_basename_index[fix_mojibake(p.name).lower()].append(p)

        raw_pages: List[Page] = []
        for p in self.root.rglob("*.md"):
            if is_ignored_path(p):
                continue
            rel = p.resolve().relative_to(self.root)
            if rel == Path("Knowledge Base.md"):
                self.report.old_home_skipped = True
                continue

            parts = list(rel.parts[:-1])
            macro = parts[0] if parts and fix_mojibake(parts[0]) in MACRO_CATEGORIES else None

            real_dirs: List[str] = []
            synthetic_dirs: List[str] = []
            cur = self.root
            for part in parts:
                cur = cur / part
                fixed = fix_mojibake(part)
                if is_real_category_dir(cur, self.root):
                    real_dirs.append(fixed)
                    synthetic_dirs = []
                else:
                    synthetic_dirs.append(fixed)

            stem = fix_mojibake(p.stem)
            # Reconstruct slash-split Confluence page titles.
            title = "/".join(synthetic_dirs + [stem]) if synthetic_dirs else stem

            # Is this .md the sibling page for a real directory?
            same_dir = p.with_suffix("")
            is_cat = same_dir.is_dir() and is_real_category_dir(same_dir, self.root)
            nonempty = file_nonempty_markdown(p)
            content = p.read_bytes()
            h = hashlib.sha256(content).hexdigest()
            raw_pages.append(Page(p, rel, title, macro, real_dirs, synthetic_dirs, is_cat, nonempty, content_hash=h))

        # Detect exact duplicates at root that also exist under a macro.
        hashes_under_macro = defaultdict(list)
        for page in raw_pages:
            if page.macro:
                hashes_under_macro[page.content_hash].append(page)

        for page in raw_pages:
            if page.macro is None:
                # Top-level macro page itself has rel with no directory; detect by stem.
                if page.rel.parent == Path(".") and fix_mojibake(page.source.stem) in MACRO_CATEGORIES:
                    page.macro = fix_mojibake(page.source.stem)
                    page.real_dirs = [page.macro]
                    page.is_category_page = True
                elif page.content_hash in hashes_under_macro:
                    page.skipped = True
                    page.skip_reason = "duplicato identico già presente in una macro-categoria"
                    self.report.duplicate_pages_skipped.append({
                        "source": page.rel.as_posix(),
                        "duplicate_of": hashes_under_macro[page.content_hash][0].rel.as_posix(),
                    })
                else:
                    self.report.root_orphans.append({"source": page.rel.as_posix(), "title": page.title})

            self.pages.append(page)
            self.page_by_source[page.source.resolve()] = page

        self._assign_output_paths()
        self._build_aliases()
        self.report.pages_total = len(self.pages)

    def _assign_output_paths(self) -> None:
        # First create output paths, keeping real categories and flattening synthetic slash dirs.
        for page in self.pages:
            if page.skipped:
                continue
            if page.macro:
                macro_slug = MACRO_CATEGORIES[page.macro]
                # Remove macro duplicate from real_dirs if present.
                dirs = page.real_dirs[:]
                if dirs and dirs[0] == page.macro:
                    dirs = dirs[1:]
                out_dirs = [macro_slug] + [slugify(x, "category") for x in dirs]
            else:
                out_dirs = ["_unclassified"] + [slugify(x, "category") for x in page.real_dirs]

            # Category page -> index.md under its category directory.
            if page.is_category_page:
                # If category page is top macro page, ensure only macro dir.
                if page.rel.parent == Path(".") and fix_mojibake(page.source.stem) in MACRO_CATEGORIES:
                    out_dirs = [MACRO_CATEGORIES[fix_mojibake(page.source.stem)]]
                elif page.source.with_suffix("").is_dir():
                    # The category directory itself is represented by the page stem. If the real_dirs
                    # list did not include it (because page is its sibling), append it.
                    cat_name = fix_mojibake(page.source.stem)
                    if not out_dirs or slugify(cat_name) != out_dirs[-1]:
                        out_dirs.append(slugify(cat_name, "category"))
                out_rel = Path(*out_dirs) / "index.md"
            else:
                out_rel = Path(*out_dirs) / f"{slugify(page.title)}.md"

            # Avoid accidental collisions by suffixing a short hash.
            if out_rel in self._used_output_paths:
                suffix = hashlib.sha1(page.rel.as_posix().encode("utf-8")).hexdigest()[:8]
                out_rel = out_rel.with_name(f"{out_rel.stem}-{suffix}{out_rel.suffix}")
            self._used_output_paths.add(out_rel)
            page.output_rel = out_rel
            self._page_by_output_rel[out_rel] = page
            if out_rel.name == "index.md":
                route = "/" + "/".join(out_rel.parent.parts) + "/"
            else:
                route = "/" + "/".join(out_rel.with_suffix("").parts)
            self._page_by_route[route.rstrip("/") or "/"] = page

            # Track real output category dirs/labels.
            parts = list(out_rel.parent.parts)
            for i in range(1, len(parts) + 1):
                key = tuple(parts[:i])
                self.category_dirs.add(key)
            # Better labels from original category names.
            if page.macro:
                self.category_labels[(MACRO_CATEGORIES[page.macro],)] = page.macro
                original_dirs = page.real_dirs[:]
                if original_dirs and original_dirs[0] == page.macro:
                    original_dirs = original_dirs[1:]
                cur = [MACRO_CATEGORIES[page.macro]]
                for name in original_dirs:
                    cur.append(slugify(name, "category"))
                    self.category_labels[tuple(cur)] = name
                if page.is_category_page and page.source.with_suffix("").is_dir():
                    cat_name = fix_mojibake(page.source.stem)
                    k = tuple(out_rel.parent.parts)
                    self.category_labels[k] = cat_name
            if page.is_category_page and page.content_nonempty:
                self.category_has_index.add(tuple(out_rel.parent.parts))

    def _build_aliases(self) -> None:
        for page in self.pages:
            if page.skipped:
                continue
            aliases = {
                norm_key(page.title),
                norm_key(page.source.stem),
                norm_key(page.output_rel.stem),
            }
            # Include reconstructed relative path and original basename slug.
            aliases.add(norm_key(page.rel.with_suffix("").as_posix()))
            aliases.add(norm_key(slugify(page.title)))
            for a in aliases:
                if a:
                    self.alias_index[a].append(page)

    def _best_page_candidate(self, key: str, source_page: Page) -> Optional[Page]:
        cands = []
        seen = set()
        for cand in self.alias_index.get(key, []):
            ksrc = cand.source.resolve()
            if ksrc not in seen:
                seen.add(ksrc)
                cands.append(cand)
        if not cands:
            return None
        if len(cands) == 1:
            return cands[0]
        # Prefer same macro and longest shared original parent prefix.
        src_parts = source_page.rel.parent.parts
        def score(p: Page) -> Tuple[int, int]:
            macro = int(p.macro == source_page.macro)
            common = 0
            for a, b in zip(src_parts, p.rel.parent.parts):
                if norm_key(a) == norm_key(b):
                    common += 1
                else:
                    break
            return (macro, common)
        ranked = sorted(cands, key=score, reverse=True)
        if len(ranked) >= 2 and score(ranked[0]) == score(ranked[1]):
            return None
        return ranked[0]

    def _resolve_case_insensitive_path(self, base: Path, relative: str) -> Optional[Path]:
        """Resolve a relative path component-by-component without depending on FS case sensitivity.

        Confluence exports often write lowercase slug-like links (supporto/case.md)
        while the exported files keep display casing (Supporto/Case.md). This helper
        makes the migration deterministic on both case-sensitive and case-insensitive
        filesystems and across Python versions.
        """
        cur = base.resolve()
        parts = Path(relative).parts
        for part in parts:
            if part in ("", "."):
                continue
            if part == "..":
                cur = cur.parent
                continue
            if not cur.is_dir():
                return None
            try:
                children = [c for c in cur.iterdir() if not is_ignored_path(c)]
            except OSError:
                return None
            # IMPORTANT: do not trust `(cur / part).exists()` here. On the default
            # macOS filesystem a wrongly-cased path can still exist, but pathlib keeps
            # the caller's spelling. That creates a lexical Path which does not match
            # the actual-cased Path keys stored in our indexes. Resolve every component
            # from the directory listing so we preserve the real on-disk spelling.
            exact_name = [c for c in children if c.name == part]
            if len(exact_name) == 1:
                cur = exact_name[0]
                continue
            folded = [c for c in children if c.name.casefold() == part.casefold()]
            if len(folded) == 1:
                cur = folded[0]
                continue
            # Then allow Confluence-style punctuation/space normalization.
            wanted = norm_key(part)
            normalized = [c for c in children if norm_key(c.name) == wanted]
            if len(normalized) == 1:
                cur = normalized[0]
                continue
            return None
        return cur.resolve()

    def _resolve_local_page_link(self, source_page: Page, dest: str) -> Optional[Page]:
        decoded = urllib.parse.unquote(dest.split("#", 1)[0].split("?", 1)[0])
        decoded = decoded.replace("\\", "/")
        # Exact filesystem resolution first. On case-insensitive macOS, an existing
        # wrongly-cased lexical path may not match our actual-cased index key, so only
        # return when the index lookup itself succeeds; otherwise continue to the
        # deterministic component traversal below.
        candidate = (source_page.source.parent / decoded).resolve()
        if candidate.exists() and candidate.is_file() and candidate.suffix.lower() == ".md":
            page = self.page_by_source.get(candidate)
            if page:
                return page
        # Deterministic case-insensitive traversal. This resolves links such as
        # ./supporto/case.md -> Supporto/Case.md regardless of filesystem semantics.
        ci_candidate = self._resolve_case_insensitive_path(source_page.source.parent, decoded)
        if ci_candidate and ci_candidate.is_file() and ci_candidate.suffix.lower() == ".md":
            page = self.page_by_source.get(ci_candidate.resolve())
            if page:
                return page
        # Try case-insensitive sibling/path match.
        try:
            target_name = Path(decoded).stem
        except Exception:
            target_name = decoded.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        keys = [norm_key(target_name), norm_key(decoded)]
        for k in keys:
            p = self._best_page_candidate(k, source_page)
            if p:
                return p
        # Atlassian occasionally drops the final vowel of accented Italian words
        # in generated slugs (e.g. funzionalità -> funzionalit). Use a conservative
        # fuzzy fallback on the target basename and require a unique close match.
        target_key = norm_key(target_name)
        if target_key:
            pool = [k for k in self.alias_index.keys() if len(k) >= 8]
            matches = difflib.get_close_matches(target_key, pool, n=4, cutoff=0.94)
            fuzzy_pages = []
            seen_src = set()
            for mk in matches:
                for cand in self.alias_index.get(mk, []):
                    if cand.skipped:
                        continue
                    # Prefer candidates in the same macro area.
                    if source_page.macro and cand.macro != source_page.macro:
                        continue
                    src_key = cand.source.resolve()
                    if src_key not in seen_src:
                        seen_src.add(src_key)
                        fuzzy_pages.append(cand)
            if len(fuzzy_pages) == 1:
                return fuzzy_pages[0]
        return None

    def _resolve_confluence_page(self, source_page: Page, dest: str) -> Optional[Page]:
        m = CONFLUENCE_PAGE_RE.search(dest)
        if not m:
            return None
        title = urllib.parse.unquote_plus(m.group(2)).replace("+", " ")
        title = title.rstrip("/")
        return self._best_page_candidate(norm_key(title), source_page)

    def _asset_candidates(self, source_page: Page, dest: str) -> Tuple[List[Path], Optional[Path]]:
        clean = dest.split("#", 1)[0].split("?", 1)[0]
        clean = urllib.parse.unquote(clean)
        clean = clean.replace("\\_", "_").replace("\\ ", " ")
        # Resolve to the actual on-disk casing. This avoids duplicate asset identities
        # on case-insensitive macOS when the Markdown spelling differs only by case.
        exact = self._resolve_case_insensitive_path(source_page.source.parent, clean)
        if exact and exact.is_file():
            return [exact], exact

        basename = fix_mojibake(Path(clean).name).lower()
        candidates: List[Path] = []
        # Prefer attachments directories while walking upward from source.
        cur = source_page.source.parent
        while True:
            ad = cur / "attachments"
            if ad.is_dir():
                for p in visible_files(ad):
                    if p.is_file() and fix_mojibake(p.name).lower() == basename:
                        candidates.append(p.resolve())
            if cur == self.root or cur.parent == cur:
                break
            cur = cur.parent
        # Global basename fallback.
        for p in self.asset_basename_index.get(basename, []):
            rp = p.resolve()
            if rp not in candidates:
                candidates.append(rp)
        return candidates, None

    def _copy_asset(self, src: Path) -> str:
        src = src.resolve()
        if src in self.asset_output:
            return self.asset_output[src]
        fixed_name = fix_mojibake(src.name)
        # Remove query-like garbage that may actually be part of a filename.
        base_name = fixed_name.split("?", 1)[0]
        ext = Path(base_name).suffix.lower()
        stem = Path(base_name).stem
        if not ext:
            ext = src.suffix.lower()
        digest = hashlib.sha1(src.resolve().relative_to(self.root).as_posix().encode("utf-8", errors="ignore")).hexdigest()[:10]
        out_name = f"{digest}-{slugify(stem, 'asset')}{ext}"
        url = f"/kb-assets/{out_name}"
        self.asset_output[src] = url
        if self.apply:
            self.static_out.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, self.static_out / out_name)
        self.report.assets_copied += 1
        return url

    def _render_embedded_asset(self, label: str, url: str, source: Path, title_suffix: str = "") -> str:
        """Render a local attachment according to its real media type.

        Confluence Markdown exports can encode videos as image syntax (`![](...)`).
        Docusaurus then sends .mp4/.mov/.webm files through its image metadata
        pipeline, which triggers image-size warnings and may break the webpack build.
        Keep true images as Markdown images, but emit videos as HTML video elements.
        """
        suffix = source.suffix.lower()
        if suffix in VIDEO_EXTS:
            self.report.video_embeds_converted += 1
            return f'<video controls preload="metadata" src="{url}"></video>'
        return f"![{label}]({url}{title_suffix})"

    def _rewrite_link(self, source_page: Page, is_image: bool, label: str, raw_dest: str) -> str:
        dest, title_suffix = split_dest_and_title(raw_dest)
        d = dest.strip()
        self.report.links_total += 0 if is_image else 1

        # Leave anchors, data URIs, mail/tel, and external non-Atlassian URLs untouched.
        if d.startswith("#") or d.startswith("data:") or d.startswith("mailto:") or d.startswith("tel:"):
            return f"{'!' if is_image else ''}[{label}]({raw_dest})"

        # Normalize escaped URL punctuation before parsing. Confluence can emit links like
        # [**https://ip\_pubblico\_assegnato:4444**](https://ip_pubblico_assegnato:4444.)
        # which are examples/placeholders rather than valid clickable hostnames.
        normalized_d = d.replace("\\:", ":").replace("\\_", "_").replace("\\-", "-")
        trailing_punct = ""
        while normalized_d and normalized_d[-1] in ".,;":
            trailing_punct = normalized_d[-1] + trailing_punct
            normalized_d = normalized_d[:-1]
        parsed = urllib.parse.urlparse(normalized_d)
        is_http = parsed.scheme in {"http", "https"}

        # Invalid technical URL placeholders must not remain Markdown links: Docusaurus
        # otherwise treats the backticked destination as a relative internal path.
        # Render them as inline code and preserve sentence punctuation.
        if not is_image and is_http and "_" in (parsed.hostname or ""):
            self.report.placeholders_converted += 1
            label_plain = re.sub(r"[*`]", "", label).replace("\\_", "_").replace("\\:", ":")
            if normalized_d in label_plain or label_plain.strip() == normalized_d:
                return f"`{normalized_d}`{trailing_punct}"
            return f"{label} (`{normalized_d}`){trailing_punct}"

        # Images/local attachments.
        if is_image and not is_http:
            self.report.assets_referenced += 1
            cands, exact = self._asset_candidates(source_page, d)
            if len(cands) == 1:
                chosen = cands[0]
                if exact is None:
                    self.report.assets_fixed_path += 1
                url = self._copy_asset(chosen)
                return self._render_embedded_asset(label, url, chosen, title_suffix)
            if len(cands) > 1:
                # Rank by filesystem proximity. A unique nearest candidate is deterministic
                # and should not be reported as ambiguous. Also suppress ambiguity when all
                # candidates are byte-identical duplicates of the same asset.
                def distance(p: Path) -> int:
                    try:
                        a = source_page.source.parent.resolve().parts
                        b = p.parent.resolve().parts
                        common = 0
                        for x, y in zip(a, b):
                            if x == y:
                                common += 1
                            else:
                                break
                        return (len(a) - common) + (len(b) - common)
                    except Exception:
                        return 9999

                ranked = sorted(cands, key=lambda p: (distance(p), p.as_posix()))
                chosen = ranked[0]
                nearest_is_unique = len(ranked) == 1 or distance(ranked[0]) < distance(ranked[1])

                all_identical = False
                try:
                    digests = set()
                    for cand in ranked:
                        h = hashlib.sha256()
                        with cand.open("rb") as fh:
                            for chunk in iter(lambda: fh.read(1024 * 1024), b""):
                                h.update(chunk)
                        digests.add(h.hexdigest())
                    all_identical = len(digests) == 1
                except Exception:
                    all_identical = False

                if not nearest_is_unique and not all_identical:
                    self.report.assets_ambiguous.append({
                        "page": source_page.rel.as_posix(), "dest": d,
                        "chosen": chosen.resolve().relative_to(self.root).as_posix(),
                        "candidates": [p.resolve().relative_to(self.root).as_posix() for p in ranked],
                    })
                if exact is None:
                    self.report.assets_fixed_path += 1
                url = self._copy_asset(chosen)
                return self._render_embedded_asset(label, url, chosen, title_suffix)
            self.report.assets_missing.append({"page": source_page.rel.as_posix(), "dest": d})
            return f"![{label}]({raw_dest})"

        # Local non-image attachment links.
        if not is_image and not is_http and not d.startswith("/") and not d.lower().endswith(".md"):
            suffix = Path(urllib.parse.unquote(d.split("?",1)[0])).suffix.lower()
            if suffix and suffix != ".md":
                cands, exact = self._asset_candidates(source_page, d)
                if cands:
                    chosen = cands[0]
                    url = self._copy_asset(chosen)
                    self.report.links_resolved += 1
                    return f"[{label}]({url}{title_suffix})"

        # Confluence page URLs, relative or absolute.
        if CONFLUENCE_PAGE_RE.search(d):
            target = self._resolve_confluence_page(source_page, d)
            if target and not target.skipped:
                anchor = "#" + d.split("#", 1)[1] if "#" in d else ""
                self.report.links_resolved += 1
                if target.is_category_page and not target.content_nonempty:
                    out = "/" + "/".join(target.output_rel.parent.parts) + anchor
                else:
                    out = relative_url(self.docs_out / source_page.output_rel, self.docs_out / target.output_rel) + anchor
                return f"[{label}]({out}{title_suffix})"
            # Make unresolved Confluence links external so Docusaurus doesn't treat them as internal.
            external = d if d.startswith("http") else self.atlassian_base + d
            self.report.links_externalized.append({"page": source_page.rel.as_posix(), "dest": d, "external": external})
            return f"[{label}]({external}{title_suffix})"

        if CONFLUENCE_CREATE_RE.search(d) or ATLASSIAN_SHORT_RE.search(d):
            external = d if d.startswith("http") else self.atlassian_base + d
            self.report.links_externalized.append({"page": source_page.rel.as_posix(), "dest": d, "external": external})
            return f"[{label}]({external}{title_suffix})"

        # Absolute Atlassian links not captured above stay external but are reported.
        if is_http and "atlassian.net" in parsed.netloc.lower():
            self.report.links_externalized.append({"page": source_page.rel.as_posix(), "dest": d, "external": d})
            return f"[{label}]({d}{title_suffix})"

        if is_http:
            return f"[{label}]({raw_dest})"

        # Root-relative /wiki links not matching page pattern: externalize.
        if d.startswith("/wiki/"):
            external = self.atlassian_base + d
            self.report.links_externalized.append({"page": source_page.rel.as_posix(), "dest": d, "external": external})
            return f"[{label}]({external}{title_suffix})"

        # Local markdown page link.
        if d.lower().split("#", 1)[0].split("?", 1)[0].endswith(".md"):
            target = self._resolve_local_page_link(source_page, d)
            if target and not target.skipped:
                anchor = "#" + d.split("#", 1)[1] if "#" in d else ""
                self.report.links_resolved += 1
                if target.is_category_page and not target.content_nonempty:
                    out = "/" + "/".join(target.output_rel.parent.parts) + anchor
                else:
                    out = relative_url(self.docs_out / source_page.output_rel, self.docs_out / target.output_rel) + anchor
                return f"[{label}]({out}{title_suffix})"
            self.report.links_unresolved.append({"page": source_page.rel.as_posix(), "dest": d, "label": label})
            return f"[{label}]({raw_dest})"

        # Root-relative non-Confluence links: report and leave.
        if d.startswith("/"):
            self.report.links_unresolved.append({"page": source_page.rel.as_posix(), "dest": d, "label": label})
            return f"[{label}]({raw_dest})"

        return f"[{label}]({raw_dest})"

    def _convert_callouts(self, text: str) -> str:
        lines = text.splitlines()
        out: List[str] = []
        i = 0
        converted = 0
        while i < len(lines):
            m = CALLOUT_START_RE.match(lines[i])
            if not m:
                out.append(lines[i]); i += 1; continue
            kind = m.group(1).lower()
            converted += 1
            body: List[str] = []
            i += 1
            while i < len(lines):
                line = lines[i]
                if re.match(r"^\s*>", line):
                    body.append(re.sub(r"^\s*>\s?", "", line))
                    i += 1
                elif not line.strip():
                    # Keep a blank if the following line is still quoted.
                    if i + 1 < len(lines) and re.match(r"^\s*>", lines[i + 1]):
                        body.append(""); i += 1
                    else:
                        break
                else:
                    break
            out.append(f":::{kind}")
            out.extend(body)
            out.append(":::")
        self.report.callouts_converted += converted
        return "\n".join(out)

    def _convert_obvious_placeholders(self, text: str) -> str:
        # Work outside fenced code blocks only.
        lines = text.splitlines()
        in_fence = False
        count = 0
        out = []
        tag_re = re.compile(r"<([^<>\n]{1,80})>")
        for line in lines:
            if re.match(r"^\s*```", line):
                in_fence = not in_fence
                out.append(line); continue
            if in_fence:
                out.append(line); continue
            def repl(m):
                nonlocal count
                inner = m.group(1).strip()
                first = inner.split(None,1)[0].lstrip("/").lower()
                if first in COMMON_HTML_TAGS or "=" in inner or inner.startswith("!") or inner.startswith("?"):
                    return m.group(0)
                # Only treat obvious placeholders: spaces, underscores, or ALL_CAPS-ish names.
                if "_" in inner or " " in inner or re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", inner):
                    count += 1
                    return f"`<{inner}>`"
                return m.group(0)
            out.append(tag_re.sub(repl, line))
        self.report.placeholders_converted += count
        return "\n".join(out)

    def _convert_invalid_url_placeholders(self, text: str) -> str:
        # Example observed: https\://ip\_pubblico\_assegnato:4444
        # Process only prose outside fenced and inline code so already-correct `...`
        # placeholders are never wrapped a second time.
        pat = re.compile(r"https\\?://[A-Za-z0-9_.\\-]+(?::\d+)?")
        count = 0

        def convert_segment(segment: str) -> str:
            nonlocal count
            def repl(m):
                nonlocal count
                raw = m.group(0)
                clean = raw.replace("\\:", ":").replace("\\_", "_").replace("\\-", "-")
                try:
                    host = urllib.parse.urlparse(clean).hostname or ""
                except Exception:
                    host = ""
                if "_" in host:
                    count += 1
                    return f"`{clean}`"
                return clean
            return pat.sub(repl, segment)

        out_lines: List[str] = []
        in_fence = False
        for line in text.splitlines():
            if re.match(r"^\s*```", line):
                in_fence = not in_fence
                out_lines.append(line)
                continue
            if in_fence:
                out_lines.append(line)
                continue
            # Preserve inline code spans exactly; convert only the prose between them.
            parts = re.split(r"(`+[^`]*`+)", line)
            for i in range(0, len(parts), 2):
                parts[i] = convert_segment(parts[i])
            out_lines.append("".join(parts))

        self.report.placeholders_converted += count
        return "\n".join(out_lines)

    @staticmethod
    def _strip_heading_markup(text: str) -> str:
        """Reduce Markdown heading text to the visible text used for slug matching."""
        text = html.unescape(text.strip())
        text = re.sub(r"\s*\{#([^}]+)\}\s*$", "", text)
        text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
        text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r"[*_~`]", "", text)
        return re.sub(r"\s+", " ", text).strip()

    @staticmethod
    def _docusaurus_heading_slug(text: str) -> str:
        """Approximate Docusaurus/GitHub heading slugging while preserving Unicode letters.

        Docusaurus heading IDs are GitHub-style: lower-case, punctuation removed,
        whitespace converted to hyphens, with accented letters preserved.
        """
        text = Migrator._strip_heading_markup(text).lower()
        out: List[str] = []
        for ch in text:
            cat = unicodedata.category(ch)
            if ch.isspace():
                out.append("-")
            elif ch in "-_":
                out.append(ch)
            elif cat.startswith("L") or cat.startswith("N"):
                out.append(ch)
            # punctuation/symbols are intentionally dropped
        slug = "".join(out)
        slug = re.sub(r"-+", "-", slug).strip("-")
        return slug

    @staticmethod
    def _anchor_key(text: str) -> str:
        text = urllib.parse.unquote(text)
        text = fix_mojibake(text)
        text = unicodedata.normalize("NFKD", text)
        text = "".join(ch for ch in text if not unicodedata.combining(ch))
        return re.sub(r"[^a-z0-9]+", "", text.lower())

    @staticmethod
    def _anchor_drop_accent_key(text: str) -> str:
        """Legacy Confluence often dropped the accented letter entirely (à -> '')."""
        text = urllib.parse.unquote(text)
        text = fix_mojibake(text).lower()
        out = []
        for ch in text:
            decomp = unicodedata.normalize("NFD", ch)
            if len(decomp) > 1 and any(unicodedata.combining(x) for x in decomp[1:]):
                continue
            if ch.isalnum():
                out.append(ch)
        return "".join(out)

    def _build_anchor_index(self, transformed: Dict[Path, str]) -> None:
        self._anchor_index = {}
        for out_rel, text in transformed.items():
            headings: List[dict] = []
            aliases: Dict[str, List[dict]] = defaultdict(list)
            pseudo: Dict[str, str] = {}
            counts: Dict[str, int] = defaultdict(int)
            in_fence = False
            last_heading_slug = ""
            for line in text.splitlines():
                if re.match(r"^\s*```", line):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue
                m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
                if m:
                    raw = m.group(2)
                    explicit = re.search(r"\s*\{#([^}]+)\}\s*$", raw)
                    visible = self._strip_heading_markup(raw)
                    base = explicit.group(1) if explicit else self._docusaurus_heading_slug(visible)
                    if not base:
                        continue
                    n = counts[base]
                    counts[base] += 1
                    slug = base if n == 0 else f"{base}-{n}"
                    rec = {"text": visible, "slug": slug}
                    headings.append(rec)
                    last_heading_slug = slug
                    for key in {self._anchor_key(visible), self._anchor_key(slug),
                                self._anchor_drop_accent_key(visible), self._anchor_drop_accent_key(slug)}:
                        if key:
                            aliases[key].append(rec)
                    continue

                # Confluence sometimes exported pseudo-headings inside Markdown table cells,
                # e.g. | ### **Funzionalità** |. They do not become real HTML headings.
                # Map their legacy anchors to the nearest preceding real section instead.
                if last_heading_slug and line.lstrip().startswith("|") and "###" in line:
                    for cell in line.split("|"):
                        mm = re.search(r"#{2,6}\s+(.+)", cell)
                        if not mm:
                            continue
                        visible = self._strip_heading_markup(mm.group(1))
                        for key in {self._anchor_key(visible), self._anchor_drop_accent_key(visible)}:
                            if key:
                                pseudo[key] = last_heading_slug
            self._anchor_index[out_rel] = {"headings": headings, "aliases": aliases, "pseudo": pseudo}

    def _resolve_output_target(self, source_page: Page, link_path: str) -> Optional[Page]:
        if not link_path:
            return source_page
        decoded = urllib.parse.unquote(link_path).split("?", 1)[0]
        if decoded.startswith("/"):
            route = decoded.rstrip("/") or "/"
            page = self._page_by_route.get(route)
            if page:
                return page
            # Be tolerant of explicit .md in root-relative links.
            rel = Path(decoded.lstrip("/"))
            if rel.suffix.lower() == ".md":
                return self._page_by_output_rel.get(rel)
            return None

        # Relative Docusaurus Markdown link.
        base = source_page.output_rel.parent
        rel = Path(os.path.normpath((base / decoded).as_posix()))
        if rel.suffix.lower() == ".md":
            return self._page_by_output_rel.get(rel)
        # Relative category/path links may point at an index page.
        direct = self._page_by_output_rel.get(rel.with_suffix(".md"))
        if direct:
            return direct
        return self._page_by_output_rel.get(rel / "index.md")

    def _match_anchor(self, target: Page, fragment: str) -> Optional[str]:
        info = self._anchor_index.get(target.output_rel)
        if not info:
            return None
        frag = urllib.parse.unquote(fragment)
        headings = info["headings"]

        # Exact slug first (including case-only differences).
        for rec in headings:
            if frag == rec["slug"]:
                return rec["slug"]
        for rec in headings:
            if frag.lower() == rec["slug"].lower():
                return rec["slug"]

        keys = [self._anchor_key(frag), self._anchor_drop_accent_key(frag)]
        for key in keys:
            if not key:
                continue
            cands = info["aliases"].get(key, [])
            unique = {c["slug"]: c for c in cands}
            if len(unique) == 1:
                return next(iter(unique.values()))["slug"]
            if key in info["pseudo"]:
                return info["pseudo"][key]

        # Legacy Confluence anchors may prefix the page title before the real section.
        fkey = self._anchor_key(frag)
        suffix = [rec for rec in headings if len(self._anchor_key(rec["text"])) >= 12
                  and fkey.endswith(self._anchor_key(rec["text"]))]
        if len(suffix) == 1:
            return suffix[0]["slug"]

        # Conservative fuzzy fallback: only accept a very strong unique match.
        scored = []
        for rec in headings:
            hkey = self._anchor_key(rec["text"])
            if not fkey or not hkey:
                continue
            score = difflib.SequenceMatcher(None, fkey, hkey).ratio()
            scored.append((score, rec))
        scored.sort(key=lambda x: x[0], reverse=True)
        if scored and scored[0][0] >= 0.92:
            second = scored[1][0] if len(scored) > 1 else 0.0
            if scored[0][0] - second >= 0.05:
                return scored[0][1]["slug"]
        return None

    def _repair_anchors_in_text(self, page: Page, text: str) -> str:
        def repl(m: re.Match) -> str:
            is_image = bool(m.group(1))
            if is_image:
                return m.group(0)
            label = m.group(2)
            raw_dest = m.group(3)
            dest, title_suffix = split_dest_and_title(raw_dest)
            if "#" not in dest:
                return m.group(0)
            if dest.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                return m.group(0)
            link_path, fragment = dest.split("#", 1)
            if not fragment:
                return m.group(0)
            target = self._resolve_output_target(page, link_path)
            if not target:
                return m.group(0)
            self.report.anchor_links_seen += 1
            replacement = self._match_anchor(target, fragment)
            if replacement:
                if replacement != fragment:
                    self.report.anchors_repaired += 1
                new_dest = f"{link_path}#{replacement}"
                return f"[{label}]({new_dest}{title_suffix})"
            self.report.anchors_unresolved.append({
                "page": page.output_rel.as_posix(),
                "target": target.output_rel.as_posix(),
                "fragment": fragment,
                "dest": dest,
            })
            return m.group(0)
        return MD_LINK_RE.sub(repl, text)

    def _normalize_heading_levels(self, text: str) -> str:
        """Ensure the document body starts at H2 when Confluence exported H1 sections.

        In Docusaurus the document title is the page H1. Confluence exports often use
        additional H1 headings for sections, which is semantically invalid and, notably,
        Docusaurus' anchor checker does not register H1 hash-links like normal section
        headings. When a page contains body H1s, shift every ATX heading down one level
        (H1->H2, H2->H3, ...; H6 stays H6) to preserve the relative hierarchy.
        """
        lines = text.splitlines()
        in_fence = False
        levels: List[int] = []
        for line in lines:
            if re.match(r"^\s*```", line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            m = re.match(r"^(#{1,6})\s+", line)
            if m:
                levels.append(len(m.group(1)))
        if 1 not in levels:
            return text

        self.report.heading_pages_normalized += 1
        out: List[str] = []
        in_fence = False
        shifted = 0
        for line in lines:
            if re.match(r"^\s*```", line):
                in_fence = not in_fence
                out.append(line)
                continue
            if in_fence:
                out.append(line)
                continue
            m = re.match(r"^(#{1,6})(\s+.*)$", line)
            if m:
                level = len(m.group(1))
                new_level = min(6, level + 1)
                if new_level != level:
                    shifted += 1
                out.append("#" * new_level + m.group(2))
            else:
                out.append(line)
        self.report.headings_shifted += shifted
        return "\n".join(out)

    def _add_explicit_heading_ids(self, text: str) -> str:
        """Add stable ASCII IDs to Markdown headings.

        This avoids relying on github-slugger details (punctuation, Unicode accents,
        non-breaking spaces, duplicate suffixes) and makes future heading edits safer.
        The output files are .md/CommonMark, where Docusaurus supports {#id} syntax.
        """
        lines = text.splitlines()
        in_fence = False
        used: Dict[str, int] = defaultdict(int)
        out: List[str] = []
        added = 0
        for line in lines:
            if re.match(r"^\s*```", line):
                in_fence = not in_fence
                out.append(line)
                continue
            if in_fence:
                out.append(line)
                continue
            m = re.match(r"^(#{1,6})(\s+)(.+?)\s*$", line)
            if not m:
                out.append(line)
                continue
            hashes, spacing, raw = m.groups()
            existing = re.search(r"\s*\{#([^}]+)\}\s*$", raw)
            if existing:
                eid = existing.group(1)
                used[eid] += 1
                out.append(line)
                continue
            visible = self._strip_heading_markup(raw)
            base = slugify(visible, "section")
            n = used[base]
            used[base] += 1
            eid = base if n == 0 else f"{base}-{n}"
            out.append(f"{hashes}{spacing}{raw} {{#{eid}}}")
            added += 1
        self.report.heading_ids_added += added
        return "\n".join(out)

    def _frontmatter(self, page: Page, body: str) -> str:
        body = body.lstrip("\ufeff")
        # If existing frontmatter is present, inject title only when missing.
        if body.startswith("---\n"):
            end = body.find("\n---", 4)
            if end != -1:
                fm = body[4:end]
                rest = body[end + 4:].lstrip("\n")
                if not re.search(r"(?m)^title\s*:", fm):
                    fm = f"title: {json.dumps(page.title, ensure_ascii=False)}\n" + fm
                return f"---\n{fm.rstrip()}\n---\n\n{rest}"
        return f"---\ntitle: {json.dumps(page.title, ensure_ascii=False)}\n---\n\n{body.lstrip()}"

    def transform_page(self, page: Page) -> str:
        text = page.source.read_text(encoding="utf-8", errors="replace")
        fixed = fix_mojibake(text)
        if fixed != text:
            self.report.filename_mojibake_fixed += 1
        text = fixed
        text = self._convert_callouts(text)
        text = self._convert_obvious_placeholders(text)

        def repl(m: re.Match) -> str:
            is_image = bool(m.group(1))
            label = m.group(2)
            raw_dest = m.group(3)
            return self._rewrite_link(page, is_image, label, raw_dest)
        text = MD_LINK_RE.sub(repl, text)
        # Convert invalid placeholder URLs that occur as plain text only after Markdown
        # links have been rewritten, so we never inject backticks into a link destination.
        text = self._convert_invalid_url_placeholders(text)
        text = self._normalize_heading_levels(text)
        text = self._add_explicit_heading_ids(text)
        return self._frontmatter(page, text)

    def generate_categories(self) -> None:
        # Nested categories only. Macro _category_.json files are intentionally omitted so the
        # user's manually configured five macro categories can be preserved when merging.
        for key in sorted(self.category_dirs):
            if len(key) <= 1:
                continue
            label = self.category_labels.get(key, key[-1].replace("-", " ").title())
            target = self.docs_out.joinpath(*key) / "_category_.json"
            data = {"label": label, "collapsible": True, "collapsed": True}
            if key not in self.category_has_index:
                data["link"] = {
                    "type": "generated-index",
                    "title": label,
                    "slug": "/" + "/".join(key),
                }
            if self.apply:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            self.report.categories_generated += 1

    def run(self) -> None:
        self.scan()
        if self.apply:
            if self.output.exists():
                raise RuntimeError(f"La directory output esiste già: {self.output}\nEliminala o scegli un altro --output.")
            self.docs_out.mkdir(parents=True, exist_ok=False)
            self.static_out.mkdir(parents=True, exist_ok=True)

        transformed_pages: Dict[Path, str] = {}
        writable_pages: List[Page] = []
        for page in self.pages:
            if page.skipped:
                self.report.pages_skipped += 1
                continue
            # Empty category page becomes a generated index category; don't write empty index.md.
            if page.is_category_page and not page.content_nonempty:
                self.report.pages_skipped += 1
                continue
            transformed_pages[page.output_rel] = self.transform_page(page)
            writable_pages.append(page)
            self.report.pages_written += 1

        # Second pass: now every target page and heading is known, repair legacy fragments.
        self._build_anchor_index(transformed_pages)
        for page in writable_pages:
            transformed = self._repair_anchors_in_text(page, transformed_pages[page.output_rel])
            transformed_pages[page.output_rel] = transformed
            if self.apply:
                target = self.docs_out / page.output_rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(transformed, encoding="utf-8")

        self.generate_categories()
        if self.apply:
            self.write_reports()

    def write_reports(self) -> None:
        report_dict = self.report.__dict__
        (self.output / "migration-report.json").write_text(
            json.dumps(report_dict, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        lines = [
            "# Confluence → Docusaurus migration report",
            "",
            f"Source root: `{self.root}`",
            "",
            "## Summary",
            "",
            f"- Markdown pages scanned: **{self.report.pages_total}**",
            f"- Pages written: **{self.report.pages_written}**",
            f"- Pages skipped: **{self.report.pages_skipped}**",
            f"- Nested categories generated: **{self.report.categories_generated}**",
            f"- Local assets referenced: **{self.report.assets_referenced}**",
            f"- Assets copied: **{self.report.assets_copied}**",
            f"- Broken asset paths automatically repaired: **{self.report.assets_fixed_path}**",
            f"- Missing assets: **{len(self.report.assets_missing)}**",
            f"- Ambiguous assets: **{len(self.report.assets_ambiguous)}**",
            f"- Video embeds converted from image syntax: **{self.report.video_embeds_converted}**",
            f"- Markdown links processed: **{self.report.links_total}**",
            f"- Internal links resolved: **{self.report.links_resolved}**",
            f"- Unresolved internal links: **{len(self.report.links_unresolved)}**",
            f"- Confluence/Atlassian links left external for review: **{len(self.report.links_externalized)}**",
            f"- Callouts converted: **{self.report.callouts_converted}**",
            f"- Obvious technical placeholders converted to code: **{self.report.placeholders_converted}**",
            f"- Pages with H1 body sections normalized: **{self.report.heading_pages_normalized}**",
            f"- Markdown headings shifted down one level: **{self.report.headings_shifted}**",
            f"- Stable explicit heading IDs added: **{self.report.heading_ids_added}**",
            f"- Internal anchor links checked: **{self.report.anchor_links_seen}**",
            f"- Legacy anchors automatically repaired: **{self.report.anchors_repaired}**",
            f"- Anchor links still unresolved: **{len(self.report.anchors_unresolved)}**",
            "",
        ]
        def section(title: str, items: Sequence[dict], limit: int = 500):
            if not items: return
            lines.extend([f"## {title}", ""])
            for x in items[:limit]:
                lines.append("- `" + json.dumps(x, ensure_ascii=False) + "`")
            if len(items) > limit:
                lines.append(f"- … plus {len(items)-limit} more (see migration-report.json)")
            lines.append("")
        section("Unresolved internal links — REVIEW REQUIRED", self.report.links_unresolved)
        section("Unresolved anchors — REVIEW REQUIRED", self.report.anchors_unresolved)
        section("Atlassian links left external — REVIEW REQUIRED", self.report.links_externalized)
        section("Missing assets — REVIEW REQUIRED", self.report.assets_missing)
        section("Ambiguous assets — VERIFY CHOICE", self.report.assets_ambiguous)
        section("Duplicate pages skipped", self.report.duplicate_pages_skipped)
        section("Unclassified root pages", self.report.root_orphans)
        (self.output / "migration-report.md").write_text("\n".join(lines), encoding="utf-8")

    def print_summary(self) -> None:
        mode = "APPLY" if self.apply else "DRY RUN"
        print(f"\n=== Confluence -> Docusaurus migration ({mode}) ===")
        print(f"Export root:          {self.root}")
        print(f"Markdown pages:       {self.report.pages_total}")
        print(f"Pages to write:       {self.report.pages_written}")
        print(f"Pages skipped:        {self.report.pages_skipped}")
        print(f"Nested categories:    {self.report.categories_generated}")
        print(f"Assets referenced:    {self.report.assets_referenced}")
        print(f"Assets to copy:       {self.report.assets_copied}")
        print(f"Asset paths repaired: {self.report.assets_fixed_path}")
        print(f"Missing assets:       {len(self.report.assets_missing)}")
        print(f"Ambiguous assets:     {len(self.report.assets_ambiguous)}")
        print(f"Video embeds fixed:   {self.report.video_embeds_converted}")
        print(f"Internal links fixed: {self.report.links_resolved}")
        print(f"Unresolved links:     {len(self.report.links_unresolved)}")
        print(f"Links left external:  {len(self.report.links_externalized)}")
        print(f"Callouts converted:   {self.report.callouts_converted}")
        print(f"Placeholders fixed:   {self.report.placeholders_converted}")
        print(f"Heading pages fixed:  {self.report.heading_pages_normalized}")
        print(f"Headings shifted:     {self.report.headings_shifted}")
        print(f"Heading IDs added:    {self.report.heading_ids_added}")
        print(f"Anchor links checked: {self.report.anchor_links_seen}")
        print(f"Anchors repaired:     {self.report.anchors_repaired}")
        print(f"Unresolved anchors:   {len(self.report.anchors_unresolved)}")
        if not self.apply:
            print("\nNessun file è stato modificato o creato (dry-run).")
            print("Quando il riepilogo ti convince, rilancia con --apply e una directory --output nuova.")
        else:
            print(f"\nOutput creato in: {self.output}")
            print(f"Report: {self.output / 'migration-report.md'}")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Migra un export Markdown di Confluence verso una struttura Docusaurus sicura.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--source", required=True, help="Cartella export Confluence oppure file .zip")
    p.add_argument("--output", default="migration-output", help="Directory di destinazione (usata solo con --apply)")
    p.add_argument("--apply", action="store_true", help="Crea davvero l'output. Senza questa opzione è sempre dry-run.")
    p.add_argument("--atlassian-base", default="https://cloudfireit.atlassian.net", help="Base URL per link Atlassian non risolti")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    source = Path(args.source).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    if not source.exists():
        print(f"ERRORE: source non trovato: {source}", file=sys.stderr)
        return 2

    tempdir = None
    try:
        if source.is_file() and source.suffix.lower() == ".zip":
            tempdir = tempfile.TemporaryDirectory(prefix="confluence-export-")
            with zipfile.ZipFile(source) as zf:
                zf.extractall(tempdir.name)
            source_dir = Path(tempdir.name).resolve()
        elif source.is_dir():
            source_dir = source
        else:
            print("ERRORE: --source deve essere una cartella o un file .zip", file=sys.stderr)
            return 2

        root = find_export_root(source_dir).resolve()
        mig = Migrator(root=root, output=output, apply=args.apply, atlassian_base=args.atlassian_base)
        mig.run()
        mig.print_summary()
        return 0
    except Exception as e:
        print(f"\nERRORE: {e}", file=sys.stderr)
        return 1
    finally:
        if tempdir is not None:
            tempdir.cleanup()


if __name__ == "__main__":
    raise SystemExit(main())
