---
title: "Cloud Connect - Veeam Cloud Platform"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina spiega come attivare Cloud Connect di Veeam Cloud Platform.

**Cloud Connect** è la funzionalità che, all’interno di Veeam Cloud Platform, è vincolante per l’attivazione delle restanti funzionalità.

:::note
Cloud Connect è una funzionalità **gratuita** ed è necessaria per creare un’istanza in una determinata Region, pronta a contenere tutte le altre funzionalità del servizio.

[!TIP]
É possibile attivare più **Cloud Connect** all’interno del medesimo progetto se ogni Cloud Connect attivato presenta una Region diversa.
:::

Una volta attivata e definita la sezione Cloud Connect infatti, puoi attivare:

# Accedi Cloud Connect

Per accedere a Cloud Connect è sufficiente seguire i seguenti passaggi:

1. Accedi al servizio **Veeam Cloud Platform**. Non sai come fare? Segui la nostra [**guida**](../index.md)**.**
2. Seleziona la voce **Cloud Connect** tra le tab in alto;

![Screenshot 2024-05-13 at 16.19.43.png](/kb-assets/2ddec52ca8-screenshot-2024-05-13-at-16-19-43.png)

# Attiva Cloud Connect

Per attivare Cloud Connect è sufficiente seguire i seguenti passaggi:

1. Accedi alla voce **Cloud Connect** del servizio **Veeam Cloud Platform** dalle tab in alto;
2. Premi il bottone **Attiva Cloud Connect** nell’Overview;
3. Seleziona la **Region** in cui vuoi attivare Cloud Connect e tutte le altre funzionalità. La region scelta indica la regione geografica in cui sono archiviati tutti i dati relativi ai backup dei dispositivi.
4. Imposta la **password** di accesso a Veeam Cloud Connect.
5. Premi il bottone **Attiva Cloud Connect**.

:::note
Lo username, necessario per Accedere alla *Veeam Service Provider Console*, viene generato automaticamente.

[!WARNING]
**Per motivi di sicurezza** la Password non verrà più mostrata successivamente alla creazione. Ti consigliamo di salvarla ora e conservarla in un posto sicuro.
Inoltre, in Veeam Cloud Platform la delle password è centralizzata, viene quindi utilizzata la stessa Password per **Veeam Cloud Connect** e **Veeam Service Provider Console**.

[!INFO]
La procedura di attivazione può impiegare fino a **2 minuti** per essere completata. Se trascorso questo tempo Veeam Cloud Connect non risulta ancora attivo ti invitiamo ad aprire un [**Case**](../../../../account-manager/supporto/index.md) al nostro supporto.
:::

![Screenshot 2024-05-13 at 16.21.30.png](/kb-assets/b9e6b9d238-screenshot-2024-05-13-at-16-21-30.png)

# Crea e Attiva un Cloud Connect in un’altra region

Per creare un nuovo Cloud Connect nello stesso progetto, ma con una **region differente** è necessario seguire questi passaggi:

1. Accedi alla voce **Cloud Connect** del servizio **Veeam Cloud Platform** dalla tab
2. Accedi alla voce **Accesso** dal menù a tendina nelle tab;
3. Premi il selettore della **Region** in alto a destra e seleziona la nuova region. É possibile attivare solamente le region non ancora attive che hanno lo stato in **grigio**;
4. Segui nuovamente la procedura di attivazione di Cloud Connect seguendo questa [**guida**](https://cloudfireit.atlassian.net/wiki/spaces/~239475519/pages/2424701078/Bozza+-+Cloud+Connect+-+Veeam+Cloud+Platform#Attiva-Cloud-Connect).

:::tip
Una volta completata la procedura la nuova region presenterà lo stato **verde**.
:::

## Visualizzare le Region attive

Per visualizzare le Region in cui è attivo il Cloud Connect nello stesso progetto è sufficiente seguire questi passaggi:

1. Accedi alla voce **Cloud Connect** del servizio **Veeam Cloud Platform** dalle tab in alto;
2. Seleziona la voce **Accesso** dal menù a tendina;
3. Premi il selettore della **Region** in alto a destra e seleziona la region che ti interessa.

![Screenshot 2024-05-13 at 17.13.46.png](/kb-assets/d7a6529cd2-screenshot-2024-05-13-at-17-13-46.png)

# Azioni disponibili

Una volta completata la procedura di attivazione del Veeam Cloud Connect sono disponibili diverse azioni.

## Collega Veeam Cloud Connect

Per predisporre uno spazio di archiviazione per backup scalabile e sicuro nella nostra repository in Cloud è necessario collegare il **Veeam Cloud Connect.**

Per collegare Veeam Cloud Connect è necessario accedere alla voce **Accesso** della tab Cloud Connect e seguire questa [**guida**](index.md#Accedi--Cloud-Connect).

## Accedi alla Service Provider Console

**Accedere** a **Veeam Service Provider Console** permette di usufruire di una piattaforma di controllo web dal quale è possibile amministrare le diverse operazioni del servizio.

Una volta collegato, puoi accedere alla Veeam Service Provider Console da più sezioni:

- Premi il bottone Service Provider Console presente in alto;
- Raggiungi la tab **Veeam Service Provider Console** e premi il bottone **Accedi.**

![Screenshot 2024-05-13 at 16.31.38.png](/kb-assets/f7f2cd98a8-screenshot-2024-05-13-at-16-31-38.png)

## Accedi alle Impostazioni Veeam Cloud Connect

Dalla sezione impostazioni di Cloud Connect puoi reimpostare la password e abilitare l’accesso REST API per Veeam Service Provider Console.

Per accedere puoi seguire i seguenti passaggi:

1. Accedi alla voce **Cloud Connect** del servizio **Veeam Cloud Platform** dalle tab in alto;
2. Seleziona la voce **Impostazioni** dal menù a tendina.

![Screenshot 2024-05-13 at 16.41.14.png](/kb-assets/fb9789b65d-screenshot-2024-05-13-at-16-41-14.png)

### Reimposta la Password di accesso a Veeam Cloud Connect e Veeam Service Provider Console

La **Password** di **Veeam Cloud Connect** e **Veeam Service Provider Console** è la stessa e viene creata al momento dell’attivazione di Veeam Cloud Connect. É possibile reimpostare la password utilizzata globalmente.

Per reimpostare la password di accesso è sufficiente seguire i seguenti passaggi:

1. Accedi alla ad **Impostazioni** di **Cloud Connect;**
2. Raggiungi la sezione **Reimposta password;**
3. Premi sul bottone **Reimposta password;**
4. Si aprirà un Pop up in cui inserire la nuova password oppure generane una sicura premendo sul bottone indicato.
5. Premi sul bottone **reimposta.**

:::warning
**Per motivi di sicurezza** la Password non verrà più mostrata successivamente alla reimpostazione. Ti consigliamo di salvarla ora e conservarla in un posto sicuro.
Inoltre, in Veeam Cloud Platform la delle password è centralizzata, viene quindi utilizzata la stessa Password per **Veeam Cloud Connect** e **Veeam Service Provider Console**. Reimpostando la password da Cloud Connect, questa verrà reimpostata per entrambi gli elementi.
:::

![Screenshot 2024-05-14 at 09.14.49.png](/kb-assets/84ba2dc286-screenshot-2024-05-14-at-09-14-49.png)

### Abilita l’accesso Rest API

In questa sezione puoi abilitare l’accesso tramite REST API alla Veeam Service Provider Console.

Per abilitare l’accesso REST API è sufficiente seguire i seguenti passaggi:

1. Accedi alla ad **Impostazioni** di **Cloud Connect;**
2. Raggiungi la sezione **Accesso REST API**
3. Premi sullo switch e attiva l’accesso.

:::note
Una volta **attivato** vedrai lo switch sullo stato **attivo**.

[!WARNING]
Per disabilitare l’accesso API è sufficiente premere sullo switch.

[!INFO]
Ti occorrono ulteriori informazioni sull’utilizzo delle Rest API per Veeam Service Provider Console? [**Esplora la documentazione**](https://helpcenter.veeam.com/docs/vac/rest/reference/vspc-rest.html?ver=70)
:::

![Screenshot 2024-05-14 at 09.15.52.png](/kb-assets/0da95120b7-screenshot-2024-05-14-at-09-15-52.png)

# Elimina la funzionalità di Cloud Connect

Per eliminare un Cloud Connect è necessario seguire questi passaggi:

1. Accedi alla voce **Cloud Connect** del servizio **Veeam Cloud Platform** nel menù laterale;
2. Premi il selettore della **region** in alto a destra e seleziona la region da eliminare.
3. Premi il bottone **Elimina**

![Screenshot 2024-05-13 at 16.42.52.png](/kb-assets/3bf9ae3592-screenshot-2024-05-13-at-16-42-52.png)