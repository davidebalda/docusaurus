---
title: "Portale Extension - Voicemail"
---

## Introduzione

In questo sotto-menù è possibile gestire la voicemail dell'extension in cui si è loggati. La voicemail è riconducibile alla segreteria telefonica dell'extension. Infatti abilitandola è possibile lasciare dei messaggi vocali per l'extension quando quest'ultima risulta non disponibile, occupata oppure come destinazione di diverse deviazioni di chiamata.

## Prerequisiti

Per poter accedere e visualizzare questo sotto-menù, dovrà essere abilitata l'opzione **Voicemail.** Questa opzione è disponibile sia da [**Portale Tenant → Extension**](../portale-tenant-cloud-pbx/service-2-2/extension-2-2.md), sia da [**Portale Extension → Extension Settings**](portale-extension-extension-settings.md)

## Descrizione dei vari sotto-menù

### Voicemail Greetings

In questo sotto-menù è possibile caricare e gestire i file audio che verranno riprodotti quando il chiamante dovrà lasciare un messaggio per l'extension in questione.

Cliccando su![](/kb-assets/dc1f999f78-image2019-8-13-9-21-1.png)

è possibile caricare un nuovo messaggio.

Bisogna inserire un nome per il file audio e poi decidere il **Type** di file audio:

1. **File:** selezionando "File" apparirà un form dov'è possibile caricare un file audio in formato .waw o in formato .mp3
2. **Recording:** Selezionando "Recording" e inserendo un numerazione (interno o external) e cliccando su ***Create*** partirà una chiamata verso la numerazione inserita. Rispondendo sentirete una voce guida che vi inviterà a registrare il vostro messaggio di benvenuto per la Voicemail.

### Voicemail Settings

In questo sotto-menù è possibile gestire le varie opzioni per la **Voicemail:**

![](/kb-assets/846289fade-image2019-8-13-9-31-31.png)

- **Voicemail to Email:** se abilitata invia una copia del messaggio lasciato all'indirizzo mail specificato nelle opzioni dell'extension: [**Portale Tenant→ Extension**](../portale-tenant-cloud-pbx/service-2-2/extension-2-2.md) oppure all'interno del **Portale** [**Extension →Profile**](portale-extension-profile.md)**.**
- **Delete Voicemail after Emailing:** se abilitata, il messaggio viene cancellato dalla memoria del PBX una volta inviata la mail.
- **Skip Greeting:** se abilitata, il messaggio di benvenuto non verrà riprodotto.
- **Skip Instruction:** se abilitata, le istruzioni per lasciare un messaggio non verranno riprodotte.
- **Skip Voicemail password:** di default per accedere alla propria voicemail (tramite codice componibile da tastiera del telefono **Portale Tenant → Feature Codes**) è necessario inserire una password (chiamata VM Password e configurabile qui: [**Portale Tenant→ Extension**](../portale-tenant-cloud-pbx/service-2-2/extension-2-2.md) oppure [**Portale Extension →Profile**](portale-extension-profile.md)), se questa opzione viene abilitata, non si necessita più dei questa password per accedere alla propria voicemail.
- **Deliver voicemail to:** se abilitata è possibile fa recapitare la mail con il messaggio anche ad un altro indirizzo mail.
- **Announce CallerID:** se abilitata, verrà annunciato anche il numero della persona che ha lasciato il messaggio nella voicemail.
- **Interrupt:** se abilitata, è possibile interrompere la voicemail premendo un pulsante qualsiasi di interrompere il processo di Voicemail e di instradare la chiamata verso un altro Service che verrà specificato nei form che appariranno all'abilitazione dell'opzione.
- **Greeting Settings:** l'utente dell'extension può configurare fino a 9 messaggi di benvenuto diversi oltre a quello di default. Per selezionare quale messaggio utilizzare, effettuare l'accesso alla voicemail dell'esxtension e seguire la voce guida.

### Voicemail Messages

Elenco dei messaggi lasciati nella Vociemail dell'extension. Da qui è inoltre possibile ascoltarli, scaricarli o eliminarli:

![](/kb-assets/b8a8a6fc2b-image2019-8-13-12-21-16.png)

  

  

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Descrizione dei vari sotto-menù](#descrizione-dei-vari-sotto-men)
-   [Voicemail Greetings](#voicemail-greetings)
-   [Voicemail Settings](#voicemail-settings)
-   [Voicemail Messages](#voicemail-messages)
* * *
**Articoli collegati**


- Page:
[Estendere volume Guest OS (Linux) senza riavviare](../../../openstack-as-a-service/how-to-openstack-as-a-service/estendere-volume-guest-os-linux-senza-riavviare.md)
- Page:
[Fax to Mail & Mail to Fax](../../../internet-e-fonia/fax-to-mail-and-mail-to-fax.md)
- Page:
[Impossibile chiamare o ricevere chiamate](../../troubleshoot-cloud-pbx/impossibile-chiamare-o-ricevere-chiamate.md)
- Page:
[Portale Extension - Profile](portale-extension-profile.md)
- Page:
[Portale Extension - Voicemail](portale-extension-voicemail.md)
:::