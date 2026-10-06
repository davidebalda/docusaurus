---
title: "Time Condition (2) (2)"
---

## Introduzione {#introduzione}

In questo sotto-menù avete la possibilità di creare le **regole temporali**, che andrete poi ad applicare alle vostre numerazioni per poter gestire l'instradamento delle chiamate in base a particolari finestre temporali.

## Prerequisiti {#prerequisiti}

Una volta acquistato il servizio "Cloud PBX" su Cortex avrete accesso al "**Portale Tenant**" con le vostre credenziali.

## Guida passo-passo {#guida-passo-passo}

- Dal **Portale Tenant** entrate nella sezione Time Condition tramite il menù **Timing → Time Condition**

![](/kb-assets/67d0f8ea06-image2019-6-5-9-34-53.png)

- Una volta all'interno della dashboard delle **Time Condition** potrete vedere le regole già create e modificarle cliccando sul tasto Verde o eliminarle con il tasto Rosso
- Per creare una nuova **Time Condition** cliccate su **Add Time Condition** e vi si aprirà il form di gestione della nuova regola:  
![](/kb-assets/398f39b7d5-image2019-6-5-9-39-37.png)

Di seguito la descrizione dei vari campi:

- **Name:** campo obbligatorio, inserire un nome univoco per la seguente regola
- **Description:** campo non obbligatorio, inserire un descrizione per la regola
- **Start Time:** orario di inizio della finestra temporale che volete definire.
- **End Time:** orario di fine della finestra temporale che volete definire.
- **Start Day:** giorno della settimana di inizio della finestra temporale che volete definire.
- **End Day:** giorno della settimana di fine della finestra temporale che volete definire.
- **Start Date:** giorno del mese di inizio della finestra temporale che volete definire.
- **End Date:** giorno del mese di fine della finestra temporale che volete definire.
- **Start Month:** mese dell'anno di inizio della finestra temporale che volete definire.
- **End Month:** mese dell'anno di fine della finestra temporale che volete definire.

## Esempi {#esempi}

Di seguito alcuni esempi di **Time Condition** comunemente utilizzati

- Finestre temporali che definiscono la normale apertura degli uffici:  
![](/kb-assets/9e8964eb70-image2019-6-5-9-49-36.png)
  
![](/kb-assets/5b9010067d-image2019-6-5-9-50-5.png)

:::warning
Come vedete sono state create 2 regole (una per la mattina e una per il pomeriggio)
:::

- Finestra temporale che definisce la chiusura per ferie natalizie:  
![](/kb-assets/f8a23cf97f-image2019-6-5-9-53-5.png)

## Grafico Gestione dei timing {#grafico-gestione-dei-timing}

La decisione se il giorno odierno è compreso nella finestra temporale indicata, viene fatta seguendo gli step del grafico sottostante.

Per questo, se dovete indicare delle finestre temporali che coinvolgono più mesi, è meglio dividere le finestre temporali in base ai mesi che esse devono coprire, per evitare che in alcuni giorni la regola non venga metchata correttamente.

![](/kb-assets/69822c4bff-time-cond-fc.png)

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Guida passo-passo](#guida-passo-passo)
- [Esempi](#esempi)
- [Grafico Gestione dei timing](#grafico-gestione-dei-timing)
* * *
**Articoli collegati**


- Page:
[Time Condition (2) (2)](time-condition-2-2.md)
- Page:
[CID Routing](../call-routing/cid-routing.md)
- Page:
[DID Routing](../call-routing/did-routing.md)
- Page:
[Primi passi - Cloud PBX](../../../primi-passi-cloud-pbx.md)
:::