---
title: "Chiavi API"
---

Questa pagina spiega come gestire le Chiavi API su Cortex.

# Introduzione

Le Chiavi API sono identificativi univoci che vengono utilizzati nell’autenticazione, per fornire agli utenti o agli script di programmazione un accesso alle risorse e ai servizi del tuo account Cortex tramite le API Cortex.

Utilizzando una Chiave API potrai configurare operazioni automatizzate di gestione del tuo Account e dei tuoi Servizi, utilizzando le chiamate API disponibili.

:::tip
Tutte le informazioni relative alle chiamate API sono disponibili nella [**documentazione delle API Cortex**](https://developers.my-cortex.io/reference/getting-started-with-your-api).
:::

# Accedi all’elenco delle Chiavi API

Per accedere alla lista delle chiavi API puoi seguire i seguenti passaggi:

1. Premi sulla voce **Impostazioni** nelle TAB di navigazione in alto
2. Vedrai l’elenco delle chiavi API e gli strumenti di gestione della sezione **Chiavi API**, comprensive di etichetta, chiave API, scadenza e stato.

## Stati delle Chiavi API

Una Chiave API può assumere i seguenti stati:

- **Attivo** → La Chiave API è correttamente funzionante e può essere utilizzare per l’autenticazione e l’utilizzo delle API Cortex;
- **Scaduto** → La Chiave API ha superato la sua data di scadenza e non può più essere utilizzata.

# Crea nuova Chiave API

Per creare una nuova Chiave API per il tuo utente puoi seguire i seguenti passaggi:

1. Premi il bottone **Nuova chiave API** posto in basso a destra nella sezione;
2. Copia lo **User ID** e la **Chiave API** presenti nella nuova pagina;
3. Seleziona la **Data di scadenza** per la Chiave API nella nuova pagina;
4. Inserisci una **Etichetta** per la Chiave API nella nuova pagina,
5. Premi il bottone **Crea chiave API** nella nuova pagina per confermare l’operazione, verrà ricaricata la lista delle Chiavi API con la nuova Chiave API in stato **Attivo**.

:::info
La Chiave API risulterà valida fino alle ore 23:59 del giorno impostato come data di scadenza.

[!WARNING]
Per motivi di sicurezza la Chiave API non verrà più mostrata successivamente alla creazione. **Ti consigliamo di salvarla prima di confermarne la creazione e conservarla in un posto sicuro.**
:::

# Elimina Chiave API

Per eliminare una Chiave API puoi seguire i seguenti passaggi:

1. Premi il bottone **Elimina chiave API** posto in corrispondenza della Chiave API, nella colonna delle azioni rapide;
2. Premi il bottone **Elimina chiave API** nella finestra di dialogo per confermare l’operazione.