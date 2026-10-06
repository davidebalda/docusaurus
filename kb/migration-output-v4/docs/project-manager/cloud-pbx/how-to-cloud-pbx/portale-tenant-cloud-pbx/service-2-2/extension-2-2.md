---
title: "Extension (2) (2)"
---

## Introduzione

Guida passo-passo per la configurazione di una nuova extension all'interno del proprio Tenant

## Prerequisiti

Una volta acquistato il servizio "Cloud PBX" su Cortex avrete accesso al "**Portale Tenant**" con le vostre credenziali.

## Guida passo-passo

- Dal **Portale Tenant** entrare nella sezione extension tramite il menù **Service→Extension.**

![](/kb-assets/5483562d83-image2019-1-22-12-10-45.png)

- Cliccare su "**Add Extension**"

![](/kb-assets/292f2312e2-image2019-3-4-11-38-30.png)

- Compilare i seguenti campi:

![](/kb-assets/d1dea48175-image2019-3-4-12-6-32.png)

#### Descrizione dei vari campi:

- **Plan:** campo obbligatorio ed va ad indicare tutte le funzionalità disponibili per l'extension in creazione. Il plan **Default** comprende tutte le funzionalità disponibili.
- **Status:** flag che indica se l'extension è attiva o meno (non può essere disabilitata se inserita in un altro **Service**)
- **Type:** campo obbligatorio, qui è possibile indicare se creare una singola extension (**Number**) o un una serie di Extension (**Range**).
- **Extension Number:** Se nel **Type** si è selezionato **Number** inserire il numero dell'extension, vice-versa, se si è selezionato **Range,** compariranno 2 campi da riempire indicando i numeri delle serie di extension da creare.
- **Shift:** specifica quale shift (funzionalità creata all'interno del menù **Timing→**[**Shift**](../timing/shift-2-2.md)) da applicare all'extension. L'extension sarà raggiungibile solo negli orari indicati nello **Shift** selezionato. Le chiamate che arriveranno fuori dal periodo dello **Shift** indicato verranno gestite in base a ciò che è stato indicato nell'opzione **Shift Forward** (portale Extension→Extension Settings), se in questa opzione non è specificato nulla la chiamata arriverà comunque all'extension.
- **Extension Name:** Il campo viene compilato di default come: "uguale al numero dell'extension", ma può essere modificato con un nome o un numero a piacimento.
- **Group:** campo obbligatorio. Indica in quale gruppo verrà inserita l'extension. I membri dello stesso gruppo possono effettuare il call pick-up solo all'interno del gruppo stesso.
- **Phonebook Entry:** Se abilitato, l'extension verrà inserita nella rubrica condivisa del CloudPBX.
- **Langauge:** indica la lingua con cui verranno riprodotti i vari prompt a questa extension.
- **Web Password:** Password d'accesso al portale Extension (Non può essere più lunga di 12 caratteri e non può contenere caratteri speciali).
- **Email:** indirizzo mail che verrà usato in caso di password dimentica (portale extension), dove verranno recapitate le mail in caso vengano lasciati delle voicemail ed eventualmente i fax ricevuti.
- **Timezone:** indicare la timezone con cui volete che venga visualizzato l'orario nel vostro portale extension
- **Balance restriction:** da abilitare se si vogliono applicare delle restrizioni sul traffico telefonico per quell'extension. Da non abilitare in quanto il billing delle chiamate non viene effettuato tramite il CloudPBX.
- **Caller ID Name:** Nome che verrà mostrato come "ID chiamante", alle persone che verranno chiamate da questa extension. Questo nome ha priorità minore rispetto a quello salvato nella rubrica del CloudPbx. Questo nome verrà visualizzato solo nel caso l'extension non sia salvata in rubrica. Per le chiamate in uscita questa impostazione verrà utilizzata come terza scelta. Se il caller ID non è stato impostato ne in questo campo ne nel profilo del tenant, allora verrà utilizzato quello indicato nel **External Caller ID Number.**
- **Simultaneous Extenal Call:** numero massimo di chiamate in uscita che può fare questa extension (il valore 0 significa infinito).
- **SIP Password:** password per la registrazione SIP.
- **Feature PIN Code:** pin da utilizzare in alcune delle funzionalità abilitabili con i codici direttamente dall'apparato telefonico.
- **Ring Timeout:** definisce il tempo di durata degli squilli prima che la chiamata verso questa extension venga considerata non risposta.
- **Dial Timout:** definisce il tempo massimo di durata degli squilli prima che la chiamata effettuata da questa extension venga considerata non risposta.
- **Extension Auto Recording:** campo non obbligatorio. Selezionare quali chiamate vengono automaticamente registrate: chiamate interne, esterne o tutte.
- **External Caller ID Number:** quando questa extension effettua una chiamata in uscita, al chiamante, verrà mostrato questo numero. Questo ID ha priorità solo sull' ID specificato nella regola applicata nel campo "**Dial Rule Group".** Se questo campo non viene specificato allora la chiamata effettuata dall'extension presenterà come caller-id quello specificato nella "**Dial Rule Group**".
- **Multiple Registration:** se abilitato permette la registrazione di questa extension su più dispositivi.
- **Video Calling:** abilita la possibilità di effettuare video-chiamate per questa extension.
- **Audio and Video Codecs:** Lista dei codec disponibili per questa extension. Spostare dall'elenco di sinistra a quello di destra i codec che si desidera utilizzare:
1.   **Audio:** al momento gli unici 2 codec supportati sono: G729 e PCMA, da configurare come indicato nella figura sopra.
2.   **Video:**  video chiamata al momento non ancora supportata. 
- **Dial-out:** abilità la possibilità di effettuare chiamate in uscita per questa extension.
- **Dial Rule Group:** seleziona la regola per le chiamate in uscita. 
- **Allow all Prefixes:** abilita la possibilità di chiamare in uscita verso tutti i prefissi internazionali.
- **Allow Prefix:** se la precedente opzione è disabilitata permette di inserire i prefissi internazionali verso l'extension può effettuare chiamate.
- **Voicemail:** abilita o disabilita la voicemail
- **VM Password:** password d'accesso alla voicemail di questa extension.
- **FAX:** abilita la possibilità, per questa extension, di inviare e ricevere Fax (Guida FaxToMail).
- **FAX Header:** abilita la possibilità di aggiungere un header ai fax in uscita.
- **Fax Cover Page:** abilita la possibilità di impostare una copertina ad ogni fax inviato.
- **Fax From Company:** inserire la dicitura da inserire nella copertina del Fax.
- **Fax on Mail:** abilità la possibilità di ricevere i fax via mail.