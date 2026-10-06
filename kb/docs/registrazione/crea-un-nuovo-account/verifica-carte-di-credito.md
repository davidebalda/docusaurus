---
title: "Verifica carte di credito"
---

Questa pagina spiega come viene effettuata la verifica delle carte di credito sui nostri sistemi.

## Come funziona {#come-funziona}

Il nostro sistema verifica le carte di credito eseguendo una transazione di **€ 0** o **€ 1,00**, e poi annullandola immediatamente.

Per la maggior parte dei circuiti bancari e di carte di credito le transazioni vengono inizialmente tentate con un'autorizzazione di € 0. Se le autorizzazioni da € 0 non sono supportate, viene eseguita automaticamente un'autorizzazione da € 1,00.

In ogni caso in cui un'autorizzazione di € 1,00 restituisce un risultato positivo, inviamo immediatamente una richiesta di **annullamento** automatico per garantire che la transazione non venga addebitata e che scompaia dall'estratto conto del titolare della carta il prima possibile.

:::info
Alcune banche potrebbero non riconoscere immediatamente le richieste annullate.
È possibile che, dopo l'emissione dell'annullamento, l’estratto conto della carta mostri ancora l'addebito in sospeso. Se ciò accade, puoi contattare direttamente la tua banca e chiedergli di aggiornare il tuo estratto conto, indicando loro di cercare la richiesta di annullamento.
:::