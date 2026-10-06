---
title: "IVR (2) (2)"
---

## Introduzione {#introduzione}

Guida passo-passo per la configurazione di un nuovo IVR. Un IVR è un classico risponditore automatico che gestisce l'instradamento delle chiamate in ingresso verso altri Service tramite selezione con il tastierino numerico del telefono.

## Prerequisiti {#prerequisiti}

Una volta acquistato il servizio "Cloud PBX" su Cortex avrete accesso al "**Portale Tenant**" con le vostre credenziali.

## Guida passo-passo {#guida-passo-passo}

- Dal **Portale Tenant** entrare nella sezione IVR tramite il menù **Service → IVR**

![](/kb-assets/e4dcc73612-image2019-8-9-10-18-39.png)

- Cliccare su **ADD IVR**:
- Compilare i campi che vengono visualizzati:

![](/kb-assets/cc8ea48f71-image2019-8-9-10-19-58.png)

#### Descrizione dei vari campi {#descrizione-dei-vari-campi}

- **Name:** (obbligatorio) assegnare un nome univoco all'IVR.
- **Extension:** (obbligatorio) assegnare un numero che corrisponde all'extension number dell'IVR.
- **Language:** (obbligatorio) assegnare una lingua, assicuratevi che sia la stessa assegnata ai vari prompt che avete inserito in [**Config → Prompt List**](../config-2-2/prompt-list-2-2.md)
- **Welcome Prompt:** (obbligatorio) messaggio sonoro che verrà riprodotto all'arrivo della chiamata.
- **Repeat Prompt:** messaggio sonoro che verrà riprodotto a seguito del **Welcome Prompt** se non viene effettuata nessuna selezione con il tastierino numerico.
- **Invalid Prompt:** messaggio sonoro che verrà riprodotto se viene inserita una selezione non configurata.
- **Timeout Prompt:** messaggio vocale che verrà riprodotto al superamento del **Digit Timeout.**
- **Exit Prompt:** messaggio vocale che verrà riprodotto quando il chiamante esce dall'IVR.
- **Digit Timeout(sec):** (obbligatorio)timeout in millisecondi in cui il chiamante ha tempo di inserire la selezione. Se viene superato verrà riprodotto il **Timeout prompt.**
- **Inter-digit Timeout(sec):** (obbligatorio) Se è abilitata la funzione **Direct Extension Call**, è il timeout in secondi per l'inserimento dell'intero numero. Se superato verrà composto solo la cifra composta fino a quel momento.
- **Max Timeout Try(sec):** (obbligatorio)timeout tra un tentativo errato ed un altro. 
- **Max Invalid Try:** (obbligatorio) numero massimo di tentativi possibili.
- **IVR digit Lenght:** definire la quantità di cifre della selezione.
- **Direct Extension Call:** se abilitato è possibile selezionare con il tastierino numerico direttamente l'extension desiderata.

Una volta cliccato su **CREATE** verrete mandati sulla pagina di configurazione del vostro IVR:

![](/kb-assets/e03586934f-image2019-8-9-11-21-5.png)

Nello specchietto in alto potete vedere l'alberatura dell'IVR, in modo da avere una visione chiara di come sono state impostate le varie selezioni e, nel caso vengano annidati diversi IVR è possibile ricomporre facilmente come vengono instradate le chiamate.

Subito di fianco avete le impostazioni configurate nel precedente form che volendo possono essere modificate.

Nella parte sottostante invece è presente la configurazione della selezione numerica.

La colonna **Digit** indica il numero che il chiamante compone sul suo tastierino numerico e di conseguenza tramite i menù a tendina in corrispondenza delle colonne **Action** e **Value** il servizio verso cui instradare la chiamata quando viene premuto quel numero.

:::note
Di seguito la spiegazione degli ultimi 2 digit che sono **"i"** e **"t"**
- **"i"**: sta per "invalid" e va ad indicare verso quale Service instradare la chiamate se il chiamante effettua un numero di tentativi sbagliato superiore al valore indicato nel campo **Max Invalid Try**
- **"t":** sta per "timeout" e va ad indicare verso quale Service instradare la quando viene superato il timeout indicato nel campo: **Max Timeout Try.**
:::

  

  

:::note
**Sommario**


- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Guida passo-passo](#guida-passo-passo)
-   [Descrizione dei vari campi](#descrizione-dei-vari-campi)
* * *
**Articoli collegati**


- Page:
[Chiamate esterne da Ring Group o IVR non funzionanti](../../../troubleshoot-cloud-pbx/chiamate-esterne-da-ring-group-o-ivr-non-funzionanti.md)
- Page:
[Portale Extension - Opzioni e Funzionalità](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/1966256717/Portale+Extension+-+Opzioni+e+Funzionalit)
- Page:
[IVR (2) (2)](ivr-2-2.md)
- Page:
[Dashboard](../dashboard.md)
- Page:
[CID Routing](../call-routing/cid-routing.md)
:::