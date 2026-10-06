---
title: "Configurazione Provider PBX - Talky Time"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina definisce i passaggi da seguire per configurare un provider PBX.

## Configura un provider PBX {#configura-un-provider-pbx}

Per configurare un provider PBX è sufficiente seguire i seguenti passaggi:

1. Nella Tab **Provider**, clicca su **Nuovo Provider**
2. Seleziona la Tipologia **PBX**
3. Seleziona la tipologia di PBX con il quale eseguire l’integrazione. Nella finestra riportata di seguito sono elencati una serie di PBX, quali **Generic PBX** - **Asterisk** - **3cx - Wildix - Avaya - Trixbox - FreeSwitch - FreePBX - Kalliope**. In relazione al PBX scelto verranno mostrate diversi moduli con passaggi e requisiti specifici al PBX.  
Nel caso in cui non fosse presente il PBX di cui vuoi effettuare l’integrazione utilizza il campo **Generic PBX**. Tale lista viene costantemente aggiornata per soddisfare al meglio le richieste di qualsiasi realtà.
4. Scegli il **numero identificativo** ovvero la numerazione che identifica la sede in cui si trova il PBX e che permette di distinguere le singole extension anche in caso di più provider configurati. (es. + 39 02 xxxxx ext xxxxx).  
Puoi optare tra:
-   **numero identificativo generico**: se selezioni tale opzione il numero identificativo viene assegnato da CloudFire ed è legato al distretto di Milano.
-   **numero identificativo personalizzato**: se selezioni tale opzione puoi personalizzare il numero identificativo e configurare la numerazione principale del PBX che stai integrando nel campo **numero identificativo**.  
  Questo ti permetterà di distinguere le extension in base alle sedi e di poter usare la stessa extension su più Provider.
5. Inserisci il **Fully Qualified Domain Name (FQDN)** o l'**Indirizzo IP pubblico (IPv4)** del Provider. *Il FQDN corrisponde all’indirizzo completo a cui risponde il centralino (es.* [*pbx.cloudfire.it*](http://pbx.cloudfire.it)*)*
6. Inserisci la **Porta** di comunicazione del protocollo **SIP** (con trasporto UDP) del Provider. *La porta SIP è la porta TCP o UDP su cui è in ascolto il PBX (es. 5060)*
7. Inserisci un **Nome identificativo** per il Provider;
8. Premi sul bottone **Crea provider**.

![](/kb-assets/efd1a622da-image-20220906-080536.png)

:::tip
Una volta completato tale configurazione, nella tab **Provider** trovi il provider appena creato, con indicazione di: Stato *Attivo*, Tipologia *PBX.*
Da questo momento puoi [associare gli utenti](../utenti-teams-talky-time-direct-routing/index.md) ed iniziare ad utilizzare l’App Microsoft Teams come interno del tuo PBX
:::