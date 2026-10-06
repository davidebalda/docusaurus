---
title: "Aggiungere Cloud Storage a Veeam"
---

## Introduzione

Il Cloud Storage può essere aggiunto come repository (o external repository) nella console di Veeam a partire dalla versione 9.5 U4.

Di solito tale configurazione viene utilizzata per il tiering degli elementi di backup "datati".

## Prerequisiti

Oltre all'account di Cloud Backup dovrete essere già in possesso di un'infrastruttura Veeam B&R 9.5 U4

## Guida passo-passo

![](/kb-assets/ce921a733e-v111.png)

- Portarsi in "Backup Infrastructure" e selezionare "Backup Repositories" (la procedura è analoga per "External Repositories"); cliccare quindi "Object storage".

![](/kb-assets/6ac589f3e9-v1.png)

- Selezionare "S3 Compatible"

![](/kb-assets/e7ceaa36e3-v2.png)

- Inserire un nome identificativo all'interno di Veeam.

![](/kb-assets/bc30268484-v3.png)

- Inserire quindi il service point "[cloudfirestorage.it](http://cloudfirestorage.it)" e le vostre ACCESS e SECRET KEYs.

![](/kb-assets/37976d1343-v4.png)

- Mantenere la region di default.

![](/kb-assets/82c6b8ecd8-v5.png)

- Procedere a selezionare/creare il bucket.

![](/kb-assets/c6e055a070-v6.png)

- Procedere a selezionare/creare la cartella.

![](/kb-assets/0d9453e5a7-v7.png)

- Concludere la creazione della repository.

![](/kb-assets/919276bca3-v8.png)

- Ora la repository verrà visualizzata con tutte le altre repository.

  

  

  

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Guida passo-passo](#guida-passo-passo)
-   Filter by label
* * *
**Articoli collegati**


##### Filter by label

There are no items with the selected labels at this time.
:::