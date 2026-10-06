## Introduzione

In questo sotto menù vi sarà possibili gestire l'instradamento delle chiamate in base al numero che vi sta chiamando. In poche parole, il CloudPBX, effettua un check della numerazione che vi sta chiamando, se in questo sotto-menù vi sono presenti delle regole che si riferiscono a questa numerazione, la chiamata verrà instradata secondo quanto specificato nella regola.

## Prerequisiti

Questo sotto-menù è disponibile di default una volta attivo il servizio CloudPBX.

## Guida passo-passo

### Accesso

Dal **Portale Tenant** entrare nella sezione Cid Routing tramite il menù **Call Routing → CID Routing.**

![](./attachments/image2019-9-2_13-58-53.png)

### Creazione

Cliccate sul pulsante **Add CID**.

### Descrizione dei Campi

![](./attachments/image2019-9-2_14-1-26.png)

- **Caller Number:** numerazione telefonica da cui proviene la chiamata.
- **DID Number:** numerazione telefonica a cui è destinata la chiamata, selezioni possibili:
-   Se cliccate sulla tex-box vi verrà mostrato un elenco dei DID presenti nel vostro CloudPBX
-   Se flaggate la check-box vicino ad **ANY** selezionerete tutti i DID presenti nel vostro Cloud PBX
- **Default Destination:** tipo di **Service** verso sui instradare la chiamata.
- **Default Extension:** identificativo del **Service** selezionato al punto precedente.
- **Description:** descrizione della regola a votra discrezione.

### Funzionamento

Il funzionamento è molto semplice, all'arrivo di una chiamata, il CloudPBX, effettuerà un check del numero chiamante (**Caller Number**) e del numero chiamato (**DID**), se è presente una regola che rispetta questo check allora, la chiamata, verrà instradata verso il tipo di Service (**Default Destination**), specificato nella **Default Extension.**

> [!INFO]
> **ESEMPIO:**
> Prendendo per esempio l'immagine al punto 3:
> Tutte le chiamate provenienti dal numero **3341234567** e destinate al numero **9938480360** verranno tutte instradate verso l'**Extension 101**

  

  

> [!NOTE]
> **Sommario**
> 
> 
> 
> - [Introduzione](#introduzione)
> - [Prerequisiti](#prerequisiti)
> - [Guida passo-passo](#guida-passo-passo)
> -   [Accesso](#accesso)
> -   [Creazione](#creazione)
> -   [Descrizione dei Campi](#descrizione-dei-campi)
> -   [Funzionamento](#funzionamento)
> * * *
> **Articoli collegati**
> 
> 
> - Page:
> [Impossibile chiamare o ricevere chiamate](/wiki/spaces/KB/pages/1966256951/Impossibile+chiamare+o+ricevere+chiamate)
> - Page:
> [Portale Extension - Opzioni e Funzionalità](/wiki/spaces/KB/pages/1966256717/Portale+Extension+-+Opzioni+e+Funzionalit)
> - Page:
> [Portale Extension - Extension Settings](/wiki/spaces/KB/pages/1966256663/Portale+Extension+-+Extension+Settings)
> - Page:
> [Deviazioni di chiamata](/wiki/spaces/KB/pages/1966255812/Deviazioni+di+chiamata)
> - Page:
> [BLF Call-pickup](/wiki/spaces/KB/pages/1966255734/BLF+Call-pickup)