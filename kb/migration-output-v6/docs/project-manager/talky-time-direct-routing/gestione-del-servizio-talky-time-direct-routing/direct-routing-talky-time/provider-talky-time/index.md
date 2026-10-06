---
title: "Provider - Talky Time"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

I **Provider** sono i fornitori delle Numerazioni telefoniche o le tipologie di VPBX.

Questa pagina definisce i passaggi da seguire per configurare i Provider.

## Accedi alla sezione Provider {#accedi-alla-sezione-provider}

Per accedere al sezione Provider puoi seguire i seguenti passaggi:

1. Accedi al servizio **Talky Time Direct Routing** dalle voci di menù laterale, sotto la categoria **Unified Communication**. Non sai come fare? Segui la nostra [**guida**](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/1966249437/Gestione+del+servizio+-+Talky+Time#Accedi-al-servizio-Talky-Time)**.**
2. Seleziona la voce **Provider** dalle tab di navigazione in alto.

![Screenshot 2024-04-26 at 14.36.36.png](/kb-assets/4a5ed290ec-screenshot-2024-04-26-at-14-36-36.png)

### Tipologie di Provider {#tipologie-di-provider}

Esistono varie tipologie di Provider che si possono ricondurre alla tipologia di fornitori di numerazioni telefoniche oppure alle tipologie di Virtual PBX. Queste sono:

- **PBX**: utilizza questa tipologia di provider qualora avessi già un PBX SIP che intendi collegare all’utente Microsoft Teams. Il tuo fornitore di rete telefonica è riconducibile ad un PBX.
- **PSTN**: utilizza questa tipologia di provider qualora intendi utilizzare Microsoft Teams come PBX oppure integrarci numerazioni PSTN (Public Switched Telephone Network), sia che siano numerazioni singole che GNR.
- **SIP Account**: utilizza questa tipologia di provider se hai già attivato un Account SIP nella sezione SIP Account, di conseguenza CloudFire è il tuo fornitore di rete telefonica.

Per configurare i provider puoi seguire le seguenti guide:

### Scenari e Tipologie di Provider {#scenari-e-tipologie-di-provider}

|     |     |     |     |
| --- | --- | --- | --- |
|     | **Generic PBX - Asterisk - 3cx - Wildix - Avaya - Trixbox - FreeSwitch - FreePBX - Kalliope** | **SIP Trunk** | **SIP Extension** |
| **Integrazione con PBX aziendale** | SUPPORTATO | NON SUPPORTATO | NON SUPPORTATO |
| **Configurazione numeri geografici**  <br>**(1 utente - 1 numero)** | NON SUPPORTATO | SUPPORTATO | SUPPORTATO |
| **Configurazione numeri geografici aggiuntivi / GNR**  <br>**(1 utente - multipli numeri)** | NON SUPPORTATO | SUPPORTATO | NON SUPPORTATO |

### Azioni su Provider {#azioni-su-provider}

Nella Tab **Provider** sono mostrati tutti i Provider creati con le rispettive informazioni quali Stato, Nome, Tipologia.

Per entrare nel dettaglio di ogni provider **Premi** sul nome del Provider, in questo caso Knowledge Base.

La pagina che segue mostra il dettaglio del provider selezionato, sempre da qui è possibile modificarne la configurazione e visualizzare lo stato dello stesso.

Qualora il Provider sia in stato **Attivo**, in corrispondenza di ciascun provider, è possibile effettuare le seguenti azioni, modificandone lo stato dello stesso:

![](/kb-assets/ce7cab3fd2-screenshot-2022-01-07-at-18-22-16.png)

- **Disattiva** : rende *NON* disponibile il provider per il collegamento degli utenti sia in caso di collegamento singolo utente che in caso di import massivo
- **Elimina** : cancella il Provider (disponibile solo se tutti gli utenti configurati sono stati disassociati)