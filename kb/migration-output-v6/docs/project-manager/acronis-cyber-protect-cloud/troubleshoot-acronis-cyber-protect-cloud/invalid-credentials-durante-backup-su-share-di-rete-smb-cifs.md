---
title: "Invalid Credentials durante backup su share di rete (smb/cifs)"
---

## Problema {#problema}

Il problema riguarda l'agent Linux.

Backup plan funzionanti, con diverse esecuzioni correttamente terminate pregresse, si ritrovano in stato d'errore notificando l'invalidità delle credenziali per accedere alla risorsa di rete.

## Prerequisiti {#prerequisiti}

Escludete possibili anomalie esterne e avvenuti cambi di credenziali per l'accesso alla risorsa di rete.

Confermate di essere nella situazione indicata provando a montare manualmente la share in questione nel sistema problematico con le credenziali indicate nella console web. In caso di successo, provate ad effettuare il browse dei backup esistenti (nella web console) utilizzando l'agent che presenta il problema: verranno richieste le credenziali per accedere alla share > utilizzando le stesse credenziali del punto precedente riceverete errore di "invalid credentials" .  

## Possibili cause e soluzioni {#possibili-cause-e-soluzioni}

Il problema è causato dal disallineamento delle credenziali fra agent e web console.

Potrebbe essere causato da un aggiornamento dell'agent stesso, aggiornamento lato kernel del sistema linux o semplice errore nella sincronizzazione dei metadati fra agent e cloud.

La procedura principale per la risoluzione della problematica è la seguente:

- disinstallare l'agent dalla macchina linux
- reinstallare e ri-registrare l'agent
- permettere l'esecuzione schedulata da backup plan
- accedere nel backup vault direttamente (management console su backup.cloudfire.it > "BACKUPS" > selezionate la location problematica > impostate l'agent oggetto del problema in "Machine to browse from:" ed infine inserite le credenziali della share) 

A questo punto potete riprovare il browse dei backup e un lancio manuale del Backup plan.

  

:::note
**Sommario**



- [Problema](#problema)
- [Prerequisiti](#prerequisiti)
- [Possibili cause e soluzioni](#possibili-cause-e-soluzioni)
-   Filter by label
* * *
**Articoli collegati**


##### Filter by label {#filter-by-label}

There are no items with the selected labels at this time.
:::