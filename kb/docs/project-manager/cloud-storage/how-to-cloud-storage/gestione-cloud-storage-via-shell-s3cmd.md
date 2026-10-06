---
title: "Gestione Cloud Storage via shell: S3cmd"
---

## Introduzione {#introduzione}

E' possibile anche gestire i bucket e i contenuti del vostro account Cloud Storage via command line su tutti i sistemi con il seguente tool.

## Prerequisiti {#prerequisiti}

Python e pip installati sul dispositivo.

## Guida passo-passo {#guida-passo-passo}

- Installare il tool usando il pacchetto "pip":
```
pip install s3cmd
```

- Creare un file di configurazione chiamato *".s3cfg"* nella home dell'account con il seguente contenuto con i vostri access e secret keys:
```
[default]
access_key = <your-key>
bucket_location = US
check_ssl_certificate = True
check_ssl_hostname = True
default_mime_type = binary/octet-stream
delay_updates = False
delete_after = False
delete_after_fetch = False
delete_removed = False
dry_run = False
enable_multipart = True
encoding = UTF-8
encrypt = False
follow_symlinks = False
force = False
get_continue = False
gpg_passphrase = 
guess_mime_type = True
host_base = s3.scalablestorage.it
host_bucket = <your-bucket-name>.s3.scalablestorage.it
human_readable_sizes = False
invalidate_default_index_on_cf = False
invalidate_default_index_root_on_cf = True
invalidate_on_cf = False
limit = -1
limitrate = 0
long_listing = False
max_delete = -1
multipart_chunk_size_mb = 15
multipart_max_chunks = 10000
preserve_attrs = True
progress_meter = True
put_continue = False
recursive = False
recv_chunk = 65536
reduced_redundancy = False
requester_pays = False
restore_days = 1
restore_priority = Standard
secret_key = <your-key> 
send_chunk = 65536
server_side_encryption = False
signature_v2 = False
signurl_use_https = False
skip_existing = False
socket_timeout = 300
stats = False
stop_on_error = False
storage_class = 
throttle_max = 100
urlencoding_mode = normal
use_http_expect = False
use_https = True
use_mime_magic = True
verbosity = WARNING
```
Eseguendo un comando tipo "**s3cmd ls**" un *warning/errore* vi indicherà dove collocare il file di configurazione.
- Agire sui contenuti del vostro Cloud Storage con i comandi specifici del tool che potete trovare al seguente link  [https://s3tools.org/s3cmd-howto](https://s3tools.org/s3cmd-howto)  

  

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Guida passo-passo](#guida-passo-passo)
-   Filter by label
* * *
**Articoli collegati**


##### Filter by label {#filter-by-label}

There are no items with the selected labels at this time.
:::