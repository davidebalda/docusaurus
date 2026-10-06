---
title: "Configurazione Provider SIP Account - Talky Time"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina definisce i passaggi da seguire per per configurare un provider SIP Account.

## Configura un provider PSTN {#configura-un-provider-pstn}

La scelta della tipologia PSTN come provider è corretta qualora si intenda utilizzare Microsoft Teams come PBX oppure integrarci numerazioni PSTN (Public Switched Telephone Network), sia che siano numerazioni singole che GNR.

Nel scegliere tale tipologia di provider è necessario poi scegliere tra due scenari:

- **SIP User**: seleziona tale scenario se ogni numero geografico che vuoi integrare ha le proprie credenziali SIP, Username e Password.
- **SIP Trunk**: seleziona tale scenario se i numeri geografici che vuoi integrare sono parte di un GNR o selezione passante ed hai una singola credenziale SIP, Username e password, per tutti i numeri.

### Configurazione SIP Extension {#configurazione-sip-extension}

Per configurare un provider PSTN è sufficiente seguire i seguenti passaggi:

1. Nella Tab **Provider**, clicca su **Nuovo Provider**
2. Premi nella sezione Tipologia **SIP Account**
3. Procedi ora con la configurazione dei dettagli finali quali:
1.   **Account Sip**: Scegli tra i SIP Account creati in precedenza nell’omonima sezione
2.   **Numerazione Principale**: il numero senza prefisso internazionale, di default ti presenterà gli la numerazione principale dell’Account Sip scelto.
3.   **Nome Provider**: utilizzalo per identificare il provider durante il collegamento degli utenti
4. Premi su **Crea Provider**.

:::tip
Una volta completato tale configurazione, nella tab **Provider** trovi il provider appena creato, con indicazione di: Stato *Attivo*, nome *CloudFire SIP Account*, Tipologia *SIP Account.*
Da questo momento puoi [associare gli utenti](../utenti-teams-talky-time-direct-routing/index.md) ed iniziare ad utilizzare l’App Microsoft Teams con gli account SIP scelti.
:::

![](/kb-assets/318e565996-image-20220906-080808.png)