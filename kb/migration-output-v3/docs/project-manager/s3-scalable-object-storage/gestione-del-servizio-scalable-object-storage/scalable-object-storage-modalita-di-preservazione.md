---
title: "Scalable Object Storage - Modalità di preservazione"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina illustra il dettaglio delle caratteristiche del Scalable Object Storage tra cui la modalità di preservazione, il periodo di preservazione e la gestione delle versioni da definire al momento della creazione di ciascun bucket.

# Modalità di preservazione dei dati

La preservazione dei dati all’interno di Scalable Object Storage è la capacità di impedire che gli oggetti contenuti nei buckets vengano eliminati o sovrascritti per un periodo di tempo predeterminato (**Immutabilità del dato**).

Questa è gestita con differenti modalità di preservazione dei dati, ciascuna delle quali corrisponde a una diversa applicazione di livelli di protezione agli oggetti contenuti del bucket. Le modalità di preservazione possono aiutare a impedire che gli oggetti vengano eliminati o sovrascritti da specifici utenti per un periodo di tempo predeterminato (periodo di preservazione), essere utilizzate per soddisfare i requisiti normativi o aggiungere un ulteriore livello di protezione contro le modifiche e l'eliminazione degli oggetti.

:::warning
Una volta confermata la creazione del Bucket, la modalità di preservazione dei dati non potrà più essere modificata.
:::

# Periodo di preservazione

Il **periodo di Preservazione** (o **Retention)** è **tempo effettivo per il quale una versione dell’oggetto risulta protetta.** Questo può essere compreso tra 1 e 365 giorni.

Quando imposti un periodo di preservazione su una versione dell'oggetto, nei metadati vengono archiviate data e ora esatte (in formato timestamp) per indicare quando scade il periodo di preservazione. Una volta scaduto il periodo di preservazione, la versione dell'oggetto non risulterà più protetta e potrà essere sovrascritta/eliminata.

La modifica del periodo di preservazione dipende dalla modalità di preservazione dei dati selezionata.

# Gestione delle versioni

La gestione delle versioni è l’impostazione che permette di mantenere **più varianti** dello stesso oggetto all’interno del bucket.

L’abilitazione di questa funzionalità permette di ripristinare più facilmente i file in caso di errori nelle applicazioni o azioni non intenzionali da parte degli utenti.

:::warning
Questa impostazione è gestibile solo nel caso in cui la modalità di preservazione dei dati sia **nessuna***.* In tutte le altre modalità è abilitata di default.
:::

# Modalità di preservazione dei dati e gestione delle versioni disponibili

Queste sono le modalità attualmente supportate:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Modalità di preservazione** | **Descrizione** | **Gestione delle versioni** | **Limitazioni** | **Use Cases** |
| **Nessuna** | Non viene applicata alcuna modalità di preservazione ai dati presenti all’interno del bucket. | [(error)](https://cloudfireit.atlassian.net/wiki/s/570850602/6452/7763732b289e22362b5a69ba99fd0fffc9daf817/_/images/icons/emoticons/error.png)<br><br> Disabilitata | Qualunque utente disponga delle credenziali di accesso al bucket, e dei permessi di lettura e scrittura sullo stesso, può sovrascrivere o eliminare i dati in qualunque momento. | Non è richiesta alcuna immutabilità dei dati contenuti all’interno del bucket. |
| **Compliance** | In questa modalità una versione dell'oggetto protetto non può essere sovrascritta o eliminata da alcun utente, incluso l'utente proprietario del Bucket. Quando un oggetto è bloccato in modalità Compliance, la relativa modalità di preservazione dei dati non può essere modificata e il relativo periodo di preservazione non può essere abbreviato. La modalità Compliance aiuta a garantire che una versione dell'oggetto non possa essere sovrascritta o eliminata per la durata del periodo di preservazione. | [(tick)](https://cloudfireit.atlassian.net/wiki/s/570850602/6452/7763732b289e22362b5a69ba99fd0fffc9daf817/_/images/icons/emoticons/check.png)<br><br> Abilitata | Per poter sovrascrivere o eliminare oggetti contenuti nel bucket è necessario attendere la fine del periodo di preservazione e una volta concluso modificare lo stesso, prolungando l’immutabilità, o modificare la modalità di preservazione del bucket stesso. | É richiesto un un bucket immutabile per un determinato periodo di tempo, nel quale **nessuno** può sovrascrivere od eliminare gli oggetti. |
| **Governance** | In questa modalità gli utenti non possono sovrascrivere/eliminare una versione dell'oggetto o modificarne le impostazioni di blocco a meno che non dispongano di autorizzazioni speciali. Con la modalità Governance, proteggi gli oggetti dall'eliminazione da parte della maggior parte degli utenti, ma puoi comunque concedere ad alcuni utenti l'autorizzazione per modificare le impostazioni di conservazione o eliminare l'oggetto se necessario*.* È possibile utilizzare la modalità Governance per testare le impostazioni del periodo di conservazione prima di creare un periodo di conservazione in modalità Compliance. | [(tick)](https://cloudfireit.atlassian.net/wiki/s/570850602/6452/7763732b289e22362b5a69ba99fd0fffc9daf817/_/images/icons/emoticons/check.png)<br><br> Abilitata | Non corrisponde pienamente al concetto di Immutability in quanto un utente, con accesso API particolare, può modificarne la sola data di scadenza e di conseguenza, modificarne l’integrità del dato. | É richiesto un un bucket immutabile per un determinato periodo di tempo, ma **alcuni utenti specifici** devono poter sovrascrivere o eliminare gli oggetti. |
| **Veeam Immutable Storage** | In questa modalità una versione dell'oggetto protetto non può essere sovrascritta o eliminata da alcun utente, incluso l'utente proprietario, rendendo inoltre il Bucket compatibile con i requisiti di Veeam Immutable Storage.<br><br>*Il periodo di preservazione non può essere modificato in quanto gestito direttamente da Veeam.* | [(tick)](https://cloudfireit.atlassian.net/wiki/s/570850602/6452/7763732b289e22362b5a69ba99fd0fffc9daf817/_/images/icons/emoticons/check.png)<br><br> Abilitata | > [!WARNING]<br>> Il periodo di preservazione è gestito direttamente da Veeam e viene applicato a livello di singolo oggetto, e non per l’intero bucket. | Modalità adatta solamente per chi necessità di un bucket immutabile per dati provenienti dal Software Veeam. |