## Introduzione

Drive4Business non dispone di un client nativo per Linux.

Il metodo più pratico per utilizzare il prodotto sui sistemi operativi Linux è via web (su una distribuzione Desktop). Se vi fosse la necessità di accedere alla vostra share via file system dovrete effettuare un mount via webdav.

Ovviamente il metodo è valido anche per le distribuzioni server.

Di seguito i comandi per attuare il mount su sistemi con gestore pacchetti "**APT**".

## Guida passo-passo

1. Aprire un terminale.
2. Creare il punto di mount nella posizione a voi più comoda con privilegi elevati via sudo oppure direttamente con l'utente di **root:**  
```
sudo mkdir /mnt/d4b
```
  
3. Installare il pacchetto ***davfs2*** e selezionare nel prompt di sicurezza l'opzione desiderata:
```
sudo apt install davfs2
```
  
4. Procedere con il mount eseguendo il seguente comando, ed inserire le credenziali richieste *(user* e *password* del vostro account **D4B**):
```
sudo mount -t davfs https://drive4business.cloudfire.it/dav /mnt/d4b/
```
  
5. Ora nel percorso **/mnt/d4b** troverete la *root* della vostra share Drive4Business da sfogliare da terminale o da GUI.

> [!INFO]
> I limiti e le prestazioni della share sono date dal protocollo webdav stesso.

  

  

  

> [!NOTE]
> **Sommario**
> 
> 
> 
> - [Introduzione](#introduzione)
> - [Guida passo-passo](#guida-passo-passo)
> -   Filter by label
> * * *
> **Articoli collegati**
> 
> 
> ##### Filter by label
> 
> There are no items with the selected labels at this time.