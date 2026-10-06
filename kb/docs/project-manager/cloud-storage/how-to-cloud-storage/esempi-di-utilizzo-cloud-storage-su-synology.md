---
title: "Esempi di utilizzo Cloud Storage su Synology"
---

## Introduzione {#introduzione}

Diversi software presenti nello store di Synology permettono di utilizzare il Cloud Storage per backup o sincronizzazione dei contenuti del vostro NAS.

## Prerequisiti {#prerequisiti}

Scaricare e installare le App specifiche di backup o di sincronizzazione.

Di seguito l'esempio di "Hyper backup" e di "Cloud Sync"

## Guida passo-passo {#guida-passo-passo}

### Hyper Backup {#hyper-backup}

![](/kb-assets/4155fb1e7a-b1.png)

- Installare e aprire "Hyper Backup"
- Selezionare "Archivio S3" e cliccare "Avanti

![](/kb-assets/bb0d155faf-b2.png)

- Inserire i parametri per la connessione come da immagine, specificando **ACCESS** e **SECRET KEYs** in vostro possesso.
- In caso di correttezza dei dati potrete selezionare un bucket esistente (in caso di account non vergine), o crearne uno nuovo.

:::warning
Seguendo il Wizard avrete modo di configurare il vostro piano di backup come con vari altri software, specificando sorgente, destinazione e schedulazione.
:::

### Cloud Sync {#cloud-sync}

![](/kb-assets/f4e1c24cb5-c1.png)

- Installare e aprire "Cloud Sync"
- Selezionare "S3 storage" e cliccare "Avanti"

![](/kb-assets/690760e181-c2.png)

- Inserire i parametri per la connessione come da immagine, specificando ACCESS e SECRET KEYs in vostro possesso.
- In caso di correttezza dei dati potrete selezionare un bucket esistente (in caso di account non vergine), o crearne uno nuovo.

![](/kb-assets/d93aa2c506-c3.png)

:::warning
A questo punto proseguendo il Wizard avrete modo di configurare la sincronizzazione dei contenuti, in modo analogo al backup.

[!NOTE]
Altri applicativi Synology hanno modalità simili per interagire con i vostri bucket sul Cloud Storage e i parametri principali sono sempre quelli forniti in fase di attivazione.
:::

  

  

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Guida passo-passo](#guida-passo-passo)
-   [Hyper Backup](#hyper-backup)
-   [Cloud Sync](#cloud-sync)
  
  -   Filter by label
* * *
**Articoli collegati**


##### Filter by label {#filter-by-label}

There are no items with the selected labels at this time.
:::