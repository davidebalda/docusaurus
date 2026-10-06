---
title: "Disdetta ed eliminazione funzionalità Veeam Cloud Platform"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina spiega come **disattivare** ed **eliminare** ciascuna funzionalità presente in Veeam Cloud Platform.

- [Elimina la funzionalità di Cloud Connect](#elimina-la-funzionalit-di-cloud-connect)
- [Elimina la funzionalità di Backup Resources](#elimina-la-funzionalit-di-backup-resources)
- [Disattiva la funzionalità di Accelerazione WAN](#disattiva-la-funzionalit-di-accelerazione-wan)
- [Elimina la funzionalità Disaster Recovery](#elimina-la-funzionalit-disaster-recovery)
- [Elimina Backup Microsoft 365](#elimina-backup-microsoft-365)
- [Revoca ed elimina una licenza in Veeam Cloud Platform](#revoca-ed-elimina-una-licenza-in-veeam-cloud-platform)
-   [Revoca una Licenza](#revoca-una-licenza)
-   [Elimina una licenza](#elimina-una-licenza)

# Elimina la funzionalità di Cloud Connect

Per eliminare un Cloud Connect è necessario seguire questi passaggi:

1. Accedi alla voce **Cloud Connect** del servizio **Veeam Cloud Platform** nel menù laterale. Se non sai come fare segui questa [**guida**](gestione-del-servizio-veeam-cloud-platform/cloud-connect-veeam-cloud-platform/index.md)**;**
2. Premi il selettore della **region** in alto a destra e seleziona la region da eliminare.
3. Premi il bottone **Elimina**

![Screenshot 2024-05-13 at 16.42.52.png](/kb-assets/0fa304b8b5-screenshot-2024-05-13-at-16-42-52.png)

# Elimina la funzionalità di Backup Resources

Per eliminare la sezione Backup Resources ed eliminare tutti i backup dal repository cloud puoi seguire i seguenti passaggi:

1. Nella [sezione di dettaglio Backup Resources](gestione-del-servizio-veeam-cloud-platform/backup-resources-veeam-cloud-platform.md) premi sul bottone **elimina**
2. Premi su **elimina**
3. Conferma la tua scelta seguendo le indicazioni del pop up e premi **elimina**.

:::warning
Se elimini il servizio tutti i dati al suo interno verranno cancellati.
**Una volta confermata, l'operazione non può essere annullata.**

[!INFO]
La procedura di eliminazione può impiegare fino a **15 minuti** per completare le operazioni. Se trascorso questo tempo il servizio non risulta ancora eliminato ti invitiamo ad aprire un [**case**](../../account-manager/supporto/index.md) al nostro supporto.
:::

# Disattiva la funzionalità di Accelerazione WAN

Per disattivare l’Accelerazione WAN è sufficiente seguire i seguenti passaggi:

1. Raggiungi la sezione **Accelerazione WAN** nella sezione [Impostazioni](gestione-del-servizio-veeam-cloud-platform/backup-resources-veeam-cloud-platform.md);
2. Premi sullo switch e accendi la funzionalità.

:::info
L’attivazione potrebbe richiedere alcuni minuti. Trascorsi 15 minuti, se backup resources rimane in attivazione, ti consigliamo di aprire un [**Case**](../../account-manager/supporto/case.md) al nostro supporto tecnico.
:::

# Elimina la funzionalità Disaster Recovery

Per eliminare la funzionalità Disaster Recovery è sufficiente seguire i seguenti passaggi:

1. Accedi al servizio **Veeam Cloud Platform**. Accedi al Progetto nel quale vuoi eliminare la funzionalità Disaster Recovery, seleziona la voce **Backup Veeam** dal menu di navigazione e poi la voce **Gestione**. Non sai come fare? Segui la nostra [**guida**](gestione-del-servizio-veeam-cloud-platform/index.md)**.**
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
La procedura di eliminazione può impiegare fino a **2 minuti** per completare le operazione. Se trascorso questo tempo il servizio non risulta ancora in stato **Eliminato** ti invitiamo ad aprire un [**Case**](../../account-manager/supporto/index.md) al nostro supporto.
:::

![](/kb-assets/5a279cf0ee-image-20230322-081642.png)

# Elimina Backup Microsoft 365

Per eliminare un Backup Microsoft 365 è sufficiente seguire i seguenti passaggi:

1. Accedi alla voce **Backup Microsoft 365** del servizio **Veeam Cloud Platform** dalla tab;
2. Premi il bottone **Elimina;**
3. **Conferma** la tua scelta ed elimina il **Backup Microsoft 365**.

:::note
L’intera procedura può a impiegare fino a circa **10 min**. Se trascorso questo tempo il servizio non risulta ancora in stato **Eliminato** ti invitiamo ad aprire un [**Case**](../../account-manager/supporto/case.md) al nostro supporto.
:::

# Revoca ed elimina una licenza in Veeam Cloud Platform

### Revoca una Licenza

L’azione di revoca di una licenza comporta la disattivazione e l’eliminazione di tutte le funzionalità ad esso legate. É ancora possibile visualizzare la licenza nella tabella di riepilogo, ma non può essere riattivata.

Per disattivare la licenza selezionata puoi seguire i seguenti passaggi:

1. Accedi alla sezione [**licenza rental**](gestione-del-servizio-veeam-cloud-platform/licenze-veeam-cloud-platform.md)**;**
2. Accedi al dettaglio della licenza;
3. Premi sull’azione di **Revoca;**
4. Premi **Conferma;**
5. Lo stato della licenza sarà in un primo momento in **aggiornamento** e successivamente in **Revocato**.

:::warning
L’operazione non può essere annullata. Una volta revocata la licenza non è possibile attivarla nuovamente ed utilizzarla, è necessario creare e attivare una nuova licenza.

[!INFO]
La procedura di attivazione può impiegare fino a **10 minuti** per essere completata. Se trascorso questo tempo Veeam Cloud Connect non risulta ancora attivo ti invitiamo ad aprire un [**Case**](../../account-manager/supporto/index.md) al nostro supporto.
:::

![](/kb-assets/c6ecc72768-image-20220908-102445.png)

### Elimina una licenza

Per eliminare la licenza selezionata dalla tabella di riepilogo puoi seguire i seguenti passaggi

1. Accedi alla sezione [**licenza rental**](gestione-del-servizio-veeam-cloud-platform/licenze-veeam-cloud-platform.md)**;**
2. Accedi al dettaglio della licenza;
3. Premi sull’azione di **eliminazione;**
4. Premi **Conferma**

:::warning
L’operazione non può essere annullata. Una volta revocata la licenza non è visualizzabile nella tabella.

[!INFO]
La procedura di attivazione può impiegare fino a **10 minuti** per essere completata. Se trascorso questo tempo Veeam Cloud Connect non risulta ancora attivo ti invitiamo ad aprire un [**case**](../../account-manager/supporto/index.md) al nostro supporto.
:::

![](/kb-assets/35e10920c1-image-20220908-102541.png)