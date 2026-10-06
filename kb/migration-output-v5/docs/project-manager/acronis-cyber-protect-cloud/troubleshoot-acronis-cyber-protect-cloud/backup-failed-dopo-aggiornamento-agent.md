---
title: "Backup Failed dopo aggiornamento Agent"
---

## Problema {#problema}

Successivamente all' aggiornamento dell’ agent su host Windows è possibile incorrere nell' errore relativo a backup fallito per “Agent offline” anche se questo risulta essere online da dashboard.

## Possibili cause e soluzioni {#possibili-cause-e-soluzioni}

Le cause possono essere molteplici, per questo si rimanda all' articolo : [Problemi di comunicazione tra Agent e Cloud](problemi-di-comunicazione-tra-agent-e-cloud.md)

Nel caso in cui le soluzioni presentate in quell' articolo non fossero andate a buon fine, il problema può risiedere nella corruzione del certificato X509 utilizzato dall' agent per la comunicazione con la parte server.