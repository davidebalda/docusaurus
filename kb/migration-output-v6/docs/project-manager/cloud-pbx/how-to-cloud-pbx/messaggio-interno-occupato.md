---
title: "Messaggio \"Interno occupato\""
---

## Introduzione {#introduzione}

Questa guida ha lo scopo di informare su come fare nel caso in cui un interno sia occupato ma si voglia comunque gestire le chiamate in ingresso dirette a quello specifico interno informando con un messaggio audio che l' utente è attualmente occupato

Prerequisiti

E' necessario registrare il messaggio audio in formato .wav o .mp3

## Guida passo-passo {#guida-passo-passo}

- Accedi al pannello di controllo CloudPBX [https://pbx.cloudfire.it](https://pbx.cloudfire.it/) ed effettua login con le tue credenziali.
- Nella sezione "Config" → "Prompt List" Clicca su "Add Prompt" per aggiungere il file audio  
  
![](/kb-assets/3e52cfcf14-image2019-8-1-14-43-8.png)
  
  
Compila i campi necessari alla creazione del file audio e seleziona il file in formato .wav o .mp3 con il pulsante "Select file"  
![](/kb-assets/3a91bacaad-image2019-8-1-14-44-3.png)
  
  
Spostati nella sezione "Service" → "Playback" per associare il file audio a una Playback Extension cliccando su pulsante "Add Playback Extension"  
  
![](/kb-assets/fe238d89db-image2019-8-1-14-53-16.png)
  
  
Compila i campi contrassegnati con \*, avendo cura di selezionare, come "Language" *Italiano*:  
![](/kb-assets/5899c13971-image2019-8-1-14-54-26.png)
  
  
- Configura la deviazione di chiamata o il messaggio audio appena caricato come destinazione di ciascun interno in caso di occupatoEntra nella sezione "Service" → "Extension" :![](/kb-assets/ca5a5c523b-image2019-8-1-14-50-29.png)
  
- Clicca sull' icona ![](/kb-assets/6d009c45b6-image2019-8-1-14-47-48.png)
 per accedere al pannello di gestione dell' internoNella sezione "Extension Settings" è possibile configurare l' azione che scatenerà la riproduzione del messaggio ![](/kb-assets/992412c1d0-image2019-8-1-15-0-13.png)

- "**Busy Forward Type**" è l'azione legata all'interno occupatoSelezionando "*Playback Extension*" verrà sbloccato il menu "Busy Forward" nel cui menù sarà possibile selezionare il file audioN.B. Occorre anche configurare la funzione "Call Waiting" su **OFF**

:::info
N.B. Occorre anche configurare la funzione "Call Waiting" su **OFF**
:::

![](/kb-assets/89f3cf079e-image2019-8-1-16-42-7.png)

  

  

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Guida passo-passo](#guida-passo-passo)
-   Filter by label
* * *
##### Filter by label {#filter-by-label}

There are no items with the selected labels at this time.
:::