---
title: "Backup di caselle Office 365 - Acronis Cyber Protect Cloud"
---

## Introduzione {#introduzione}

Per utilizzare queste funzionalità esse devono essere comprese nel vostro piano contrattuale.

Nel caso specifico del backup tramite agent in locale, l'agent dovrà essere installato, operativo e online su una macchina windows.

In tutti i casi si necessita delle credenziali dell'account administrator globale del site di office 365 che si intende proteggere.

## Perché eseguire il backup dei dati di Office 365? {#perche-eseguire-il-backup-dei-dati-di-office-365}

Sebbene Microsoft Office 365 sia un set di servizi cloud, i backup regolari forniscono un ulteriore livello di protezione dagli errori degli utenti e da azioni dannose intenzionali. È possibile ripristinare gli elementi eliminati da un backup anche dopo la scadenza del periodo di conservazione di Office 365. Inoltre, è possibile conservare una copia locale delle caselle di posta di Exchange Online se richiesto a fini di conformità alle normative.

#### Agente per Office 365 {#agente-per-office-365}

A seconda della funzionalità desiderata, sarà possibile installare l'Agente per Office 365 in locale, utilizzare l'agente installato nel cloud o entrambe le opzioni. La tabella seguente riepiloga le funzionalità dell’agente locale e cloud.

|     |     |     |
| --- | --- | --- |
|     | Agente locale per Office 365 | Agente cloud per Office 365 |
| Elementi dati di cui è possibile eseguire il backup | Exchange Online: caselle di posta utente e condivise | - Exchange Online: caselle di posta utente, di gruppo e condivise<br>- OneDrive: file e cartelle utenti<br>- SharePoint Online: raccolte di siti classici, siti di gruppo inclusi i siti dei team, siti di comunicazione, singoli elementi dati |
| Backup delle caselle di posta di archiviazione (In-Place Archive) | No  | Sì  |
| Pianificazione del backup | [Definita dall’utente](https://www.acronis.com/it-it/support/documentation/BackupService/index.html#33511.html) | Non è modificabile. Ogni piano di backup viene eseguito ogni giorno alla stessa ora.\* |
| Posizioni di backup | Archivio nel cloud, cartella locale o di rete | Solo archivio nel cloud |
| Protezione automatica di nuovi utenti, gruppi, siti di Office 365 | No  | Sì, con applicazione di un piano di backup ai gruppi Tutti gli utenti, Tutti i gruppi, Tutti i siti |
| Protezione di più di una organizzazione di Office 365 | No  | Sì  |
| Ripristino granulare | Sì  | Sì  |
| Ripristino in altro utente di un’organizzazione | Sì  | Sì  |
| Ripristino in altra organizzazione | No  | Sì  |
| Ripristino di un server Microsoft Exchange locale | No  | No  |

\* Poiché un agente cloud serve più clienti, stabilisce l’orario di avvio di ogni piano di backup in modo autonomo, per garantire l’uniformità del carico durante il giorno e una qualità del servizio paritaria per tutti i clienti.

#### Limitazioni {#limitazioni}

La creazione automatica di utenti, gruppi o siti durante un ripristino non è consentita. Se, ad esempio, si desidera ripristinare un sito di SharePoint Online che è stato eliminato, creare innanzitutto un nuovo sito manualmente, quindi specificarlo come sito di destinazione durante il ripristino.

#### Diritti utenti necessari {#diritti-utenti-necessari}

##### Nel servizio di Backup {#nel-servizio-di-backup}

Qualsiasi Agente per Office 365, locale o cloud, deve essere registrato in un account di amministratore del cliente.

##### Nel servizio di Office365 {#nel-servizio-di-office365}

All'account deve essere assegnato il ruolo Amministratore globale in Microsoft Office 365.

- L’agente locale eseguirà l’accesso a Office 365 utilizzando tale account. Per abilitare l’accesso dell’agente ai contenuti di tutte le caselle di posta, all’account verrà assegnato il ruolo di gestione ApplicationImpersonation (Rappresentazione dell’applicazione).
- L’agente cloud non accede a Office 365. Le autorizzazioni necessarie all’agente vengono fornite direttamente da Microsoft Office 365. È necessario confermare la concessione di tali autorizzazioni una sola volta, dopo la registrazione come amministratore globale. L’agente non memorizza le credenziali dell’account e non le utilizza per eseguire attività di backup e ripristino.

## Utilizzo dell’Agente installato in locale per Office 365 {#utilizzo-dell-agente-installato-in-locale-per-office-365}

### Aggiunta di un’organizzazione di Office 365 {#aggiunta-di-un-organizzazione-di-office-365}

1. Accedere alla console di backup come amministratore aziendale.
2. Fare clic sull'icona dell'account nell'angolo superiore destro, quindi su *Download* > **Agente per Office 365**.
3. Scaricare l'agente e installarlo nella macchina Windows connessa a Internet.
4. Dopo aver completato l'installazione, fare clic su Dispositivi > Microsoft Office 365 e quindi immettere le credenziali di amministratore globale di Microsoft Office 365
5. Importante In un'organizzazione (gruppo aziendale) deve essere presente un unico Agente per Office 365 in locale.

Gli elementi dati dell’organizzazione vengono visualizzati nella console di backup, nella pagina Microsoft Office 365.

#### Protezione caselle {#protezione-caselle}

##### Di quali elementi è possibile eseguire il backup? {#di-quali-elementi-e-possibile-eseguire-il-backup}

È possibile eseguire il backup delle caselle di posta utente e delle caselle condivise. Non è possibile eseguire il backup delle caselle di posta di archiviazione (In-Place Archive) e delle caselle di posta di gruppo.

##### Quali elementi è possibile ripristinare? {#quali-elementi-e-possibile-ripristinare}

Dal backup di una casella postale è possibile ripristinare i seguenti elementi:

- Caselle postali
- Cartelle e-mail
- Messaggi e-mail
- Eventi di calendario
- Attività
- Contatti
- Voci del diario
- Note

È possibile utilizzare la ricerca per individuare gli elementi.

Quando una casella di posta viene ripristinata in una casella di posta esistente, vengono sovrascritti gli elementi già esistenti con ID corrispondenti.

:::info
Il ripristino di elementi di caselle di posta non sovrascrive alcun elemento. Il percorso completo di un elemento della casella di posta viene invece ricreato nella cartella di destinazione.
:::

#### Selezione delle caselle di posta {#selezione-delle-caselle-di-posta}

Selezionare le caselle di posta come descritto di seguito, quindi specificare eventuali altre impostazioni del piano di backup [in modo appropriato](https://www.acronis.com/it-it/support/documentation/BackupService/index.html#33579.html).

Per selezionare le caselle di posta:

1. Fare clic su Microsoft Office 365.
2. Se richiesto, accedere a Microsoft Office 365 come amministratore globale.
3. Selezionare le caselle di posta di cui si desidera eseguire il backup.
4. Fare clic su Backup.

#### Ripristino di caselle di posta {#ripristino-di-caselle-di-posta}

1. Fare clic su Microsoft Office 365.
2. Selezionare la casella di posta da ripristinare e fare clic su Ripristina.È possibile cercare le caselle di posta per nome. I caratteri jolly non sono supportati.Se la casella di posta è stata eliminata, selezionarla nella [scheda Backup](https://www.acronis.com/it-it/support/documentation/BackupService/index.html#35883.html), quindi fare clic su Mostra backup.
3. Selezionare un punto di ripristino. Notare che i punti di ripristino vengono filtrati in base alla posizione.
4. Fare clic su ***Ripristina > Casella di posta***.
5. In Casella postale di destinazione, visualizzare, cambiare o specificare la casella di posta di destinazione.Per impostazione predefinita, viene selezionata la casella di posta originale. Se tale casella di posta non esiste, è necessario specificare la casella di posta di destinazione.
6. Fare clic su *Avvia ripristino*.

#### Ripristino di elementi delle caselle postali {#ripristino-di-elementi-delle-caselle-postali}

1. Fare clic su Microsoft Office 365.
2. Selezionare la casella di posta che conteneva in origine gli elementi da ripristinare, quindi fare clic su Ripristina.È possibile cercare le caselle di posta per nome. I caratteri jolly non sono supportati.Se la casella di posta è stata eliminata, selezionarla nella [scheda Backup](https://www.acronis.com/it-it/support/documentation/BackupService/index.html#35883.html), quindi fare clic su Mostra backup.
3. Selezionare un punto di ripristino. Notare che i punti di ripristino vengono filtrati in base alla posizione.
4. Fare clic su ***Ripristina > Messaggi e-mail***.
5. Selezionare gli elementi che si desidera ripristinare.Sono disponibili le opzioni di ricerca seguenti: I caratteri jolly non sono supportati.
-   Per i messaggi e-mail: ricerca per oggetto, mittente, destinatario e data.
-   Per gli eventi: ricerca per titolo e data.
-   Per le attività: ricerca per titolo e data.
-   Per i contatti: ricerca per nome, indirizzo e-mail e numero di telefono.Quando è selezionato un messaggio e-mail, è possibile fare clic su Mostra il contenuto per visualizzarne il contenuto, inclusi gli allegati.Suggerimento  Fare clic sul nome di un file allegato per scaricarlo.Quando è selezionato un messaggio e-mail, è possibile fare clic su Invia come e-mail per inviare il messaggio a un indirizzo e-mail. Il messaggio verrà inviato dall’indirizzo e-mail dell’account di amministratore.Per poter selezionare le cartelle, fare clic sull'icona di “ripristino delle cartelle”: [recover fodlers](https://www.acronis.com/it-it/support/documentation/BackupService/37405.png)
6. Fare clic su **Ripristina.**
7. In Cassetta postale di destinazione, visualizzare, cambiare o specificare la casella di posta di destinazione.Per impostazione predefinita, viene selezionata la casella di posta originale. Se tale casella di posta non esiste, è necessario specificare la casella di posta di destinazione.
8. Fare clic su ***Avvia ripristino.***
9. Confermare la propria decisione.

Gli elementi delle caselle di posta vengono sempre ripristinati nella cartella Elementi ripristinati della casella di posta di destinazione.

#### Modifica le credenziali di accesso di Office 365 {#modifica-le-credenziali-di-accesso-di-office-365}

È possibile modificare le credenziali di accesso di Office 365 senza reinstallare l’agente.

1. Fare clic su ***Dispositivi > Microsoft Office 365***.
2. Fare clic su *Specifica credenziali*.
3. Immettere le credenziali di amministratore globale di Office 365 e quindi fare clic su OK.

:::info
L’agente eseguirà l’accesso a Office 365 utilizzando tale account. Per abilitare l’accesso dell’agente ai contenuti di tutte le caselle di posta, all’account verrà assegnato il ruolo di gestione **Application Impersonation** (Rappresentazione dell’applicazione).
:::

## Utilizzo dell’Agente cloud per Office 365 {#utilizzo-dell-agente-cloud-per-office-365}

### Aggiunta di un’organizzazione di Office 365 {#aggiunta-di-un-organizzazione-di-office-365-1}

1. Accedere alla console di backup come amministratore aziendale.
2. Fare clic su ***Dispositivi > Aggiungi > Microsoft Office 365 Business.***
3. Selezionare il data center Microsoft usato dall’organizzazione (il software reindirizza alla pagina di accesso di Microsoft Office 365).
4. Accedere a Office 365 con le credenziali di amministratore globale. → Microsoft Office 365 visualizza un elenco di autorizzazioni necessarie per eseguire il backup e il ripristino dei dati dell’organizzazione.
5. Confermare di accedere al servizio di backup tali autorizzazioni.

Gli elementi dati dell’organizzazione vengono visualizzati nella console di backup, nella pagina Microsoft Office 365.

#### Suggerimenti per l'utilizzo in ulteriori contesti {#suggerimenti-per-l-utilizzo-in-ulteriori-contesti}

- L’agente cloud esegue la sincronizzazione con Office 365 ogni 24 ore, a partire dal momento in cui l’organizzazione è aggiunta al servizio di backup. Se un utente, un gruppo o un sito vengono rimossi, la modifica è immediatamente visualizzata nella console di backup. Per forzare la sincronizzazione dell’agente cloud con Office 365, selezionare l’organizzazione nella pagina di Microsoft Office 365quindi fare clic su Aggiorna.
- Se è stato applicato un piano di backup al gruppo Tutti gli utenti, Tutti i gruppi o Tutti i siti, gli elementi appena aggiunti vengono inclusi nel backup solo dopo la sincronizzazione.
- In base ai criteri Microsoft, dopo che un utente, un gruppo o un sito sono stati rimossi dall’interfaccia utente di Office 365, esso resta disponibile per qualche giorno tramite l’API. In questo periodo l’elemento eliminato è inattivo (mostrato in grigio) nella console di backup e i backup dell’elemento non vengono eseguiti. Quando l’elemento rimosso non è più disponibile neanche tramite l’API, non sarà più visualizzato nella console di backup. I relativi backup (se presenti) sono reperibili in Backup > Backup di Microsoft Office 365.

### Protezione delle caselle di posta di Exchange Online {#protezione-delle-caselle-di-posta-di-exchange-online}

#### Di quali elementi è possibile eseguire il backup? {#di-quali-elementi-e-possibile-eseguire-il-backup-1}

È possibile eseguire il backup delle caselle di posta utente, di gruppo e condivise. Facoltativamente, è possibile scegliere di eseguire il backup delle caselle di posta di archiviazione (In-Place Archive) delle caselle di posta selezionate.

#### Quali elementi è possibile ripristinare? {#quali-elementi-e-possibile-ripristinare-1}

Dal backup di una casella postale è possibile ripristinare i seguenti elementi:

- Caselle postali
- Cartelle e-mail
- Messaggi e-mail
- Eventi di calendario
- Attività
- Contatti
- Voci del diario
- Note

È possibile utilizzare la ricerca per individuare gli elementi.

Durante il ripristino di caselle di posta e di elementi delle caselle di posta, è possibile selezionare se sovrascrivere o meno gli elementi nella posizione di destinazione.

#### Selezione delle caselle di posta {#selezione-delle-caselle-di-posta-1}

Selezionare le caselle di posta come descritto di seguito, quindi specificare eventuali altre impostazioni del piano di backup [in modo appropriato](https://www.acronis.com/it-it/support/documentation/BackupService/index.html#33579.html).

Per selezionare le caselle di posta di Exchange Online:

1. Fare clic su Microsoft Office 365.
2. Se al servizio di backup sono state aggiunte più organizzazioni di Office 365, selezionare l’organizzazione i cui dati utente devono essere sottoposti a backup. *Altrimenti, ignorare questo passaggio*.
3. Eseguire una delle seguenti operazioni:
-   Per eseguire il backup delle caselle di posta di tutti gli utenti e di tutte le caselle condivise (incluse quelli che verranno create in futuro), espandere il nodo Utenti, selezionare Tutti gli utenti e quindi fare clic su Raggruppa backup.
-   Per eseguire il backup di singole caselle di posta utente o di caselle condivise, espandere il nodo Utenti, selezionare Tutti gli utenti, selezionare gli utenti la cui casella di posta si desidera sottoporre a backup e quindi fare clic su Backup.
-   Per eseguire il backup delle caselle di posta di tutti i gruppi (incluse quelli dei gruppi che verranno creati in futuro), espandere il nodo Gruppi, selezionare Tutti i gruppi, quindi fare clic su Raggruppa backup.
-   Per eseguire il backup di singole caselle di posta di gruppo, espandere il nodo Gruppi, selezionare Tutti i gruppi, selezionare i gruppi le cui caselle di posta si desidera sottoporre a backup e quindi fare clic su Backup.
4. Nel pannello del piano di backup:
-   Verificare che l’elemento Caselle di posta sia selezionato in Elementi del backup.
-   Se non si desidera eseguire il backup delle caselle di posta di archiviazione, disattivare l’opzione Casella di posta di archiviazione

#### Ripristino di caselle postali {#ripristino-di-caselle-postali}

1. Fare clic su Microsoft Office 365.
2. Se al servizio di backup sono state aggiunte più organizzazioni di Office 365, selezionare l’organizzazione di cui ripristinare i dati oggetto di backup. *Altrimenti, ignorare questo passaggio*.
3. Eseguire una delle seguenti operazioni:
-   Per ripristinare una casella di posta utente, espandere il nodo Utenti, selezionare Tutti gli utenti, selezionare l’utente la cui casella di posta si desidera ripristinare e quindi fare clic su Ripristina.
-   Per ripristinare una casella di posta condivisa, espandere il nodo Utenti, selezionare Tutti gli utenti, selezionare la casella condivisa che si desidera ripristinare e quindi fare clic su Ripristina.
-   Per ripristinare una casella di posta di gruppo, espandere il nodo Gruppi, selezionare Tutti i gruppi, selezionare il gruppo la cui casella di posta si desidera ripristinare e quindi fare clic su Ripristina.
-   Se la casella di posta utente, di gruppo o condivisa è stata eliminata, selezionarla nella sezione Backup di Microsoft Office 365 della scheda [Backup](https://www.acronis.com/it-it/support/documentation/BackupService/index.html#35883.html), quindi fare clic su Mostra backup.È possibile cercare gli utenti e i gruppi per nome. I caratteri jolly non sono supportati.
4. Selezionare un punto di ripristino (per visualizzare solo i punti di ripristino che contengono caselle di posta, selezionare Caselle di posta in Filtra per contenuto).
5. Fare clic su ***Ripristina > Intera casella di posta***.
6. Se al servizio di backup sono aggiunte più organizzazioni di Office 365, fare clic su Organizzazione di Office 365 per visualizzare, modificare o specificare l’organizzazione di destinazione.Per impostazione predefinita, è selezionata l’organizzazione originale. Se tale organizzazione non risulta più registrata al servizio di backup, è necessario specificare l’organizzazione di destinazione.
7. In *Ripristina* nelle caselle di posta, visualizzare, cambiare o specificare la casella di posta di destinazione.Per impostazione predefinita, viene selezionata la casella di posta originale. Se questa casella di posta non esiste o se è stata selezionata un’organizzazione non originale, è necessario specificare la casella di posta di destinazione.
8. Fare clic su **Avvia ripristino**.
9. Selezionare una delle opzioni di sovrascrittura:
-   Sovrascrivi gli elementi esistenti
-   Non sovrascrivere gli elementi esistenti
10. Fare clic su ***Procedi*** per confermare la propria decisione.

#### Ripristino di elementi delle caselle postali {#ripristino-di-elementi-delle-caselle-postali-1}

1. Fare clic su Microsoft Office 365.
2. Se al servizio di backup sono state aggiunte più organizzazioni di Office 365, selezionare l’organizzazione di cui ripristinare i dati oggetto di backup. Altrimenti, ignorare questo passaggio.
3. Eseguire una delle seguenti operazioni:
-   Per ripristinare gli elementi da una casella di posta utente, espandere il nodo Utenti, selezionare Tutti gli utenti, selezionare l’utente la cui casella di posta conteneva in origine gli elementi da ripristinare e quindi fare clic su Ripristina.
-   Per ripristinare elementi da una casella di posta condivisa, espandere il nodo Utenti, selezionare Tutti gli utenti, selezionare la casella condivisa che originariamente conteneva gli elementi che si desidera ripristinare e quindi fare clic su Ripristina.
-   Per ripristinare gli elementi da una casella di posta di gruppo, espandere il nodo Gruppi, selezionare Tutti i gruppi, selezionare il gruppo la cui casella di posta conteneva in origine gli elementi da ripristinare e quindi fare clic su Ripristina.
-   Se la casella di posta utente, di gruppo o condivisa è stata eliminata, selezionarla nella sezione Backup di Microsoft Office 365 della scheda [Backup](https://www.acronis.com/it-it/support/documentation/BackupService/index.html#35883.html), quindi fare clic su Mostra backup.È possibile cercare gli utenti e i gruppi per nome. I caratteri jolly non sono supportati.
4. Selezionare un punto di ripristino (per visualizzare solo i punti di ripristino che contengono caselle di posta, selezionare Caselle di posta in Filtra per contenuto).
5. ***Fare clic su Ripristina > Messaggi e-mail.***
6. Esplorare la cartella richiesta o utilizzare la ricerca per ottenere l'elenco degli elementi richiesti.Sono disponibili le opzioni di ricerca seguenti: I caratteri jolly non sono supportati.
-   Per i messaggi e-mail: ricerca per oggetto, mittente, destinatario e data.
-   Per gli eventi: ricerca per titolo e data.
-   Per le attività: ricerca per titolo e data.
-   Per i contatti: ricerca per nome, indirizzo e-mail e numero di telefono.
7. Selezionare gli elementi che si desidera ripristinare. Per poter selezionare le cartelle, fare clic sull'icona di “ripristino delle cartelle”: [recover fodlers](https://www.acronis.com/it-it/support/documentation/BackupService/37405.png)
Inoltre, è possibile eseguire una delle seguenti operazioni:
-   Dopo aver selezionato un elemento, fare clic su Mostra contenuto per visualizzarne il contenuto, inclusi gli allegati. Fare clic sul nome di un file allegato per scaricarlo.
-   Quando è selezionato un messaggio e-mail o un elemento di calendario, fare clic su Invia come e-mail per inviare l’elemento all’indirizzo e-mail specificato. È possibile selezionare il mittente e scrivere un testo da aggiungere all’elemento inoltrato.
-   Solo se il backup non è crittografato, è stata usata la ricerca e selezionato un unico elemento nei risultati della ricerca, è possibile fare clic su Mostra versioni per selezionare la versione dell’elemento da ripristinare. È possibile selezionare qualsiasi versione di cui sia stato eseguito il backup, precedente o successiva al punto di ripristino selezionato.
8. Fare clic su ***Ripristina***.
9. Se al servizio di backup sono state aggiunte più organizzazioni di Office 365, fare clic su **Organizzazione di Office 365** per visualizzare, modificare o specificare l’organizzazione di destinazione.
10. Per impostazione predefinita, è selezionata l’organizzazione originale. Se tale organizzazione non risulta più registrata al servizio di backup, è necessario specificare l’organizzazione di destinazione.
11. In Ripristina nelle caselle di posta, visualizzare, cambiare o specificare la casella di posta di destinazione.Per impostazione predefinita, viene selezionata la casella di posta originale. Se questa casella di posta non esiste o se è stata selezionata un’organizzazione non originale, è necessario specificare la casella di posta di destinazione.
12. \[Solo quando si ripristinano gli elementi in una casella di posta utente o condivisa\] In Percorso visualizzare o modificare la cartella di destinazione nella casella di posta di destinazione. Per impostazione predefinita, la cartella Elementi ripristinati è selezionata.Gli elementi delle caselle di posta di gruppo vengono sempre ripristinati nella cartella Posta in arrivo.
13. Fare clic su ***Avvia ripristino***.
14. Selezionare una delle opzioni di sovrascrittura:
-   Sovrascrivi gli elementi esistenti
-   Non sovrascrivere gli elementi esistenti
15. Fare clic su ***Procedi*** per confermare la propria decisione.

:::note
Documentazione originale disponibile su: [https://www.acronis.com/it-it/support/documentation/BackupService/index.html#37287.html](https://www.acronis.com/it-it/support/documentation/BackupService/index.html#37287.html)
:::