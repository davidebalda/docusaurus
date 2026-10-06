---
title: "Dettaglio sincronizzazione Dominio - Talky Time Direct Routing"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina illustra il dettaglio delle operazioni effettuate durante la sincronizzazione del **Dominio Teams**.

## Sincronizzazione Dominio {#sincronizzazione-dominio}

L’operazione di sincronizzazione del Dominio Teams è suddivisa nei **6 Step** indicati di seguito.

|     |     |     |
| --- | --- | --- |
| **Step** | **Stato** | **Dettaglio** |
| **1** | Creazione Dominio | Creazione del Dominio che verrà utilizzato per effettuare l’integrazione all’interno del Tenant Microsoft del Cliente |
| **2** | Verifica Dominio | Creazione del record DNS relativo al Dominio e propagazione dello stesso. Questo è necessario perché il nuovo Dominio creato venga correttamente riconosciuto da parte di Microsoft. |
| **3** | Creazione utente gestione integrazione | Creazione di un nuovo utente all’interno del Tenant Microsoft del Cliente, necessario a gestire le operazioni di integrazione. |
| **4** | Assegnazione ruolo Amministratore | Assegnazione del ruolo di Admin all’utente appena creato. |
| **5** | Assegnazione licenza | Assegnazione di una licenza di tipologia **Microsoft 365 Business Basic/Standard/Premium** oppure **Office 365 E1/E3/E5** all’utente appena creato. |
| **6** | Sincronizzazione utenti | Avvio dell’effettiva sincronizzazione, nella quale verranno effettuate le seguenti azioni:<br><br>- Recupero lista utenti con le corrette licenze assegnate. Questi risulteranno poi disponibili per il collegamento a Numerazioni/Interni PBX nella fase relativa.<br>- Verifica di Numerazioni/Interni PBX assegnati ad Utenti Teams ed eventuale segnalazione di discrepanze nella sezione apposita. |