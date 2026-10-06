---
title: "Backup Resources - Veeam Cloud Platform"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina spiega come attivare Backup Resources di Veeam Cloud Platform.

Con Backup Resources attivi risorse per il backup e la gestione dei dati per il mondo cloud, virtuale, fisico e Saas.

## Attiva funzionalità Backup Resources {#attiva-funzionalita-backup-resources}

Per attivare Backup Resources è sufficiente seguire i seguenti passaggi:

1. Accedi al servizio **Veeam Cloud Platform**. Non sai come fare? Segui la nostra [**guida**](index.md)**.**
2. Seleziona la voce **Backup Resources** nelle tab in alto;
3. Premi il bottone **Attiva Backup Resources** nell’Overview;
4. Seleziona ora la **Tipologia di billing** che desideri avere per il tuo spazio cloud tra:
1.   **Pay per usage**: seleziona questa modalità di billing per avere a disposizione risorse illimitate e pagare solo il consumo effettivo, calcolato su base oraria, ciò ti garantisce la massima flessibilità.
2.   **Pay per allocation**: seleziona questa modalità di billing per acquistare una quantità di risorse pre-allocate, ciò ti garantisce il massimo controllo. Se selezioni questa modalità dovrai anche indicare la **quantità in GB** che intenti allocare in cloud.![Screenshot 2024-05-13 at 17.24.11.png](/kb-assets/5b29f028a4-screenshot-2024-05-13-at-17-24-11.png)
5. Visualizza nella sezione Costo Stimato un riepilogo dei costi basati sulla configurazione selezionata. Indica un quantitativo di tempo in ore, giorni o mesi per una previsione di costi nell’intervallo selezionato. Ai fini di questo calcolo, consideriamo che 1 mese equivale a 730 ore.
6. Premi sul bottone **Attiva Backup Resources.**

:::note
Visualizzerai la pagina Backup Resources con lo stato **In attivazione** ben visibile.
Quando l’attivazione verrà completata con successo visualizzerai lo stato **Attivo**.

[!INFO]
La procedura di attivazione può impiegare fino a **10 minuti** per essere completata. Se trascorso questo tempo Veeam Cloud Connect non risulta ancora attivo ti invitiamo ad aprire un [**Case**](../../../account-manager/supporto/index.md) al nostro supporto.
:::

### Dettaglio Backup Resources - Dispositivi {#dettaglio-backup-resources-dispositivi}

Nella pagina Backup Resources, una volta che Veeam Cloud Platform è in stato **Attivo** puoi visualizzare lo **stato** e l'**utilizzo dei dispositivi** sottoposti a backup e la **modalità di billing** associata allo **spazio** utilizzato.

Per accedere al dettaglio Backup Resources è sufficiente seguire i seguenti passaggi:

1. Accedi al servizio **Veeam Cloud Platform**. Non sai come fare? Segui la nostra [**guida**](index.md)**.**
2. Seleziona la voce **Backup Resources** nelle tab in alto;
3. Vai alla voce **Dispositivi** nella tab.

![Screenshot 2024-05-13 at 17.35.16.png](/kb-assets/3dae6247d6-screenshot-2024-05-13-at-17-35-16.png)

#### Dettaglio Backup Dispositivi {#dettaglio-backup-dispositivi}

In questa sezione puoi visionare tutti i dettagli dei dispositivi in cui sono installati gli agenti di backup, suddivisi per VM, Server e Workstation con il relativo stato dei backup.

:::note
**Consiglio**: puoi visualizzare lo stato dei backup e dei job, per farlo è necessario installare un agente specifico. Scopri di più seguendo la [**guida**](../how-to-veeam-cloud-platform/visualizzazione-dello-stato-dei-backup-e-dei-job-sul-portale.md).
:::

#### Dettaglio Spazio utilizzato {#dettaglio-spazio-utilizzato}

In questa sezione puoi visualizzare la modalità di billing e l'utilizzo dello spazio utilizzato per i backup.

### Azioni Backup Resources {#azioni-backup-resources}

#### Modifica Backup Resources {#modifica-backup-resources}

Nella sezione Backup Resources puoi modificare la modalità di billing per lo spazio utilizzato. Per farlo, puoi seguire i seguenti passaggi:

1. Nella sezione di dettaglio Backup Resources, nella card **Billing e spazio utilizzato** premi sul bottone **modifica;**
2. Seleziona la **modalità di billing** che preferisci;
3. Conferma la tua scelta e premi **salva**.

:::info
La procedura di modifica può impiegare fino a **15 minuti** per completare le operazioni. Se trascorso questo tempo il servizio non risulta ancora in stato **Modifica,** ti invitiamo ad aprire un [**case**](../../../account-manager/supporto/index.md) al nostro supporto.
:::

#### Elimina Backup Resources {#elimina-backup-resources}

Per eliminare la sezione Backup Resources ed eliminare tutti i backup dal repository cloud puoi seguire i seguenti passaggi:

1. Nella sezione di dettaglio Backup Resources premi sul bottone **elimina**
2. Premi su **elimina**
3. Conferma la tua scelta seguendo le indicazioni del pop up e premi **elimina**.

:::warning
Se elimini il servizio tutti i dati al suo interno verranno cancellati.
**Una volta confermata, l'operazione non può essere annullata.**

[!INFO]
La procedura di eliminazione può impiegare fino a **15 minuti** per completare le operazioni. Se trascorso questo tempo il servizio non risulta ancora eliminato ti invitiamo ad aprire un [**case**](../../../account-manager/supporto/index.md) al nostro supporto.
:::

Una volta completata l’attivazione della funzionalità Backup Resources:

### Dettaglio Backup Resources - Impostazioni {#dettaglio-backup-resources-impostazioni}

Nella pagina Backup Resources - impostazioni puoi gestire le impostazioni quali la gestione avanzata bandwith e accelerazione WAN.

1. Accedi al servizio **Veeam Cloud Platform**. Non sai come fare? Segui la nostra [**guida**](index.md)**.**
2. Seleziona la voce **Backup Resources** dalle tab in alto;
3. Seleziona la voce **Impostazioni** dal menù a tendina.

#### Modifica la Gestione Avanzata Bandwith {#modifica-la-gestione-avanzata-bandwith}

La Gestione avanzata bandwidth consente di limitare il traffico di rete in ingresso.

:::info
Le impostazioni vengono applicate globalmente sia su **Cloud Connect** che su **Disaster Recovery**.
:::

Per modificare la Gestione avanzata bandwidth è sufficiente seguire i seguenti passaggi:

1. Accedi alla sezione **gestione avanzata bandwith**
2. Premi sul bottone **Modifica**
3. Specifica il limite per il **Traffico di rete in ingresso**.
4. Premi sul bottone **Salva** posto in basso a destra nella sezione dedicata alla Gestione avanzata bandwidth ed attendi il completamento del processo di attivazione.

![](/kb-assets/30a15f1922-image-20230322-084514.png)

#### Attiva la funzionalità Accelerazione WAN {#attiva-la-funzionalita-accelerazione-wan}

L’accelerazione WAN integrata, sviluppata da Veeam, ed ottimizzata specificamente per i file di Veeam Cloud Platform, consente di copiare i dati su location remote fino a 50 volte più velocemente rispetto a quanto avviene con l’utilizzo di una normale copia di file. Questa funzionalità viene specificamente utilizzata per processi di copia di backup offsite e processi di replica.

Per attivare l’Accelerazione WAN è sufficiente seguire i seguenti passaggi:

1. Raggiungi la sezione **Accelerazione WAN**
2. Premi sullo switch e accendi la funzionalità.

:::info
L’attivazione potrebbe richiedere alcuni minuti. Trascorsi 15 minuti, se backup resources rimane in attivazione, ti consigliamo di aprire un [**Case**](../../../account-manager/supporto/case.md) al nostro supporto tecnico.
:::

#### Disattiva la funzionalità Accelerazione WAN {#disattiva-la-funzionalita-accelerazione-wan}

Per disattivare l’Accelerazione WAN è sufficiente seguire i seguenti passaggi:

1. Raggiungi la sezione **Accelerazione WAN**
2. Premi sullo switch e accendi la funzionalità.

:::info
L’attivazione potrebbe richiedere alcuni minuti. Trascorsi 15 minuti, se backup resources rimane in attivazione, ti consigliamo di aprire un [**Case**](../../../account-manager/supporto/case.md) al nostro supporto tecnico.
:::