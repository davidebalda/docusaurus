---
title: "Ring Group (2) (2)"
---

## Introduzione

Guida passo-passo per la configurazione di un Ring Group. I Ring Group sono quel service che vi permette di gestire una chiamata in arrivo e di instradarla verso un gruppo di extension con solo 2 strategie di squillo: o squillo contemporaneo di tutte le extension inserite oppure sequenziale.

Il ring group si defferenzia dalla coda per essere più statico (in quanto le extension inserite non hanno la possibilità di loggarsi e sloggarsi) ma anche più semplice (in quanto le opzioni disponibili sono minori).

## Prerequisiti

Una volta acquistato il servizio "Cloud PBX" su Cortex avrete accesso al "**Portale Tenant**" con le vostre credenziali.

## Guida passo-passo

- Dal **Portale Tenant** entrare nella sezione Queue tramite il menù **Service → Ring Group.**

![](/kb-assets/379681a3e2-image2019-8-9-11-49-38.png)

- Cliccare su **ADD RING GROUP**;
- Compilare i seguenti campi:

![](/kb-assets/d0630fb0f0-image2019-8-9-11-51-17.png)

#### Descrizione dei vari campi:

- **Name:** (obbligatorio) assegnare un nome univoco al Ring Group.
- **Extension:** (obbligatorio) assegnare un nome univoco che corrisponderà all'extension number del Ring Group.
- **Type:** (obbligatorio) scegliere la strategia di squillo:
-   **SIMULTANEOUS:** la chiamata in ingresso verrà inviata a tutte le extension inserite nel Ring Group facendole squillare contemporanemente.
-   **SEQUENTIAL:** la chiamata in ingresso verrà inviata a tutte le extension inserite nel Ring Group ma facendole squillare in modo sequenziale nell'ordine specificato nel modulo sottostante **Extension List.**
- **MOH:** musica d'attesa che verrà riprodotta dopo il **Welcome Prompt** fino a quando una delle extension non risponde.
- **Language:** Lingua del Ring Group, assicuratevi che sia la stessa dei Prompt o MOH che avete inserito in [**Config → Prompt List**](../config-2-2/prompt-list-2-2.md) e che intendete utilizzare in questo Ring Group.
- **Information Prompt:** messaggio sonoro che verrà riprodotto all'arrivo della chiamata nel Ring Group.
- **Timeout:** timeout in secondi che mantiene la chiamata in attesa all'interno del Ring Group, una volta superato considera la chiamata fallita.
- **On Fail Activity:** Se abilitato da la possibilità di instradare la chiamata verso altri service una volta che è considerata fallita.
-   **On Fail Activity Type:** tipo di service a cui instradare la chiamata fallita.
-   **On Fail Activity Number:** numero del servizio specificato nel punto sopra.
- **Recording:** Se abilitato, le chiamate arrivate e risposte da questo Ring Group vengono registrate.
- **Display Name in Caller ID:** se abilitato, alle extension inserite nel Ring Group, quando arriva una chiamata proveniente da questo Ring Group, viene inviato anche il **Name** del ring-group. Questa opzione è utile quando un'extension è inserita in più Ring Group diversi, in questo modo è possibile avere informazioni sulla chiamata prima di rispondere.
- **Call Feature:** da la possibilità di abilitare le funizonalità di chiamata, come per esempio Call Pickup, trasferimento etc...
- **Send Missed Call Notification:** se abilitata invierà un email di notifica sulle chiamate perse all'indirizzo specificato nel text box che apparirà.
- **Add Extension:** in questo modulo è possibile inserire le varie extension che faranno parte del Ring Group.
-   **Type:** selezionare **internal** se volete inserire un extension del PBX, selezionare invece **external** se volete inserire un numero telefonico esterno al PBX.
-   **Extension:** selezionare l'extension desiderata oppure il numero di telefono esterno desiderato.
- **Extension List:** qui viene mostrata l'elenco delle extension presenti nel Ring Group. In caso di **Type SEQUENTIAL,** è possibile trascinare le extension sopra o sotto le altre per cambiare l'ordine di risposta.

  

  

:::note
**Sommario**


- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Guida passo-passo](#guida-passo-passo)
-   [Descrizione dei vari campi:](#descrizione-dei-vari-campi)
* * *
**Articoli collegati**


- Page:
[Chiamate esterne da Ring Group o IVR non funzionanti](../../../troubleshoot-cloud-pbx/chiamate-esterne-da-ring-group-o-ivr-non-funzionanti.md)
- Page:
[Portale Extension - Opzioni e Funzionalità](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/1966256717/Portale+Extension+-+Opzioni+e+Funzionalit)
- Page:
[Ring Group (2) (2)](ring-group-2-2.md)
- Page:
[Dashboard](../dashboard.md)
- Page:
[CID Routing](../call-routing/cid-routing.md)
:::