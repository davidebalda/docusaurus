---
title: "Visualizzazione dello stato dei backup e dei job sul portale"
---

Questa guida mostra come installare e sincronizzare i dati presenti sul Backup Server nel quale è installato Veeam Backup and Replication con la Veeam Availability Console.

## Prerequisiti di installazione della Veeam Availability Console {#prerequisiti-di-installazione-della-veeam-availability-console}

Per verificare i requisisti per l’installazione della Veeam Availability Console è sufficiente seguire i seguenti passaggi:

1. Accedi al Backup Server sul quale è installato Veeam Backup e Replication
2. Vai a **Backup Infrastructure** → **Service Provider**
3. Sull’elemento nella sezione Service Provider, premere con il tasto destro e andare su **Properties**
4. Verificare che la voce “**Allow this Veeam Backup & Replication installation to be managed by the service provider**” sia selezionata.  
Se non selezionata, selezionarla.  
![](/kb-assets/4042b69a8d-bk-veeam-vac-1.png)
5. Premi su **Next** e applica la modifica apportata  
\[Facoltativo\] Premi su **Cancel** se la voce era già spuntata e vai direttamente alla prossima sezione
6. Premi su **Finish** una volta apportate le modifiche.

:::info
La voce *Allow this Veeam Backup & replication to be managed by the service provider* permette la corretta sincronizzazione dei dati presenti sul Backup Server con la dashboard della Veeam Availability Console e permette al Service Provider e all’utente di gestire le installazioni, orchestrare e monitorare l’andamento dei backup da remoto.
:::

## Come installare la Veeam Availability Console {#come-installare-la-veeam-availability-console}

Per installare correttamente la Veeam Availability Console è sufficiente seguire i seguenti passaggi:

1. Vai su [https://vac.cloudfire.it](https://vac.cloudfire.it) e accedi con le tue credenziali del servizio **Veeam Cloud Platform** da Cortex
2. Vai su **Clients** → **Discovery**
3. Dalla tab nella parte superiore dello schermo, vai su **Computers**
4. Premi su **Download Agent**  
![](/kb-assets/0b791bca64-bk-veeam-vac-2.png)
5. Scegli su quale sistema operativo deve essere installata la Console (Windows/Linux/..)
6. Specifica la tua **Company**
7. Copia il **Link** per il Download della console e incollalo nel browser del tuo Backup Server per inizializzare il download dell’eseguibile
8. Lancia il file eseguibile e **segui il wizard** di installazione
9. Una volta terminato potrai visualizzare e gestire i tuoi dati direttamente dalla **Veeam Availability Console** andado su [https://vac.cloudfire.it](https://vac.cloudfire.it)