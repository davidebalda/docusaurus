---
title: "Configurazione Provider PSTN - Talky Time"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina definisce i passaggi da seguire per per configurare un provider PSTN.

# Configura un provider PSTN

La scelta della tipologia PSTN come provider è corretta qualora si intenda utilizzare Microsoft Teams come PBX oppure integrarci numerazioni PSTN (Public Switched Telephone Network), sia che siano numerazioni singole che GNR.

Nel scegliere tale tipologia di provider è necessario poi scegliere tra due scenari:

- **SIP User**: seleziona tale scenario se ogni numero geografico che vuoi integrare ha le proprie credenziali SIP, Username e Password.
- **SIP Trunk**: seleziona tale scenario se i numeri geografici che vuoi integrare sono parte di un GNR o selezione passante ed hai una singola credenziale SIP, Username e password, per tutti i numeri.

## Configurazione SIP Extension

Per configurare un provider PSTN è sufficiente seguire i seguenti passaggi:

1. Nella Tab **Provider**, clicca su **Nuovo Provider**
2. Premi nella sezione Tipologia **PSTN**
3. Seleziona lo scenario **SIP User**
4. Procedi ora con la configurazione dei dettagli finali:
1.   **FQDN/IP**: indirizzo del Provider (es. *sip.cloudfire.it*)
2.   **Porta SIP**: porta UDP su cui è in ascolto il servizio SIP (es. 5060)
3.   **Nome Provider**: utilizzalo per identificare il provider durante il collegamento degli utenti (es. CloudFire SIP User)
5. Premi su **Crea provider**.

:::tip
Una volta completato tale configurazione, nella tab **Provider** trovi il provider appena creato, con indicazione di: Stato *Attivo*, nome *CloudFire SIP Account*, Tipologia *SIP Account.*
Da questo momento puoi [associare gli utenti](../utenti-teams-talky-time-direct-routing/index.md) ed iniziare ad utilizzare l’App Microsoft Teams con gli account SIP scelti.
:::

![](/kb-assets/cea7101c77-image-20230320-150605.png)

## Configurazione SIP Trunk

Per configurare un provider PSTN con scenario SIP Trunk è sufficiente seguire i seguenti passaggi:

1. Nella Tab **Provider**, clicca su **Nuovo Provider**
2. Premi nella sezione Tipologia **PSTN**
3. Seleziona lo scenario **SIP Trunk**
4. Procedi ora con la configurazione dei dettagli finali:
1.   **FQDN/IP**: indirizzo del Provider (es. *sip.cloudfire.it*)
2.   **Porta SIP**: porta UDP su cui è in ascolto il servizio SIP (es. 5060)
3.   **Nazione**: la nazione di appartenenza della numerazione (es. Italia)
4.   **Prefisso provider**: se hai dubbi lascia il campo compilato di default, altrimenti contatta il tuo Provider
5.   **Numerazione Principale**: il numero senza prefisso internazionale (es. 052217534)
6.   **Username SIP**: username dell' account SIP
7.   **Password SIP**: password dell' account SIP
8.   **Nome Provider**: utilizzalo per identificare il provider durante il collegamento degli utenti
5. Clicca su **Crea Provider**.

:::tip
Una volta completato tale configurazione, nella tab **Provider** trovi il provider appena creato, con indicazione di: Stato *Attivo*, nome *CloudFire SIP Account*, Tipologia *SIP Account.*
Da questo momento puoi [associare gli utenti](../utenti-teams-talky-time-direct-routing/index.md) ed iniziare ad utilizzare l’App Microsoft Teams con gli account SIP scelti.
:::

![](/kb-assets/95889973c6-image-20230320-150723.png)