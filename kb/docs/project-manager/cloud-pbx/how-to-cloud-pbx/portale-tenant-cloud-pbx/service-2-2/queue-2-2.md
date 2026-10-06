---
title: "Queue (2) (2)"
---

## Introduzione {#introduzione}

Guida passo-passo per la configurazione di una nuova coda all'interno del proprio Tenant. Le code sono quel service che vi permette di gestire l'arrivo di una chiamata e di instradarla verso le extension gestendone l'ordine di squillo e i messaggi che l'interlocutore sentirà mentre è in attesa.

Le code sono pensate per essere dinamiche garantendo la possibilità alle varie extension di potersi loggare e sloggare a piacimento attraverso dei particolari codici da comporre con il tastierino del proprio telefono.

## Prerequisiti {#prerequisiti}

Una volta acquistato il servizio "Cloud PBX" su Cortex avrete accesso al "**Portale Tenant**" con le vostre credenziali.

## Guida passo-passo {#guida-passo-passo}

- Dal **Portale Tenant** entrare nella sezione Queue tramite il menù **Service → Queue.**

![](/kb-assets/de6c844603-image2019-5-30-17-50-24.png)

- Cliccare su **Add Queue**
- Compilare i seguenti campi:

![](/kb-assets/96bd53b223-image2019-5-30-18-2-31.png)

#### Descrizione dei vari campi {#descrizione-dei-vari-campi}

- ***Name** : (obbligatorio) assegnare un nome univoco alla coda.*
- ***Extension** : (obbligatorio) assegnare un extension alla coda.*
- ***Stratergy** : (obbligatorio) Selezionare la modalità di squillo delle extension che compongono la coda:*
-   ***Ring All** : squillo contemporaneo di tutte le extension presenti nell’ elenco Agents.*
-   ***Top Down** : squillo delle extension presenti nell’ elenco Agents in ordine dalla prima in alto all’ ultima in basso.*
-   ***Longest Idle Agent** : squillo delle extension nell’ elenco Agents in ordine di maggiore idle time.*
-   ***Round Robin** : squillo sequenziale delle extension in Agents.*
-   ***Agent with Least Talk Time** : squillo delle extensions in Agents in ordine di tempo in conversazione minore.*
-   ***Agent with Fewest Call** : squillo delle extensions in Agents in ordine di minor chiamate risposte.*
-   ***Random** : squillo delle extensions in Agents casual.*
- ***MOH** : (obbligatorio) selezionare la MOH (Music On Hold – Musica d’ attesa).*
- ***Language** : (obbligatorio) selezionare la lingua.*
- ***Max Waiting Calls** : (obbligatorio) indicare il numero massimo di chiamate in attesa contemporanee in coda.*
- ***Timeout (Sec)** : (obbligatorio) indicare il timeout della permanenza in coda di ciascuna chiamata.*
- ***Wrap Up Time (Sec)** : (obbligatorio) Tempo di avvolgimento.*
- ***Recording** : On abilita la registrazione audio – Off disabilita la registrazione audio.*
- ***Auto Answer Agent Call** : On abilita l’ auto risposta – Off disabilita l’ auto risposta.*
- ***Exit Caller if No Agent Available** : On termina la coda se nessuna extensions risulta disponibile – Off mantiene le chiamate in coda anche se tutte le extension sono occupate.*
- ***Play Position On Enter** : On abilita la riproduzione della posizione nella coda – Off disabilita la funzione.*
- ***Play Position** : On riproduce la posizione della posizione nella coda – Off disabilita la funzione.*
- ***Display Name In Caller ID** : On abilita la visualizzazione del CID – Off disabilita la funzione.*
- ***Queue Auto Login** : On abilita le extensions a far parte della coda automaticamente – Off occorre digitare il Feature Code per entrare nella coda.*
- ***Call Feature** : On abilita le Call Feature – Off disabilita la funzione.*
- ***On Fail Activity** : On permette di specificare dove instradare la chiama in caso di fail della coda – Off disabilita la funzione.*
- ***Send Missed Call Notification** : On abilita l’ invio di mail in caso di mancata risposta alla chiamata presente in coda – Off disabilita la funzione.*
- ***Agents** : spostare le extensions dalla colonna di sinistra (disponibili) alla colonna di destra (nella coda).*

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Guida passo-passo](#guida-passo-passo)
-   [Descrizione dei vari campi](#descrizione-dei-vari-campi)
* * *
**Articoli collegati**


- Page:
[Estendere volume Guest OS (Linux) senza riavviare](../../../../openstack-as-a-service/how-to-openstack-as-a-service/estendere-volume-guest-os-linux-senza-riavviare.md)
- Page:
[Impossibile chiamare o ricevere chiamate](../../../troubleshoot-cloud-pbx/impossibile-chiamare-o-ricevere-chiamate.md)
- Page:
[Portale Extension - Profile](../../portale-extension/portale-extension-profile.md)
- Page:
[Portale Extension - Voicemail](../../portale-extension/portale-extension-voicemail.md)
- Page:
[Accesso Portale Extension](../../portale-extension/accesso-portale-extension.md)
:::