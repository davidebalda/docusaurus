---
title: "Utenti Teams - Talky Time Direct Routing"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina definisce i passaggi da seguire per collegare gli Utenti Microsoft Teams a Numerazioni geografiche o agli interni PBX, configurati nella sezione **Provider**.

## Accedi alla sezione Utenti Teams {#accedi-alla-sezione-utenti-teams}

Per accedere al sezione Utenti Microsoft Teams puoi seguire i seguenti passaggi:

1. Accedi al servizio **Talky Time Direct Routing** dalle voci di menù laterale, sotto la categoria **Unified Communication**. Segui la nostra [**guida**](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/1966249437/Gestione+del+servizio+-+Talky+Time#Accedi-al-servizio-Talky-Time)**.**
2. Seleziona la voce **Utenti Teams** dalle tab di navigazione in alto.

![Screenshot 2024-04-26 at 14.47.18.png](/kb-assets/be1996a3aa-screenshot-2024-04-26-at-14-47-18.png)

### Collega Utenti Microsoft Teams {#collega-utenti-microsoft-teams}

:::warning
Solamente nel caso in cui stessi procedendo alla migrazione alla nuova versione di Talky Time con le funzionalità Multi-Region descritti in questa [**guida**](https://cloudfireit.atlassian.net/l/cp/Rn0mogJr), e riscontrassi alcuni utenti non sincronizzati, **NON premere il bottone sincronizza utenti** alla sinistra dello stato di sincronizzazione. Collega manualmente gli utenti seguendo i passaggi di seguito.
:::

Per collegare gli utenti Teams è sufficiente seguire questi passaggi:

1. Premi su **Collega utente**

:::info
In relazione alla **Tipologia di Provider** creata nella sezione precedente e scelta in questa il processo di Configurazione e collegamento di ciascuno di essi con la suite di Microsoft Teams® sarà differente. Non sarà necessario selezionare la tipologia di Provider poiché viene proposto automaticamente il processo di configurazione adatto allo scenario in cui ci si trova. Rivedi la [**guida**](../provider-talky-time/index.md) relativa alla configurazione dei Provider.

[!TIP]
Qualora volessi importare più numerazioni o interni PBX puoi seguire questa [**guida**](import-massivo-utenti-teams-talky-time.md).
:::

#### Configurazione PBX {#configurazione-pbx}

I seguenti passaggi mostrano la configurazione nel caso in cui nelle precedenti sezioni si sia creato un Provider PBX, si fa riferimento quindi a Generic PBX - Asterisk - 3cx - Wildix - Avaya - Trixbox - FreeSwitch - FreePBX - Kalliope.

1. Compila i dati utilizzando i prerequisiti richiesti. Quali:
1.   **Utente Microsoft Teams**: Nella lista sono presenti tutti gli utenti del Dominio Microsoft Teams collegato al servizio che dispongono delle licenze necessarie all’utilizzo di Talky Time.
2.   **Provider**: indica il provider al quale appartiene l’interno PBX che vuoi collegare all’utente Microsoft Teams
3.   **FQDN**: Viene già precompilato in base alle informazioni inserite precedentemente nella sezione provider
4.   **Interno PBX**: interno che si vuole associare all’utente Microsoft Teams
5.   **Username**: Username di registrazione dell’Interno del PBX che vuoi collegare
6.   **Password**: Password di registrazione dell’interno del PBX che vuoi collegare
2. Premi su **Collega utente**

:::warning
La corretta propagazione delle configurazioni potrebbe richiedere fino a 60 minuti. In caso di problemi ad effettuare e ricevere chiamate ti consigliamo di riprovare più tardi.
:::

Durante il collegamento verrà mostrato lo stato dell’Utente Microsoft Teams **In collegamento**. Una volta terminato sarà **Collegato.**

#### Configurazione SIP Trunk {#configurazione-sip-trunk}

I seguenti passaggi mostrano la configurazione nel caso in cui nelle precedenti sezioni si sia creato un Provider PSTN con SIP Trunk.

1. Compila i dati utilizzando i prerequisiti richiesti. Quali:
1.   **Utente Microsoft Teams**: Nella lista sono presenti tutti gli utenti del Dominio Microsoft Teams collegato al servizio che dispongono delle licenze necessarie all’utilizzo di Talky Time.
2.   **Provider**: indica il provider al quale appartiene l’interno PBX che vuoi collegare all’utente Microsoft Teams
3.   **Nazione:** seleziona dall’elenco la nazione di appartenenza della Numerazione
4.   **Prefisso Provider**: inserisci il prefisso del Provider di appartenenza della Numerazione (in caso di problemi contatta l’assistenza del Provider per richiedere il prefisso corretto)
5.   **Numerazione Principale**: inserisci la Numerazione principale comprensiva di prefisso nazionale (ES: 02123456)
2. Premi su **Collega utente**

:::warning
La corretta propagazione delle configurazioni potrebbe richiedere fino a 60 minuti. In caso di problemi ad effettuare e ricevere chiamate ti consigliamo di riprovare più tardi.
:::

Durante il collegamento verrà mostrato lo stato dell’Utente Microsoft Teams **In collegamento**. Una volta terminato sarà **Collegato.**

#### Configurazione SIP Extension {#configurazione-sip-extension}

I seguenti passaggi mostrano la configurazione nel caso in cui nelle precedenti sezioni si sia creato un Provider PSTN con SIP Extension.

1. Compila i dati utilizzando i prerequisiti richiesti. Quali:
1.   **Utente Microsoft Teams**: Nella lista sono presenti tutti gli utenti del Dominio Microsoft Teams collegato al servizio che dispongono delle licenze necessarie all’utilizzo di Talky Time.
2.   **Provider**: indica il provider al quale appartiene il SIP Extension che vuoi collegare all’utente Microsoft Teams
3.   **Nazione:** seleziona dall’elenco la nazione di appartenenza della Numerazione
4.   **Prefisso Provider**: inserisci il prefisso del Provider di appartenenza della Numerazione (in caso di problemi contatta l’assistenza del Provider per richiedere il prefisso corretto)
5.   **Numerazione Principale**: inserisci la Numerazione principale comprensiva di prefisso nazionale (ES: 02123456)
6.   **Interno PBX**: interno che si vuole associare all’utente Microsoft Teams
7.   **Username**: Username di registrazione dell’Interno del PBX che vuoi collegare
8.   **Password**: Password di registrazione dell’interno del PBX che vuoi collegare
2. Premi su **Collega utente**

:::warning
La corretta propagazione delle configurazioni potrebbe richiedere fino a 60 minuti. In caso di problemi ad effettuare e ricevere chiamate ti consigliamo di riprovare più tardi.
:::

Durante il collegamento verrà mostrato lo stato dell’Utente Microsoft Teams **In collegamento**. Una volta terminato sarà **Collegato.**

#### Configurazione SIP Account {#configurazione-sip-account}

I seguenti passaggi mostrano la configurazione nel caso in cui nelle precedenti sezioni si sia creato un Provider SIP account ovvero seleziona questa tipologia se hai già attivato un Account SIP nella sezione “linee Voip” e vuoi collegarlo a Microsoft Teams.

1. Compila i dati utilizzando i prerequisiti richiesti. Quali:
-   **Utente Microsoft Teams**: Nella lista sono presenti tutti gli utenti del Dominio Microsoft Teams collegato al servizio che dispongono delle licenze necessarie all’utilizzo di Talky Time.
-   **Provider**: indica il provider da collegare all’utente Microsoft Teams
-   **Numerazione**: seleziona la numerazione da collegare all’Utente Microsoft Teams.
2. Premi su **Collega utente.**

:::warning
La corretta propagazione delle configurazioni potrebbe richiedere fino a 60 minuti. In caso di problemi ad effettuare e ricevere chiamate ti consigliamo di riprovare più tardi.
:::

Durante il collegamento verrà mostrato lo stato dell’Utente Microsoft Teams **In collegamento**. Una volta terminato sarà **Collegato.**

### Dettaglio Utenti Microsoft Teams {#dettaglio-utenti-microsoft-teams}

Per visionare e modificare il dettaglio di ciascun utente Microsoft Teams accedi al progetto, premi su Direct Routing nel menù a sinistra, e seleziona **Utenti Teams** nella tab in alto.

Premendo sul nome dell’Utente Microsoft Teams è possibile visionare il dettaglio dell’utente, lo stato e modificarlo.

![](/kb-assets/f8fe64c758-image-20220221-115404.png)

Per scollegare l’utente Microsoft Teams è necessario cliccare sull’azione **Scollega utente** in alto a sinistra.

Nella sezione **Personalizza Caller ID** inoltre, premendo su **Modifica** puoi modificare ed aggiungere il numero telefonico presentato in uscita dal chiamante. In assenza di personalizzazione viene presentata la numerazione principale.

Ricerca e seleziona la numerazione che intendi presentare in uscita tra quelle disponibili, sempre in relazione alla tipologia di provider scelto.