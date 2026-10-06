---
title: "Aggiornamento versione Talky Time Direct Routing"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

# Prerequisiti aggiornamento

Prima di procedere alla configurazione del Dominio Teams all’interno della piattaforma Cortex occorre controllare di avere:

1. **Credenziali Microsoft** di un utente con privilegi sia di **Global Administrator** che di **Teams Administrator** da utilizzare per la configurazione; Una o più licenze per ogni utente Talky Time Direct Routing da attivare e un’ulteriore licenza Microsoft da assegnare all’utente di servizio. Vedi il dettaglio dei requisiti per la sincronizzazione del dominio a questa [**guida**](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/1966250086/Dominio+Microsoft+Teams+-+Talky+Time+Legacy#Requisiti)**.**
2. **Fully Qualified Domain Name (FQDN)** o l'**Indirizzo IP pubblico (IPv4) del Provider**;
3. **Porta** di comunicazione del protocollo **SIP** (con trasporto UDP) del Provider.
4. Credenziali SIP degli Utenti

# Procedura aggioramento

## Dismissione vecchia versione

Per procedere all’aggiornamento della versione di Talky Time è necessario seguire i seguenti passaggi:

1. Accedi al servizio **Talky Time**. Non sai come fare? Segui la nostra [**guida**](../index.md)**.**
2. Seleziona la voce **Direct Routing** dal menù di navigazione laterale, oppure premi su gestisci in corrispondenza della card **Direct Routing.**
3. Nella sezione Utenti Teams **scollega gli Utenti Teams** attivi dall’azione disponibile in corrispondenza di ciascun utente. Se non sai come fare segui questa [**guida**](utenti-teams-talky-time-direct-routing/index.md)**.**
4. Nella sezione Provider **Elimina i Provider attivi** dall’azione disponibile in corrispondenza di ciascun provider. L’azione Elimina è disponibile solo se tutti gli utenti configurati sono stati disassociati. Se non sai come fare puoi seguire questa [**guida**](provider-talky-time/index.md)**.**
5. Nella sezione Dominio **Scollega ed Elimina il Dominio**. Se non sai come fare puoi seguire questa [**guida**](dominio-microsoft-teams-talky-time-direct-routing/index.md).

## Configurazione nuova versione

1. Sincronizza nuovamente il dominio, con i medesimi requisiti seguendo questa [**guida**](dominio-microsoft-teams-talky-time-direct-routing/index.md);
2. Crea nuovamente i Provider seguendo questa [**guida**](https://cloudfireit.atlassian.net/l/cp/tG0WDrkU);
3. Collega nuovamente gli utenti Teams seguendo questa [**guida**](utenti-teams-talky-time-direct-routing/index.md).

:::info
Assicuratevi che la vostra licenza contenga **almeno** i seguenti due servicePlansName: `MCOEV - 4828c8ec-dc2e-4779-b502-87ac9ce28ab7` e `TEAMS1 - 57ff2da0-773e-42df-b2af-ffb7a2317929` e non sia in grace period. Non è, al momento, previsto il supporto di licenze in grace period.  
  
[https://learn.microsoft.com/en-us/microsoft-365/commerce/subscriptions/what-if-my-subscription-expires?view=o365-worldwide](https://learn.microsoft.com/en-us/microsoft-365/commerce/subscriptions/what-if-my-subscription-expires?view=o365-worldwide)
:::

# Troubleshoot

Se, a seguito della configurazione alla nuova versione, riscontri problemi di ricezione di chiamate sulla numerazione principale è necessario controllare che il numero sia associato al Resource Account di Microsoft Teams®.

Per risolvere questa problematica puoi seguire questi passaggi:

1. Accedi al portale **Microsoft 365 Admin Center** con le credenziali **Global Administrator**;
2. Seleziona la voce sul menù laterale e accedi al portale **Admin Center Teams** con credenziali di **Teams Administrator**;
3. Seleziona **Voce/Voice** dal menù a sinistra;
4. Seleziona la voce Account di Risorse o Resource Account;![](/kb-assets/ff4ec30cdc-image-20230721-091501.png)
5. Seleziona il **Resource Account** che è impostato per ricevere le chiamate. In questo momento infatti non avrai alcun numero di telefono associato ai vari Resource Account;
6. Premi il bottone **Assegna/Annulla assegnazione**
7. Si aprirà una finestra sulla destra in cui dovrai:
1.   Seleziona la voce **Instradamento Diretto** dal primo menù a tendina “Tipo di numero di Telefono”;
2.   Inserisci il numero di telefono assegnato, ovvero la numerazione principale a cui le telefonate devono arrivare;
3.   Premi sul bottone **Salva**

![](/kb-assets/e29ea35e45-image-20230721-092446.png)

:::warning
Se il problema persiste, ti invitiamo ad aprire un [Case](../../../../account-manager/supporto/case.md) al nostro supporto.
:::