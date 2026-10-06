---
title: "Audit Log"
---

Questa pagina spiega come visualizzare e navigare nella sezione **Audit Log** del tuo Account Cortex.

Con **Audit Logging** si intende il processo di documentazione delle attività all’interno di un sistema software quale Cortex. Esaminando gli audit log presenti in Cortex, gli amministratori di sistema possono tenere traccia dell'attività degli utenti ed indagare sulle violazioni e garantire la conformità ai requisiti normativi.

:::info
Ogni **utente con accesso al portale Account Manager** è in grado di navigare nella pagina e visualizzare gli audit log presenti. Scopri di più su [**Ruoli e Permessi**](utenti/ruoli-dettaglio-dei-permessi.md)**.**

[!NOTE]
In Cortex sono disponibili gli Audit Log dal giorno **1 novembre 2023**.
:::

# Accedi alla pagina Audit Log

Per accedere alla pagina Audit Log puoi seguire i seguenti passaggi:

1. Effettua il **login** su Cortex, verrai indirizzato su **Account Manager**;
2. Seleziona la voce **Audit Log** dal menu di navigazione laterale.

## Attività registrate

All’interno della sezione audit Log vengono registrate e mostrate le seguenti attività:

- **Utente**: identifica l'utente che ha effettuato l’attività. Leggi di più su [**utenti**](utenti/index.md) e [**permessi**](utenti/ruoli-dettaglio-dei-permessi.md);
- **Tipologia di evento**: l’evento registrato dal sistema Cortex. Nella sezione successiva sono elencate le tipologie di evento registrate;
- **Oggetto**: descrive il servizio che ha interessato l’evento stesso, e nel caso del servizio Public Cloud il dettaglio dell’istanza. L’oggetto non è sempre presente, per alcuni eventi infatti non c'è alcun dettaglio;
- **Account**: identifica l’account che ha interessato l’evento;
- **Data Ora:** identifica la data e l’orario in cui è avvenuto l’evento.

### Tipologia di Evento

Gli eventi che vengono registrati all’interno della sezione audit log sono:

|     |     |
| --- | --- |
| **Tipologia Evento** | **Descrizione** |
| Create | L’utente ha effettuato un’operazione di **creazione** che può riguardare: un servizio, una funzionalità o risorsa interna ad un servizio, un progetto, un utente, una region. Se relativa ad un servizio, verrà mostrato il dettaglio stesso dell’attività. |
| Update | L’utente ha effettuato un’operazione di **modifica** che può riguardare: un servizio, una funzionalità o risorsa interna ad un servizio, un progetto, un utente, una region. Se relativa ad un servizio, verrà mostrato il dettaglio stesso dell’attività. |
| Delete | L’utente ha effettuato un’operazione di **eliminazione** che può riguardare: un servizio, una funzionalità o risorsa interna ad un servizio, un progetto, un utente, una region. Se relativa ad un servizio, verrà mostrato il dettaglio stesso dell’attività. |
| Activate | L’utente ha effettuato un’operazione di **attivazione** che può riguardare: un servizio, una funzionalità o risorsa interna ad un servizio, un progetto, un utente, una region. Se relativa ad un servizio, verrà mostrato il dettaglio stesso dell’attività. |
| Deactivate | L’utente ha effettuato un’operazione di **disattivazione** che può riguardare: un servizio, una funzionalità o risorsa interna ad un servizio, un progetto, un utente, una region. Se relativa ad un servizio, verrà mostrato il dettaglio stesso dell’attività. |
| Login | L’utente ha effettuato un’operazione di **accesso** con il proprio utente all’interno dell’Account Cortex della propria organizzazione. |
| Login-As | L’utente ha effettuato un’operazione di **accesso** con il proprio utente all’interno dell’Account Cortex dell’*organizzazione del proprio cliente gestito*. Scopri le differenze tra [**cliente autonomo**](../partner-portal/clienti.md#Cliente-Autonomo) e [**gestito**](../partner-portal/clienti.md#Cliente-Gestito). |

## Filtri disponibili in pagina

Puoi filtrare e visualizzare gli audit log in pagina utilizzando i filtri:

- Evento: selezionando l’evento o gli eventi di interesse;
- Oggetto: selezionando l’oggetto o gli oggetti di interesse;
- Progetto: selezionando tra i progetti disponibili;
- Arco temporale: selezionando la data di inizio e la data di fine degli eventi di interesse.

## Dettaglio Evento

Puoi visualizzare il dettaglio di ciascun evento premendo sulla **label dell’evento** interessato.

Si aprirà il suo dettaglio compreso di:

- Utente
- Email Utente
- Account Utente
- Evento
- Oggetto
- Account
- Progetto
- Indirizzo IP - *Il* *dettaglio Indirizzo IP è disponibile solo nell’evento login*
- Tipologia Accesso - *Il* *dettaglio Tipologia di Accesso può riguarda l’accesso da portale Web o utilizzo di API di Terze Parti.*
- Descrizione dell’evento

Se si tratta di un evento di Update verranno mostrate due tab di dettaglio:

- Dati: comprende tutti i dati riportati nell’elenco qui sopra;
- Dettaglio: mostra il dettaglio dell’update prima e dopo l’aggiornamento.

## Download Audit Log

Puoi esportare il report audit log seguendo i seguenti passaggi:

1. Premi il bottone **Esporta** in alto a destra nella pagina;
2. Verrà generato il file CSV sulla base dei filtri applicati in pagina;
3. Una volta preparato il file CSV sarai avvisato con una notifica in alto a destra.
4. Dalla notifica potrai quindi effettuare il download.