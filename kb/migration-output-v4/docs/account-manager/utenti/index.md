---
title: "Utenti"
---

Questa pagina spiega come visualizzare e gestire gli Utenti su Cortex.

- **Gestire** molteplici **Utenti** ti permette di definire accessi personalizzati per i singoli membri del Team;
- **Assegnare** i corretti **Ruoli** ti permette di limitare i privilegi degli Utenti ed impedire l’accesso ad alcune risorse o aree di Cortex.

# Accedi alla pagina Utenti

Per accedere alla pagina Utenti puoi seguire i seguenti passaggi:

1. Effettua il **login** su Cortex, verrai indirizzato su **Account Manager**
2. Seleziona la voce **Utenti** dal menu di navigazione laterale

Nella pagina è riportato l’elenco degli Utenti inseriti, comprensivi di nome e cognome, ruolo, email e stato.

:::info
I link di navigazione a [**Project Manager**](../../project-manager/index.md) ed [**Partner Portal**](../../partner-portal/index.md) (solo se hai un Account Partner) sono sempre visibili in alto a destra nella pagina.
:::

## Stati degli Utenti

Un Utente può assumere i seguenti stati:

- **Attivo** → L’utente è correttamente attivo e può operare normalmente, sulla base dei permessi concessi dal proprio ruolo;
- **Disattivo** → L’utente è impossibilitato ad effettuare il login su Cortex.

## Ruoli degli Utenti

Un Utente può assumere i seguenti ruoli:

- **Admin** → Accesso completo a tutte le funzionalità.
- **Tecnico** → Accesso a tutte le funzionalità di gestione di Account e Fatture. Non ha accesso a Clienti, Utenti e Progetti. Non può gestire Prezzi e Servizi.
- **Vendite** → Accesso a tutte le funzionalità di gestione di Clienti, Progetti e Servizi. Non ha accesso a Prezzi e Fatture. Non può gestire Account, Utenti e Listini.
- **Contabilità** → Accesso a tutte le funzionalità di gestione di Clienti, Prezzi e Fatture. Non può gestire Account, Utenti, Progetti e Servizi.
- **Read Only** → Visibilità completa di tutto il portale ma nessuna possibilità di operare sulle funzionalità.

:::info
Un elenco dettagliato di tutti i permessi concessi da ciascun Ruolo è disponibile alla pagina [Ruoli - Dettaglio dei permessi](ruoli-dettaglio-dei-permessi.md).
:::

# Invita nuovo Utente

Puoi invitare un **nuovo Utente** a registrarsi al portale ed accedere al **tuo Account**.

Per invitare un nuovo Utente puoi seguire i seguenti passaggi:

1. Premi il bottone **Invita utente** posto in alto a destra nella sezione;
2. Seleziona la modalità di invito tra **Invia email di invito**. *Verrà inviata una email al nuovo utente contenente tutte le informazioni per accedere al tuo Account.*
3. Inserisci l’**indirizzo email** dell’utente da invitare;
4. Seleziona il **Ruolo** da applicare al nuovo utente, per maggiori informazioni sui ruoli segui questa [**guida**](ruoli-dettaglio-dei-permessi.md);
5. Premi il bottone **Invita utente** nella finestra di dialogo per confermare l’operazione e verrà **inviata la mail di invito all’indirizzo Email indicato**.
6. Una volta completata la registrazione verifica che il nuovo Utente sia presente nella lista Utenti nella pagina.

:::info
Il codice invito ha una validità di **7 giorni** dal momento della conferma di invito. Nel caso scada potrai invitare nuovamente l’utente inviando una nuova email di invito.

[!TIP]
Il codice invito è effettivamente utilizzabile solo dopo che avrai confermato l’invito del nuovo utente mediante il bottone **Invita utente**.

[!WARNING]
Per completare la registrazione del nuovo utente puoi seguire questa [**guida**](../../registrazione/accedi-ad-un-account-esistente.md).
:::

# Accedi al dettaglio Utente

Nel dettaglio dell’Utente sono riportati i dati dell’utente, le informazioni sull’ultimo accesso, la lingua predefinita e la configurazione dell’autenticazione a multifattore (MFA).

Per accedere al dettaglio di un Utente puoi seguire i seguenti passaggi:

1. Premi sul **Nome e cognome** dell’Utente nella lista degli utenti

## Modifica Utente

Per modificare o aggiornare i dati dell’Utente puoi seguire i seguenti passaggi:

1. Premi il bottone **Modifica** posto in alto a destra nella pagina;
2. Modifica i dati con le nuove informazioni;
3. Premi il bottone **Salva** posto in fondo alla sezione per salvare le modifiche;
4. Verifica che le nuove informazioni inserite siano correttamente mostrate nella pagina.

:::tip
Puoi arricchire il tuo Utente di ulteriori informazioni di contatto, come il numero di telefono e di cellulare.

[!WARNING]
L’**Email/Username** non può essere modificato.
:::

![](/kb-assets/311b8cd56d-image-20220907-145259.png)

## Autenticazione multifattore (MFA)

L'autenticazione a multifattore (MFA) ti consente di aumentare il livello di sicurezza del tuo utente, richiedendo l'inserimento di un codice per effettuare l'accesso al portale. In questa sezione puoi reimpostare la configurazione del MFA. L’autenticazione Multi-Fattore è obbligatoria.

:::info
Troverai maggiori informazioni nella guida dedicata all’[**autenticazione multifattore (MFA)**](autenticazione-multifattore-mfa.md).
:::

## Reimposta la password

Per reimpostare la password dell’Utente puoi seguire i seguenti passaggi:

1. Premi il bottone **Reimposta password** posto in alto a destra nella pagina
2. Premi il bottone **Reimposta password** nella finestra di dialogo per confermare l’operazione.

:::warning
Le password degli utenti Cortex hanno **validità 90 giorni**. Al raggiungimento del termine è necessario aggiornare la propria password, creandone una diversa dalle 24 precedenti password impostate.

[!INFO]
Verrà inviata una email all’utente contente il link per reimpostare la password.

[!NOTE]
Stai cercando come reimpostare la password dalla pagina di login? [**Segui le istruzioni riportate qui**](index.md#Reimposta-la-password)

[!NOTE]
Per reimpostare la password è necessario seguire alcuni criteri di sicurezza consultabili a questa [**guida**](criteri-di-sicurezza-e-gestione-degli-accessi-su-cortex.md)**.**
:::

## Disattiva/Attiva Utente

Per gestire lo stato dell’Utente puoi seguire i seguenti passaggi:

1. Premi il bottone **Disattiva utente** o **Attiva utente** posto in alto a destra nella pagina
2. Premi il bottone **Disattiva utente** o **Attiva utente** nella finestra di dialogo per confermare l’operazione

:::warning
Un Utente **Disattivo** non può fare login su Cortex.

[!CAUTION]
Non puoi disattivare l’utente che stai attualmente utilizzando per operare su Cortex.
:::

## Elimina Utente

Per eliminare l’Utente puoi seguire i seguenti passaggi:

1. Premi il bottone **Elimina utente** posto in alto a destra nella pagina
2. Premi il bottone **Elimina** nella finestra di dialogo per confermare l’operazione

:::caution
L’eliminazione dell’utente è un’operazione **definitiva** ed **irreversibile**.

[!CAUTION]
Non puoi eliminare l’utente che stai attualmente utilizzando per operare su Cortex.
:::

## Gestisci i consensi del tuo utente

CloudFire si impegna costantemente nella gestione del Trattamento dei tuoi dati personali e, in conformità con le normative vigenti è necessario che tu esprima le tue preferenze in merito a:

- Trattamento dei Dati personali da parte di CloudFire, così come descritto nell’[Informativa Privacy](https://www.cloudfire.it/informative/informativa-privacy);
- Ricezione comunicazioni di Marketing relative a prodotti, servizi ed Eventi CloudFire.

Per gestire i consensi del proprio Utente puoi seguire i seguenti passaggi:

1. Accedi alla tab **Consensi** nel dettaglio dell’utente;
2. Modifica e aggiorna le tue preferenze utilizzando il bottone in corrispondenza di ogni consenso esplicito.

:::info
Se non hai ancora espresso i consensi relativi al tuo utente e hai già un utente attivo in Cortex, al primo login, in seguito all’implementazione della funzionalità gestione consensi, si aprirà una modale in cui ti verrà richiesto di esprimere le tue preferenze.
:::

## Chiavi API

Le Chiavi API vengono utilizzate nell’autenticazione per fornire agli utenti o agli script di programmazione un accesso alle risorse e ai servizi del tuo account Cortex tramite le API Cortex.

:::info
Troverai maggiori informazioni nella guida dedicata alle [**Chiavi API**](chiavi-api.md).
:::

# Reimposta password da pagina di login

Per reimpostare la password del tuo Utente puoi seguire i seguenti passaggi:

1. Premi il link **Forgot password?** posto sotto al campo password;
2. Inserisci l’**Email/Username** del tuo utente;
3. Premi il bottone **Reset password** per confermare l’operazione.

:::info
Ti verrà inviata una email contente il link per reimpostare la password.

[!NOTE]
Per reimpostare la password è necessario seguire alcuni criteri di sicurezza consultabili a questa [**guida**](criteri-di-sicurezza-e-gestione-degli-accessi-su-cortex.md)**.**

[!NOTE]
Stai cercando come reimpostare la password dalla pagina Utenti? [**Segui le istruzioni riportate qui**](index.md#Reimposta-la-password)
:::