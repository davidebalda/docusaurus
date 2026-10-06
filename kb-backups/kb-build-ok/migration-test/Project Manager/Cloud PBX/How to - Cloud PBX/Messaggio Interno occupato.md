## Introduzione

Questa guida ha lo scopo di informare su come fare nel caso in cui un interno sia occupato ma si voglia comunque gestire le chiamate in ingresso dirette a quello specifico interno informando con un messaggio audio che l' utente è attualmente occupato

Prerequisiti

E' necessario registrare il messaggio audio in formato .wav o .mp3

## Guida passo-passo

- Accedi al pannello di controllo CloudPBX [https://pbx.cloudfire.it](https://pbx.cloudfire.it/) ed effettua login con le tue credenziali.
- Nella sezione "Config" → "Prompt List" Clicca su "Add Prompt" per aggiungere il file audio  
  
![](./attachments/image2019-8-1_14-43-8.png)
  
  
Compila i campi necessari alla creazione del file audio e seleziona il file in formato .wav o .mp3 con il pulsante "Select file"  
![](./attachments/image2019-8-1_14-44-3.png)
  
  
Spostati nella sezione "Service" → "Playback" per associare il file audio a una Playback Extension cliccando su pulsante "Add Playback Extension"  
  
![](./attachments/image2019-8-1_14-53-16.png)
  
  
Compila i campi contrassegnati con \*, avendo cura di selezionare, come "Language" *Italiano*:  
![](./attachments/image2019-8-1_14-54-26.png)
  
  
- Configura la deviazione di chiamata o il messaggio audio appena caricato come destinazione di ciascun interno in caso di occupatoEntra nella sezione "Service" → "Extension" :![](./attachments/image2019-8-1_14-50-29.png)
  
- Clicca sull' icona ![](./attachments/image2019-8-1_14-47-48.png)
 per accedere al pannello di gestione dell' internoNella sezione "Extension Settings" è possibile configurare l' azione che scatenerà la riproduzione del messaggio ![](./attachments/image2019-8-1_15-0-13.png)

- "**Busy Forward Type**" è l'azione legata all'interno occupatoSelezionando "*Playback Extension*" verrà sbloccato il menu "Busy Forward" nel cui menù sarà possibile selezionare il file audioN.B. Occorre anche configurare la funzione "Call Waiting" su **OFF**

> [!INFO]
> N.B. Occorre anche configurare la funzione "Call Waiting" su **OFF**

![](./attachments/image2019-8-1_16-42-7.png)

  

  

> [!NOTE]
> **Sommario**
> 
> 
> 
> - [Introduzione](#introduzione)
> - [Guida passo-passo](#guida-passo-passo)
> -   Filter by label
> * * *
> ##### Filter by label
> 
> There are no items with the selected labels at this time.