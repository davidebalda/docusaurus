---
title: "Device - Autoprovisioning (2) (2)"
---

## Introduzione

In questo sotto menù è possibile configurare l'**auto-provisioning** dei telefoni IP.

## Prerequisiti

:::info
Prima di proseguire in questa guida controllare marca e modello dei telefoni IP allegata a questa guida:
[**Tabella dispositivi Supportati**](../../guide-ai-telefoni-supportati/elenco-telefoni-supportati.md)
Solo i modelli "**Certified**" e "**Tested**" saranno completamente configurabili attraverso l'auto-provisioning.
I modelli solo "**Certified**" non avranno tutte le funzionalità configurabili attraverso l'auto-provisioning.
:::

Per auto-provisionare i telefoni sip dovete collegarli ad una rete che abbia la possibilità di comunicare con la sub-net **185.132.68.112/28**, per cui controllate le regole firewall per la rete telefonica.

Per fare in modo che i telefoni si possano provisionare dovete aggiungere l'**option 66 (tipologia ascii)** all'interno del DHCP server che distribuisce gli IP alla rete telefonica, il valore da assegnare a questa opzione è il seguente: [**http://{user}:{password}@pbx.cloudfire.it/hpm/provision/**](https://hpmaccess:7488R!9TREIq@pbx.cloudfire.it/hpm/provision/)  

:::warning
Essendo il Server autenticato, aprire una segnalazione con il nostro supporto per avere username e password per l'autenticazione del Server.
:::

## Guida passo-passo

Ora vi illustreremo come eseguire l'associazione **Dispositivo → Extension**:

- Cliccare sul bottone ![](/kb-assets/27363b9bd4-image2019-4-4-10-24-54.png)
- Compilare i vari campi come segue e cliccare su create:  
![](/kb-assets/d99bb1d8ff-image2019-4-4-10-26-22.png)

:::warning
**ATTENZIONE**, tutti i campi sono provvisti di auto-completamento, ma per attivalo occorre compilare i campi nel seguente ordine:
1. **Mac Address**
2. **Device Template**
3. **Line Number**
4. **Extension Type**
5. **Extension**
6. **Line Label**
:::

1. **Mac Address:** inserire l'indirizzo Mac del telefono IP da provvisionare, questo indirizzo va inserito **senza** punteggiatura.
2. **Device Template:** inserire il template in base al modello del telefono IP da provvisionare.

:::warning
Utilizzate sempre i template con la desinenza **\_Production,** che sono i template funzionanti e testati. Gli altri template sono dei test oppure presentano configurazioni non standard che potrebbero compromettere il corretto funzionamento dei vostri apparati.
:::

1. **Line Number:** inserire il numero corrispondente alla linea (e.g. identity per SNOM o account per Yealink) del dispositivo SIP associare l'extension.
2. **Extension Type:**
1.   **EXTENSION:** extension interna del vostro CloudPBX.
2.   **CUSTOM:** extension esterna al CloudPBX. E' possibile infatti configurare un extension di un altro centralino IP. Compilare tutti i nuovi campi che compariranno.
3. **Extension:** specificare quale extension registrare sul dispositivo.
4. **Line Label:** etichetta da applicare all'extension.
5. **Device Note:** note a vostra discrezione.
6. **TFTP Access:** abilitare in caso di utilizzo di un TFTP server per l'upgrade del firmware (funzionalità non ancora supportata).

## Funzionalità aggiuntive

Una volta creato il device vi comparirà nell'elenco dei dispositivi:

![](/kb-assets/4ce44f6385-image2019-4-4-10-59-5.png)

Cliccando sui vari pulsanti di fianco avrete modo di gestire diverse funzionalità.

![](/kb-assets/339bda0603-image2019-4-4-11-2-42.png)

![](/kb-assets/07a1e0d48d-image2019-4-4-11-1-48.png)

 Questo bottone permette di visualizzare le linee e le key associate al dispositivo:

![](/kb-assets/58e087d1ba-image2019-4-4-11-9-48.png)

 Questo bottone permette di eliminare il Device

![](/kb-assets/d935edbaf8-image2019-4-4-11-10-28.png)

 Questo bottone permette di riavviare da remoto il dispositivo.

![](/kb-assets/db69e9ac6c-image2019-4-4-11-11-14.png)

Questo bottone permette di modificare l'indirizzo MAC associato all'extension e le credenziali di accesso all'interfaccia web del dispositivo stesso.

:::caution
Non è possibile modificare il template. Per poterlo fare dovete eliminare il device con il bottone al punto 2 e rifarlo.

[!INFO]
Qui vi sarà possibile cambiare la **password** d'accesso alla Web GUI del vostro apparato. Di default la password è **123456**
:::

![](/kb-assets/1a2c3a1cda-image2019-4-4-11-15-2.png)

 Questo bottone permette di aggiungere, modificare o eliminare la configurazione delle linee (e.g. identity per SNOM o account per Yealink).

:::warning
In questa lista non può essere presente meno di 1 line configurata.
:::

![](/kb-assets/8ba5869fa2-image2019-4-4-11-19-8.png)

Questo bottone permette di configurare i valori delle **programmable keys** (tasti programmabili) del vostro telefono IP.

- **Category:** tipo di tasto programmabile che si vuole configurare. In base al dispositivo le categorie vengono matchate in maniera diversa.
- **Key number:** numero identificativo del tasto programmabile.
- **Type:** tipo di funzionalità da applicare al tasto programmabile
- **Line:** linea (e.g. identity per SNOM o account per Yealink) a cui viene associata la configurazione del tasto programmabile.
- **Extension:** extension da associare al tasto programmabile, inserire un numero di extension esistente per attivare l'auto-completamento.
- **Value:** valore da associare al tasto programmabile.
- **Label:** etichetta da associare al tasto programmabile.

Qui sotto esempio di configurazione del tasto programmabile 5 di uno SNOM D715 come BLF:

![](/kb-assets/34ed7f36a6-image2019-4-4-12-13-28.png)

Qui il link per configurare i BLF per effettuare il call [**pick-up**](../../blf-call-pickup.md)**.**

## Personalizzazioni

Se desiderate delle personalizzazioni per il template dei telefoni dovete aprire una **Service Request** al nostro servizio di assistenza tecnica, specificando marca e modello del telefono e l'elenco delle personalizzazioni richieste.

[**Guida apertura segnalazioni**](https://cloudfireit.atlassian.net/wiki/pages/createpage.action?spaceKey=KB&title=Guida%20apertura%20segnalazioni&linkCreation=true&fromPageId=1966255283)

  

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Guida passo-passo](#guida-passo-passo)
- [Funzionalità aggiuntive](#funzionalit-aggiuntive)
- [Personalizzazioni](#personalizzazioni)
* * *
**Articoli collegati**


- Page:
[Impossibile chiamare o ricevere chiamate](../../../troubleshoot-cloud-pbx/impossibile-chiamare-o-ricevere-chiamate.md)
- Page:
[SNOM - Factory Reset](../../snom-factory-reset.md)
- Page:
[Portale Extension - Profile](../../portale-extension/portale-extension-profile.md)
- Page:
[Portale Extension - Opzioni e Funzionalità](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/1966256717/Portale+Extension+-+Opzioni+e+Funzionalit)
- Page:
[Funzionalità Call Flow Control - Day/Night](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/1966256564/Funzionalit+Call+Flow+Control+-+Day+Night)
:::