---
title: "Disaster Recovery - Veeam Cloud Platform"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina spiega come attivare ed eliminare le funzionalità Disaster Recovery con Veeam e come gestire le operazioni di failover da Veeam Service Provider Console.

- **Attivare** la funzionalità Disaster Recovery permette di utilizzare Veeam Service Provider Console per gestire le proprie macchine in caso di errore in produzione.
- **Gestire** la funzionalità di Disaster Recovery permette di utilizzare le operazioni di failover da Veeam Service Provider Console.
- **Eliminare** la funzionalità Disaster Recovery permette di cancellare tutte le risorse correlate e disabilitate le funzionalità su Veeam Service Provider Console.

## Prerequisiti di accesso {#prerequisiti-di-accesso}

Prima di procedere ad effettuare l’accesso su Veeam Cloud Connect Portal controlla di avere **Attivato e Collegato** il servizio di Veeam Cloud Connect.

Il **Disaster Recovery** consente di garantire in modo affidabile la continuità dei propri servizi IT su qualsiasi scala con il ripristino da backup, repliche, repliche CDP e storage snapshot basati su Veeam. Questo approccio viene adottato per ripristinare l'accesso e la funzionalità della propria infrastruttura in seguito a eventi disastrosi naturali o causati dall'uomo, come guasti alle apparecchiature o attacchi informatici.

## Attiva la funzionalità Disaster Recovery {#attiva-la-funzionalita-disaster-recovery}

Per attivare la funzionalità di Disaster Recovery è sufficiente seguire i seguenti passaggi:

1. Accedi al servizio **Veeam Cloud Platform**. Non sai come fare? Segui la nostra [**guida**](index.md)**.**
2. Seleziona la voce **Disaster Recovery** dalle tab in alto;
3. Premi il bottone **Attiva Disaster Recovery**;
4. Scegli tra gli **Hypervisor** disponibili nella card Hypervisor.
5. Definisci il numero di IP pubblici allocati.
6. Premi sul bottone **Attiva** posto in basso a destra nella pagina.
7. Premi sul bottone **Conferma** nella finestra di dialogo.  
Visualizzerai nuovamente la pagina Disaster Recovery con lo stato **In attivazione** ben visibile in alto a destra nella sezione Disaster Recovery.
8. Una volta completata l’attivazione visualizzerai la pagina Disaster Recovery con lo stato **Attivo** ben visibile in alto a destra nella sezione Disaster Recovery.

:::info
La procedura di attivazione può impiegare fino a **10 minuti** per essere completata. Se trascorso questo tempo Veeam Cloud Connect non risulta ancora attivo ti invitiamo ad aprire un [**Case**](../../../account-manager/supporto/index.md) al nostro supporto.

[!CAUTION]
Per mantenere i **più elevati standard di sicurezza** la gestione delle password è centralizzata. Viene quindi utilizzata la stessa Password per **Veeam Cloud Connect**, **Veeam Service Provider Console** e **Disaster Recovery**.
Reimpostando la Password per uno di questi elementi questa verrà reimpostata anche per tutti gli altri. Per **reimpostare la password** occorre seguire questa [**guida**](https://cloudfireit.atlassian.net/wiki/spaces/~239475519/pages/2182774787/New+Cloud+Connect+-+Veeam+Cloud+Platform#Reimposta-la-Password-di-accesso-a-Veeam-Cloud-Connect-e-Veeam-Service-Provider-Console)**.**
:::

### Gestisci la funzionalità Disaster Recovery {#gestisci-la-funzionalita-disaster-recovery}

Per gestire le funzionalità Disaster Recovery è sufficiente seguire i seguenti passaggi:

1. Accedi al servizio **Veeam Cloud Platform**. Non sai come fare? Segui la nostra [**guida**](index.md)**.**
2. Seleziona la voce **Disaster Recovery** nel menù laterale;
3. Premi sul bottone **Accedi** posto in basso a destra nella sezione Disaster Recovery.
4. Si aprirà una nuova finestra nel browser ([https://vac.cloudfire.it](https://vac.cloudfire.it/)) nella quale è possibile inserire le credenziali Username e Password per accedere a Veeam Service Provider Console.![](/kb-assets/686b67b2db-bk-veeam-gestione-7.png)

### Elimina la funzionalità Disaster Recovery {#elimina-la-funzionalita-disaster-recovery}

Per eliminare la funzionalità Disaster Recovery è sufficiente seguire i seguenti passaggi:

1. Accedi al Progetto nel quale vuoi eliminare la funzionalità Disaster Recovery, seleziona la voce **Backup Veeam** dal menu di navigazione e poi la voce **Gestione**.
2. Seleziona la voce **Disaster Recovery** dalla barra di navigazione orizzontale presente in pagina.
3. Premi il bottone **Elimina** in basso a destra nella sezione Disaster Recovery.
4. Premi il bottone **Elimina** nella finestra di dialogo per eliminare il Disaster Recovery.
5. Visualizzerai nuovamente la pagina Disaster Recovery con lo stato **In eliminazione** ben visibile in alto a destra.
6. Una volta completata l’eliminazione visualizzerai la pagina Disaster Recovery con lo stato **Eliminato** ben visibile in alto a destra nella sezione Disaster Recovery.

:::caution
L’eliminazione del servizio Disaster Recovery comporta l’eliminazione di **TUTTE** le risorse correlate. Verranno inoltre disabilitate le funzionalità su Veeam Service Provider Console.  
**L’operazione è irreversibile e non può essere annullata**.  
Per riattivare la funzionalità una volta eliminata dovrai contattare il nostro supporto tecnico seguendo la [**guida**](#) o scrivendo una email all’indirizzo [help@cloudfire.it](mailto:help@cloudfire.it).

[!INFO]
La procedura di eliminazione può impiegare fino a **2 minuti** per completare le operazione. Se trascorso questo tempo il servizio non risulta ancora in stato **Eliminato** ti invitiamo ad aprire un [**Case**](../../../account-manager/supporto/index.md) al nostro supporto.
:::

![](/kb-assets/3893ec2d3b-image-20230322-081642.png)