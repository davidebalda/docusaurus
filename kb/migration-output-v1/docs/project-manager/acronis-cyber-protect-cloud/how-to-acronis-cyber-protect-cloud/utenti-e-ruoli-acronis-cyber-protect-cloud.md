---
title: "Utenti e Ruoli - Acronis Cyber Protect Cloud"
---

Acronis dà la possibilità di creare vari utenti con ruoli differenti, qui potrete trovarne una lista ed una breve descrizione.

### Come creare un utente

Creare un utente è molto semplice, basterà seguire i seguenti passaggi:

1. Dalla homepage, selezionare **Users**;![](/kb-assets/3c88211930-acronis-users1.png)
2. Una volta entrati nella sezione, in alto a destra troverete il bottone **+New** - cliccatelo e dal menù selezionate **User**;  
![](/kb-assets/8e31e6a729-clickuser.png)
3. La pagina per la creazione dell’utente è la seguente - dovrete inserire il le informazioni di Login per il nuovo utente, un indirizzo email, nome e cognome (facoltativi), e la lingua dell’account:  
![](/kb-assets/bafb00d3be-acronis-utenti.png)
4. Una volta compilata la scheda, cliccate su **Create** ed avrete un nuovo utente.

### Differenze fra i vari ruoli

#### Company Administrator

![](/kb-assets/b41ebafc71-compadmin.png)

Il ruolo di Company Administrator dà diritti ad ogni servizio, e se il servizio di Disaster Recovery risulta attivo, l’utente avrà accesso anche alle funzionalità recovery.

:::tip
Il Company Administrator ha automaticamente accesso al **Management Portal** e al ruolo di **Protection** - questi sono selezionati dal sistema e non possono essere rimossi.
:::

#### Management Portal

![](/kb-assets/41d6cda43e-portalmana.png)

Il **Management Portal** permette all’utente *amministratore* di gestire i vari utenti all’interno della propria organizzazione. Ci sono due tipo di amministratore:

- **Administrator:** può modificare e gestire utenti;
- **Read-only Administrator**: ha accesso al portale Management ma non può eseguire alcuna azione amministrativa.

#### Protection

![](/kb-assets/258f180796-protector.png)

Questo ruolo permette la gestione di normali backup. Non ha l’accesso alla funzionalità di Disaster Recovery, che è riservata al Company Administrator.

![](/kb-assets/17c0890054-restore-operator.png)

Come potete vedere, ci sono varie tipologie di utente che possono avere questo ruolo:

- **User**: un utente che non ha accesso al portale Management, il cui accesso a servizi e ruoli è definito dall’amministratore;
- **Administrator** e **Read-only Administrator**;
- **Restore Operator**: un utente abilitato alla gestione dei backup e al recovery delle applicazioni in maniera più precisa, potendo quindi gestire specifiche risorse (inclusi Microsoft 365 e Google Workspace), limitando l’accesso ai contenuti sensibili qualora non fosse un amministratore. Può vedere la lista dei backup e gli avvisi ma non può cancellarli.

:::warning
Questo ruolo è disponibile solo con Cyber Protection.
:::

- [Come creare un utente](#come-creare-un-utente)
- [Differenze fra i vari ruoli](#differenze-fra-i-vari-ruoli)
-   [Company Administrator](#company-administrator)
-   [Management Portal](#management-portal)
-   [Protection](#protection)