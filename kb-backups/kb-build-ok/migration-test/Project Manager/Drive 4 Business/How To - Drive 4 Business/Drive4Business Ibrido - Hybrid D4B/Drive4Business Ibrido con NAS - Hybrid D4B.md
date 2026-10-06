Questa pagina spiega come installare Drive4Business se si dispone di un NAS sulla propria rete locale.

Drive4Business non offre un agente specifico per i NAS, dunque per poterne sfruttare il potenziale bisogna seguire questi passaggi.

## Prerequisiti di installazione

Prima di proseguire con la configurazione del Drive4Business, controllare di disporre i seguenti elementi, necessari all’installazione.

1. Disporre di un computer che svolgerà la funzione di ponte tra il NAS e il Drive4Business in cloud
2. Possedere un NAS e impostarlo come Disco di rete locale con un suo percorso dati sul dispositivo specificato nel punto soprastante
3. Essere in possesso delle credenziali del Drive4Business (se non le possiedi visita questo link per [Attivare il servizio Drive4Business](../../../drive-4-business/gestione-del-servizio-drive-4-business.md))
4. Aver installato sul computer il Server Agent di Drive4Business

Il punto di partenza deve essere simile a quello mostrato di seguito

![](./attachments/D4B%20-%20Hybrid%20NAS%20-%201.png)

## Cosa sono le Attached Folders?

Le Attached Folders sono cartelle sulla macchina locale che possono essere aggiunte manualmente su Drive4Business.

La loro peculiarità è che mantengono attiva la sincronizzazione bidirezionale verso il cloud e il loro contenuto locale. Come nello scenario Drive4Business Ibrido classico.

Possono essere gestite direttamente dal portale Drive4Business su Web, sotto la voce Attached Folders, come se fossero delle Team Folders.

# Come installare il Drive4Business Ibrido con NAS

Una volta installato l’Agente Server e il Nas sulla macchina Windows locale, procedere con in seguenti passaggi:

1. Apri il Client Server e clicca sulla voce **Attached Folders**  
![](./attachments/D4B%20-%20Hybrid%20NAS%20-%202.png)
2. Premi sull’icona **Attach CISF Share**
3. Nella finestra di dialogo mostrata, specifica il **Name** che deve assumere la cartella sul Drive4Business, la sua **Location** nella rete locale (\\\\host\\share\\folder), l’**Username** e la **Password** associata all’utente per accedere al NAS  
Una volta inserite le richieste, premi su **Attach CIFS Share**.  
![](./attachments/D4B%20-%20Hybrid%20NAS%20-%204.png)
4. A questo punto avremo aggiunto la nostra Attached Folder e la sincronizzazione bidirezionale partirà in automatico.  
![](./attachments/D4B%20-%20Hybrid%20NAS%20-%205.png)
5. A questo punto è necessario attendere che tutti i file presenti sul NAS vengano sincronizzati verso il Drive4Business.  
Tramite le icone poste sulla destra della cartella inserita è possibile eseguire diverse opzioni, tra cui: Forzare la sincronizzazione, monitorare quanti file non sono ancora stati sincronizzati, interrompere la sincronizzazione ed eliminare la cartella.

> [!INFO]
> Qualora si presentino errori ti invitiamo a contattare il nostro supporto tecnico tramite il nostro [Help Center](https://task.cloudfire.it/plugins/servlet/desk/portal/1) o scrivendo una email all’indirizzo [help@cloudfire.it](mailto:help@cloudfire.it).