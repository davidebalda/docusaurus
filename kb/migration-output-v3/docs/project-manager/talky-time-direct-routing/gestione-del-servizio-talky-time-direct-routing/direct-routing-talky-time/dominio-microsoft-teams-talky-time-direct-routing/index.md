---
title: "Dominio Microsoft Teams - Talky Time Direct Routing"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina definisce i passaggi da seguire per procedere alla configurazione del Dominio di Teams all’interno della piattaforma CloudFire, necessario per l’integrazione di Talky Time Direct Routing.

## Requisiti

Per una configurazione corretta e senza interruzioni è necessario avere i seguenti requisiti. Prima di procedere controlla di avere:

- Credenziali Microsoft di un utente con privilegi sia di **Global Administrator** che di **Teams Administrator** da utilizzare per la configurazione.

![](/kb-assets/c6d91dbec3-microsoftteams-image-1.png)

- Una o più licenze per ogni utente Talky Time Direct Routing da attivare, come da tabella riepilogativa:

|     |     |
| --- | --- |
| **Licenza (per utente)** | **Add-on per Call e Conference** |
| - Office 365 E1<br>- Office 365 E3 | - Phone System and Conference license<br>- Teams Phone Standard |
| Microsoft 365 E5 | *nessuno* |
| - Microsoft 365 Business Basic<br>- Microsoft 365 Business Standard<br>- Microsoft 365 Business Premium | - Microsoft 365 Business Voice (without calling Plan): **dal 1°marzo 2022 l’addon sarà deprecato e non più attivabile. Chi già possiede tale licenza potrà utilizzarla fino a scadenza del contratto.**<br>- **Teams Phone Standard**<br><br>> [!WARNING]<br>> Attenzione: per l’utilizzo di Talky Time Direct Routing **NON è necessario** il Teams Phone with Calling Plan, bensì il **Teams Phone Standard**. |

- Una licenza ulteriore come da quelle descritte in tabella da assegnare all’utente di servizio.

# Sincronizza Dominio Microsoft Teams

Per sincronizzare un Dominio Microsoft Teams puoi seguire i seguenti passaggi:

1. Accedi al servizio **Talky Time Direct Routing** dalle voci di menù laterale, sotto la categoria **Unified Communication**. Segui la nostra [**guida**](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/1966249437/Gestione+del+servizio+-+Talky+Time#Accedi-al-servizio-Talky-Time)**.**
2. Seleziona la voce **Dominio Teams** dalle voci delle tab in alto;
3. Premi il bottone **Sincronizza Dominio** posto al centro della pagina.

:::info
Se hai già sincronizzato un Dominio nella Region che stai visualizzando dovrai effettuare lo switch su una Region senza Dominio configurato.
:::

![Screenshot 2024-04-26 at 14.32.55.png](/kb-assets/255607b124-screenshot-2024-04-26-at-14-32-55.png)

## Seleziona la Region

Seleziona la Region dove sincronizzare il Dominio Microsoft Teams. Questa sarà la regione geografica nella quale saranno archiviati tutti i dati relativi alla configurazione del Dominio, dei Provider e degli Utenti Teams.

![](/kb-assets/02c6920458-image-20230804-074432.png)

:::note
Qualora non avessi specifiche esigenze di ridondanza ti consigliamo di selezionare la **Region geograficamente più vicina a te**. Ciò potrebbe aiutarti a mantenere le latenze più basse nelle chiamate.
:::

## Inserisci il Dominio Microsoft Teams

:::note
Se già utilizzi **Azure AD** per gestire gli utenti della tua organizzazione Microsoft puoi automatizzare la sincronizzazione del dominio con gli utenti Talky Time Direct Routing e risparmiare tempo negli step successivi dell’attivazione di Talky Time Direct Routing selezionando il campo Imposta gli utenti AzureAD.
:::

Inserisci i seguenti dati del Dominio Microsoft Teams:

1. Inserisci il dominio che intendi sincronizzare nel campo **Dominio Microsoft Teams**. Utilizza il dominio contenente gli Utenti Teams che vuoi utilizzare nel servizio;
2. Seleziona nel campo **Nazione** la nazione utilizzata per la registrazione del dominio;
3. Seleziona o no il flag **Importa gli utenti AzureAD**
4. Premi su **Avvia sincronizzazione**.![](/kb-assets/9151080d6a-image-20230804-074549.png)

1. Successivamente si aprirà una **pagina pop-up**, come quella che trovi qui di seguito.  
Come richiesto dalla pagina, inserisci le credenziali di un utente con privilegi di Amministratore per il dominio che vuoi configurare.

:::info
Tale richiesta è necessaria per creare un utente di servizio necessario a procedere nelle fasi successive. Dalle operazione seguenti alla verifica del dominio sarà possibile modificare la password dell'utente con privilegi di amministratore o rimuovere del tutto tale utente poiché non verrà più utilizzato.
:::

![](/kb-assets/ddf1ed4ed9-screenshot-2022-01-07-at-17-27-12.png)

La schermata successiva mostra mostrata la lista dei permessi che verranno rilasciati dalla piattaforma Talky Time Direct Routing, il cui nome sarà sempre nella seguente forma: ***cf\_automation\_svc@`<random\_id>`.<dominio.esteso>***  
Tale utenza verrà utilizzata per tutte le successive configurazioni.

1. Premi su

**accetta** per proseguire l’integrazione.

![](/kb-assets/d0a1767c4a-screenshot-2022-01-07-at-17-27-29.png)

:::info
Durante il processo puoi controllare lo **stato di avanzamento della sincronizzazione**.  
Il processo di sincronizzazione è automatizzato e non ha bisogno di ulteriori azioni. É composto da da due step che corrispondono al controllo dei requisiti già definiti [qui](index.md#Requisiti).  
L’intera procedura può a impiegare fino a circa **15 min**, mentre avrà una durata fino ai 30 minuti per domini con un numero elevato di utenti (>50). Se trascorso questo tempo il servizio non risulta ancora in stato **Attivo** ti invitiamo ad aprire un [**Case**](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/1966244909) al nostro supporto.
:::

![](/kb-assets/c5fa3d15f7-image-20230320-120243.png)

:::note
Trovi il processo di sincronizzazione dettagliato in questa [pagina](dettaglio-sincronizzazione-dominio-talky-time-direct-routing.md).

[!CAUTION]
Qualora non rispettassi i requisiti richiesti, il processo di sincronizzazione viene automaticamente **interrotto** e vengono segnalati i requisiti non rispettati su cui puoi operare per la corretta sincronizzazione del Dominio.

[!TIP]
Per procedere nuovamente alla **sincronizzazione** dovrai premere sul bottone **elimina** in alto a destra della card e riiniziare la sincronizzazione.
:::

### Sincronizzazione Manuale

Se ti occorre un aggiornamento rapido tra la configurazione del **tenant Microsoft** ed il **servizio** ed il **numero di utenti** che puoi collegare, puoi avviare manualmente il processo di sincronizzazione del Dominio Microsoft Teams®.

Per avviare una **nuova sincronizzazione sul Dominio Microsoft Teams**® è sufficiente seguire questi passaggi:

1. Premi il bottone **Sincronizza dominio** in alto a destra nella sezione Dominio Microsoft Teams.
2. Visualizzerai nuovamente la pagina con lo stato **Sincronizzazione** ben visibile nella sezione Dominio Microsoft Teams.
3. Quando la sincronizzazione verrà completata con successo visualizzerai lo stato **Sincronizzato**.

:::info
La sincronizzazione del Dominio può impiegare fino a **30 minuti** per essere completata. Se trascorso questo tempo il Dominio non risulta ancora sincronizzato ti invitiamo ad aprire un [**Case**](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/1966244909) al nostro supporto.
:::

![](/kb-assets/16e315fdcc-image-20230320-134550.png)

Una volta sincronizzato il dominio Teams avrai accesso alla Dashboard di puoi procedere con la configurazione del **Provider SIP**.

Per avviare una nuova sincronizzazione degli utenti è sufficiente seguire i seguenti passaggi:

1. Premi il bottone **Sincronizza utenti** in alto a destra nella sezione Dominio Microsoft Teams.
2. Visualizzerai nuovamente la pagina Utenti Teams con lo stato **Sincronizzazione** ben visibile in alto a destra nella sezione Dominio Microsoft Teams.
3. Quando la sincronizzazione verrà completata con successo visualizzerai lo stato **Sincronizzato**.

:::info
La sincronizzazione del Dominio può impiegare fino a **30 minuti** per essere completata. Se trascorso questo tempo gli utenti non risultano ancora sincronizzato ti invitiamo ad aprire un [**Case**](#) al nostro supporto.
:::

![](/kb-assets/183acdada9-image-20230321-143216.png)

:::tip
Una volta sincronizzato il Dominio Microsoft Teams puoi procedere alla configurazione di un [**Provider**](../provider-talky-time/index.md).
:::

## Scollega ed elimina il Dominio Microsoft Teams

Per scollegare ed eliminare il Dominio Teams è sufficiente seguire questi passaggi:

1. Premi sul bottone **Elimina** in alto a destra nella sezione Dominio Microsoft Teams.
2. Si apre una finestra di dialogo che richiede la conferma dell’eliminazione del dominio.
3. Premi su **Elimina**.
4. Visualizzerai nuovamente la pagina Utenti Teams senza più i dati del Dominio compilati.

:::warning
L’operazione non può essere annullata una volta confermata. La sincronizzazione del dominio viene interrotta e ciò non consente di configurare alcun Provider.

[!WARNING]
Puoi scollegare il Dominio solo se non è presente alcun Account collegato.
Lo scollegamento del Dominio **interrompe la sincronizzazione** e disabilita le successive sezioni di configurazione.
:::

![](/kb-assets/bef5d6b404-image-20230320-135057.png)