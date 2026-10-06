---
title: "Profile (2) (2)"
---

## Introduzione

Il **Profile** del **Portale Tenant** è la sezione in cui potete modificare le impostazioni generali del vostro Tenant.

## Guida passo-passo

### Accesso

Una volta eseguito l'accesso al **Portale Tenant,** cliccate sulla faccina in alto a destra e di seguito su **Profile.**

![](/kb-assets/151697fc6b-image2019-9-13-10-49-25.png)

### **Dashboard**

![](/kb-assets/aa37ef9935-image2019-9-17-15-44-23.png)

![](/kb-assets/32588fe242-image2019-9-17-15-44-44.png)

### Descrizione dei vari campi

#### Details

- **Email:** indirizzo mail di riferimento del **Tenant.**
- **Default Language:** lingua di default del **Tenant.**
- **Default Dashboard:** dashboard che verrà visualizzata quando effettuerete l'accesso al **Portale Tenant.**
- **Profile Picture:** icona che verrà visualizzata in alto a destra all'interno del **Portale Tenant.**
- **Timezone:** fuso orario.
- **Default Outgoing Rule Group: Rule Group** di default che verrà utilizzata se vengono configurati delle destinazioni esterne come parte di **Ring Group, IVR etc.**

:::info
Vedi [Chiamate esterne da Ring Group o IVR non funzionanti](../../troubleshoot-cloud-pbx/chiamate-esterne-da-ring-group-o-ivr-non-funzionanti.md)
:::

- **External Call Ring Type:** opzione che regola il tipo di Ring Tone per le chiamate esterne. Salvo indicazione particolare non modificare questo settaggio che è stato ottimizzato sull'infrastruttura Cloudfire.
- **MOH:** musica d'attesa che verrà utilizzata durante la normale messa in attesa da parte di un extension.
- **Invoice Recipient Email(s):** indirizzo mail del destinatario delle fatture. Settaggio inutile in quanto la fatturazione viene fatta fuori dal CloudPBX.

#### Address

- **First Name:** Nome del referente per questo Tenant del CloudPBX.
- **Last Name:** Cognome del referente per questo Tenant del CloudPBX.
- **Business Name:** Nome dell'azienda.
- **Address 1:** primo indirizzo di riferimento.
- **Address 2:** secondo indirizzo di riferimento.
- **City:** città.
- **State:** stato.
- **ZIP:** CAP.

#### Settings

- **Callback URL:** URL diu destinazione della funzione di avviso di chiamata (feature ancora in fase di test).
- **Maximum Fax Tries:** numero massimo di prove di invio Fax prima che venga considerato fallito.
- **Fax Tries Pause Interval(in seconds) \*:** intervallo in secondi di attesa tra una prova di invio fax e l'altra.
- **Original CallerID on Transfer:** se abilitata mantiene il Caller ID originale dopo i trasferimenti di chiamata.
- **Original CallerID on Forward:** se abilitata mantiene il Caller ID originale dopo le deviazioni di chiamata.
- **Feature Code PIN:** PIN per l'attivazione dei Codici riferiti al Tenant (per maggiori info controllare [Feature List](feature-list.md))

#### About Us

- **Logo:** Logo del Tenant.
- **About Us:** Breve descrizione del Tenant o dell'azienda.

  

  

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Guida passo-passo](#guida-passo-passo)
-   [Accesso](#accesso)
-   [Dashboard](#dashboard)
-   [Descrizione dei vari campi](#descrizione-dei-vari-campi)
  
  -   [Details](#details)
  
  -   [Address](#address)
  
  -   [Settings](#settings)
  
  -   [About Us](#about-us)
* * *
**Articoli collegati**


- Page:
[Impossibile chiamare o ricevere chiamate](../../troubleshoot-cloud-pbx/impossibile-chiamare-o-ricevere-chiamate.md)
- Page:
[Portale Extension - Opzioni e Funzionalità](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/1966256717/Portale+Extension+-+Opzioni+e+Funzionalit)
- Page:
[Portale Extension - Extension Settings](../portale-extension/portale-extension-extension-settings.md)
- Page:
[Deviazioni di chiamata](../deviazioni-di-chiamata.md)
- Page:
[BLF Call-pickup](../blf-call-pickup.md)
:::