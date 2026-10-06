## Introduzione

Il Cloud Storage può essere aggiunto come repository (o external repository) nella console di Veeam a partire dalla versione 9.5 U4.

Di solito tale configurazione viene utilizzata per il tiering degli elementi di backup "datati".

## Prerequisiti

Oltre all'account di Cloud Backup dovrete essere già in possesso di un'infrastruttura Veeam B&R 9.5 U4

## Guida passo-passo

![](./attachments/v111.PNG)

- Portarsi in "Backup Infrastructure" e selezionare "Backup Repositories" (la procedura è analoga per "External Repositories"); cliccare quindi "Object storage".

![](./attachments/v1.PNG)

- Selezionare "S3 Compatible"

![](./attachments/v2.PNG)

- Inserire un nome identificativo all'interno di Veeam.

![](./attachments/v3.PNG)

- Inserire quindi il service point "[cloudfirestorage.it](http://cloudfirestorage.it)" e le vostre ACCESS e SECRET KEYs.

![](./attachments/v4.PNG)

- Mantenere la region di default.

![](./attachments/v5.PNG)

- Procedere a selezionare/creare il bucket.

![](./attachments/v6.PNG)

- Procedere a selezionare/creare la cartella.

![](./attachments/v7.PNG)

- Concludere la creazione della repository.

![](./attachments/v8.PNG)

- Ora la repository verrà visualizzata con tutte le altre repository.

  

  

  

> [!NOTE]
> **Sommario**
> 
> 
> 
> - [Introduzione](#introduzione)
> - [Prerequisiti](#prerequisiti)
> - [Guida passo-passo](#guida-passo-passo)
> -   Filter by label
> * * *
> **Articoli collegati**
> 
> 
> ##### Filter by label
> 
> There are no items with the selected labels at this time.