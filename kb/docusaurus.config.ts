import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Benvenuto',
  tagline: 'Knowledge Base aziendale',
  favicon: 'img/cloudfire_icon.png',
  // Per ora lavoriamo solo localmente.
  // Quando pubblicheremo la KB sostituiremo questo URL.
  url: 'https://kb.cloudfire.it',
  baseUrl: '/',

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'it',
    locales: ['it'],
  },

  // I file .md vengono trattati come Markdown standard.
  // Se in futuro ci serviranno componenti React useremo .mdx.
  markdown: {
    format: 'detect',
  },

  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.ts',
        },

        blog: false,

        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themes: [
  [
    require.resolve('@easyops-cn/docusaurus-search-local'),
    {
      hashed: 'filename',
      language: ['it', 'en'],
      indexDocs: true,
      indexBlog: false,
      indexPages: false,
      docsRouteBasePath: '/',
      searchBarShortcutHint: true,
    },
  ],
],

  themeConfig: {
    navbar: {
      logo: {
      alt: 'CloudFire',
      src: 'img/cloudfire_logo.svg',
      srcDark: 'img/cloudfire_logo_dark.svg',
      href: '/',
    },
      items: [
        {
        type: 'search',
        position: 'left',
        className: 'kb-navbar-search'
      },
      ],
    },

    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()}`,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;