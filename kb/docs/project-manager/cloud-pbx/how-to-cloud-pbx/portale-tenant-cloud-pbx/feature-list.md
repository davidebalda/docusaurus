---
title: "Feature List"
---

## Introduzione {#introduzione}

Questo sotto menù contiene l'elenco dei codici componibili dal tastierino numerico del proprio telefono che permettono di attivare e disattivare diverse funzionalità legate alla propria extension, come deviazioni, login/logout dalle code, trasferimenti etc.

## Prerequisiti {#prerequisiti}

Alcuni di questi codici per poter essere utilizzati necessitano dell'abilitazione della relativa opzione. Di seguito per ogni codice ne verrà spiegato il funzionamento e anche i prerequisiti per utilizzarlo.

## Elenco di Codici {#elenco-di-codici}

|     |     |     |
| --- | --- | --- |
| ### **Funzionalità** | ### **Codice di Attivazione** | ### **Utilizzo** |
| **Trasferimento cieco** | **\*1** | Durante una chiamata è possibile comporre il codice *\*1,* dopo la voce guida, inserire l’extension (o numero di telefono esterno) di destinazione seguito dal tasto *#* per eseguire il trasferimento cieco della chiamata verso la numerazione inserita<br><br>> [!INFO]<br>> Per poter usare questo codice, deve essere abilitata l’opzione ***Transfer*** (*Portale Extension → Extension Settings)* |
| **Trasferimento con attesa** | **\*4** | Durante una chiamata è possibile comporre il codice *\*4* dopo la voce guida, inserire l'extension (o un numero di telefono esterno) di destinazione seguito dal tasto **#** per eseguire il trasferimento con attesa della chiamata verso la numerazione inserita.<br><br>> [!INFO]<br>> Per poter usare questo codice deve essere abilitata l’opzione ***Transfer*** (*Portale Extension → Extension Settings)* |
| **Conferenza a 3** | **0** | Dopo aver effettuato un trasferimento con attesa *(\*4)*, premendo il tasto *0* è possibile fare una conferenza a tre tra voi, l'utente in attesa e il destinatario del trasferimento.<br><br>> [!INFO]<br>> Per poter usare questo codice deve essere abilitata l’opzione ***Transfer*** (*Portale Extension → Extension Settings)* |
| **Registrazione di un Busy Callback** | **0** | Durante una chiamata in attesa in una coda premere il tasto *0* per registrare la chiamata che vi arriva da un Busy Callback. |
| **Call Recording** | **\*6** | Se abilitata la corrispettiva opzione all'interno del menù <br><br>*Portale Extension → Extension Settings* durante una chiamata potete comporre questo codice per registrarla (una volta composto il codice verrete avvisati da un segnale acustico). |
| **Call Park** | **\*5** | Se abilitata la corrispettiva opzione all'interno del del menù *Portale Extension → Extension Settings* durante una chiamata potete comporre questo codice per mettere in attesa l'interlocutore (una volta composto il codice verrete avvisati da un segnale acustico). |
| **DTMF** | **\*7** | Se abilitata la corrispettiva opzione all'interno del del menù *Portale Extension → Extension Settings* durante una chiamata potete comporre questo codice per mettere in attesa l'interlocutore e rendere completamente libero il vosrto apparato, infatti dopo aver composto questo codice, una voce registrata vi comunicherà il codice assegnato (**Parking lot number**) alla chiamata per poter riprendere la conversazione. |
| **Call Pickup** | **\*77** | Questo pickup è direttamente conseguente al punto precedente; componendo *\*77* seguito dal codice assegnato alla chiamata potrete riprendere l'interlocutore messo in attesa con il codice *\*7* |
| **Call Pickup from User Defined Slot** | **\*76** | Questo pickup è similare a quello del punto precedente ma eseguibile anche da un extension che non ha messo direttamente in attesa l'interlocutore. A patto che questa extension conosca i codici assegnati al parking (**Parking lot number**).<br><br>> [!NOTE]<br>> - **Per Parking Lot del Tenant:** \*76`<parking lot numer>`<br>> - **Per Parking Lot dell’Extension:** \*76`<numero dell'extension che ha messo in attesa la chiamata>``<parking lot number>` |
| **Ringing Extension Pickup** | **\*88** | Pickup di una chiamata destinata ad un'altra extension. Nel classico caso in cui al vostro collega suona l'interno ma lui non può rispondere, voi potete comporre questo codice, seguito dal numero dell'extension del collega, per rispondere alla chiamata in arrivo al suo telefono.<br><br>> [!INFO]<br>> Per utilizzarlo, digitare **\*88`<numero dell’extension>`** |
| **Ringing Sip Extension Pickup** | **\*81** | Funzionamento similare alla precedente con la possibilità di rispondere a chiamate destinate ad extension registrate su altri tenant.<br><br>> [!INFO]<br>> Per utilizzarlo, digitare: **\*81`<Tenant ID>``<numero dell'extension>`** |
| **Ringing Extension Pickup from Group** | **\*8** | Pickup di qualsiasi chiamata destinata ad una o più extension inserita nello stesso gruppo *(Portale Tenant → Extension)* di quella che compone questo codice. |
| **Voicemail Access** | **\*\*** | Codice da utilizzare per poter accedere alla *Voice Mail* dell'extension registrata sul telefono da cui componete il codice |
| **Voicemail Remotely** | **\*99** | Codice da utilizzare per poter accedere alla Voice Mail di un'extension se il telefono da cui componete il codice non è quello con l'extension registrata di cui volete controllare la Voice Mail<br><br>> [!INFO]<br>> Per utilizzarlo, digitare: **\*99`<numero dell’extension>`** |
| **Direct Voicemail** | **\*82** | Codice da utilizzare se volete lasciare un messaggio direttamente alla mail di una data extension.<br><br>> [!INFO]<br>> Per utilizzarlo, digitare: **\*82`<numero dell'extension>`** |
| **Call to Last Dialed Number** | **\*73** | Codice da utilizzare se volete ricomporre l'ultimo numero che avete composto |
| **Call to Last Received Number** | **\*94** | Codice da utilizzare se volete comporre un numero ricercando il nome del contatto nella rubrica. Una volta composto questo codice e fatto partire la chiamata una voce guida vi indicherà come effettuare la ricerca in rubrica |
| **Barge-In Extension** | **\*79** | Se abilitata la corrispettiva opzione all'interno del menù *Portale Extension → Extension Settings,* utilizzando questo codice, potrete inserirvi nella conversazione in atto dell'extension inserita (sia l'extension che inserite che l’interlocutore vi potranno sentire.<br><br>> [!INFO]<br>> Per utilizzarlo, digitare: **\*79<numero dell'extension** |
| **Whisper Extension** | **\*65** | Se abilitata la corrispettiva opzione all'interno del menù *Portale Extension → Extension Settings,* utilizzando questo codice potrete inserirvi nella conversazione in atto dell'extension inserita (solo l'extension inserita potrà sentire ciò che direte).<br><br>> [!INFO]<br>> Per utilizzarlo, digitare: **\*65`<numero dell'extension>`** |
| **Break Out** | **\*45** | Codice che *disabilita* il "break" per l’extension. Il Break è una sorta di "vado in pausa", se abilitata, l'extension non riceverà nessuna chiamata da nessuna coda. Questa opzione viene abilitata sull'extension, quindi anche rimuovendo e reinserendo l’extension questa opzione rimarrà attiva fino alla sua disabilitazione tramite questo feature code. |
| **Break In** | **\*44** | Codice che abilita il "break" per l’extension. Il Break è una sorta di "vado in pausa", se abilitata, l'extension non riceverà nessuna chiamata da nessuna coda. Questa opzione viene abilitata sull'extension, quindi anche rimuovendo e reinserendo l’extension questa opzione rimarrà attiva fino alla sua disabilitazione tramite il feature code precedente |
| **Queue Login** | **\*11** | Codice da utilizzare se si vuole che l'extension venga inserita nel gruppo degli agenti di una coda.<br><br>> [!NOTE]<br>> - **\*11`<numero della coda>`:** Per entrare in una coda specifica;<br>> - **11\*:** Per entrare in tutte le code del Tenant; |
| **Queue Logout** | **\*12** | Codice da utilizzare se si vuole che l'extension venga tolta dal gruppo degli agenti di una coda.<br><br>> [!NOTE]<br>> - **\*12`<numero della coda>`:** Per uscire da una coda specifica;<br>> - **\*12:** per uscire da tutte le code del Tenant. |
| **External Call Lock** | **\*95** | Codice da utilizzare se si vuole inibire un'extension dall'effettuare chiamate verso l'esterno. Rimarrà comunque la possibilità di effettuare chiamate interne. Componendo il codice una voce guida vi chiederà il *PIN dell'extension* per abilitare il blocco.<br><br>> [!INFO]<br>> Per disabilitare il blocco ripetere il codice e reinserire il PIN. |
| **Extension DND Setting** | **\*92** | Codice da utilizzare per entrare nel menù di configurazione del **Do Not Disturb.**<br><br>> [!INFO]<br>> Per utilizzarlo, digitare: **\*92`<PIN dell'extension>`** |
| **Extension DND Setting** | **\*97** | Codice da utilizzare per abilitare il **Do Not Distrub.**<br><br>> [!INFO]<br>> Per utilizzarlo, digitare: **\*97`<PIN dell'extension>`** |
| **Disable Extension DND** | **\*98** | Codice da utilizzare per disabilitare il **Do Not Disturb.**<br><br>> [!INFO]<br>> Per utilizzarlo, digitare: **\*98`<PIN dell'extension>`** |
| **Extension Universal Forward Setting** | **\*91** | Codice da utilizzare per abilitare la deviazione di chiamata fissa per l'extension.<br><br>> [!INFO]<br>> Per utilizzarlo, digitare: **\*91`<PIN dell'extension>`\*`<DESTINATION>`**<br><br>> [!NOTE]<br>> Il campo **DESTINATION** Può assumere i seguenti valori:<br>> - **1:** le chiamate verranno deviate alla **Voicemail** dell'extension<br>> - **2:** disabilita la deviazione.<br>> - **Extension Number:** le chiamate verranno deviate verso l'extension qui specificata (da inserire nel formato **TenantID+Extension Number,** es. "1111502", tenant 1111 extension 502).<br>> - **External Numer:** le chiamate verranno deviate verso il numero di telefono esterno qui specificato. |
| **Tenant ID Routing Setting:** | **\*93** | Codice da utilizzare se si vuole modificare la destinazione di una chiamata diretta ad un particolare DID del vostro Cloud PBX. Questa opzione fa in modo che la chiamata venga deviata verso una delle **Inbound Rule** già assegnate ad un DID (*Portale Tenant → DID Routing),* specificandone nel codice stesso il codice di priorità, per cui si necessita di una conoscenza delle regole create.<br><br>> [!INFO]<br>> Per utilizzarlo, digitare: **\*93`<PIN del Tenant>`\*`<DID>`\*`<Codice di priorità della regola>`** |
| **Dial Number Anonimously** | **\*70** | Codice da utilizzare se si vuole chiamare un numero nascondendo il proprio *CallerID*.<br><br>> [!INFO]<br>> Per utilizzarlo, digitare: **\*70`<numero>`** |
| **Call Screening Enable/Disable** | **\*71** | Codice da utilizzare per abilitare o disabilitare il **Call Screening** (*Portale Extension → Extension Settings*) |

  

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Elenco di Codici](#elenco-di-codici)
-   [Funzionalità](#elenco-di-codici)
-   [Codice di Attivazione](#elenco-di-codici)
-   [Utilizzo](#elenco-di-codici)
* * *
**Articoli collegati**


- Page:
[Estendere volume Guest OS (Linux) senza riavviare](../../../openstack-as-a-service/how-to-openstack-as-a-service/estendere-volume-guest-os-linux-senza-riavviare.md)
- Page:
[Impossibile chiamare o ricevere chiamate](../../troubleshoot-cloud-pbx/impossibile-chiamare-o-ricevere-chiamate.md)
- Page:
[Portale Extension - Profile](../portale-extension/portale-extension-profile.md)
- Page:
[Portale Extension - Voicemail](../portale-extension/portale-extension-voicemail.md)
- Page:
[Accesso Portale Extension](../portale-extension/accesso-portale-extension.md)
:::