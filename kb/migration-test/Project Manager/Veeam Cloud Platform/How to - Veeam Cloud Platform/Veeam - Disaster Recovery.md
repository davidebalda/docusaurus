- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Configurazione job di Replica](#configurazione-job-di-replica)
- [Configurazione Failover Plans](#configurazione-failover-plans)
- [Creazione Failover Plan](#creazione-failover-plan)
- [Testare il Failover Plan](#testare-il-failover-plan)
- [Eseguire i Failover Plan](#eseguire-i-failover-plan)

### Introduzione

In questa guida vi mostreremo come configurare il Disaster Recovery con Veeam Cloud Platform e come utilizzarlo in caso di necessità.

### Prerequisiti

Per poter utilizzare il Disaster Recovery dovete per prima cosa attivare il corrispondente servizio sul vostro Management Portal Cortex → [Disaster Recovery - Veeam Cloud Platform](../../veeam-cloud-platform/gestione-del-servizio-veeam-cloud-platform/disaster-recovery-veeam-cloud-platform.md)

Una volta attivato il servizio, all’interno della Console Veeam del vostro B&R Server, dovrete aver aggiunto la repo Cloudfire come Service Provider → [Collegamento Cloud Connect a Cloudfire - Veeam Cloud Platform](../../veeam-cloud-platform/gestione-del-servizio-veeam-cloud-platform/cloud-connect-veeam-cloud-platform/collegamento-cloud-connect-a-cloudfire-veeam-cloud-platform.md)

Una volta soddisfatti i requisiti sopra, avrete accesso all’infrastruttura VMWare di Disaster recovery messa a disposizione da Cloudfire.

### Configurazione job di Replica

la prima operazione da fare per poter utilizzare il Disaster Recovery è creare un job di replica delle macchine virtuali. Scegliete le macchine che volete replicare e di seguito nelle destination aggiungete il **Cloud Host “**Vshpere DRaaS”.

![](./attachments/image-20221209-095330.png)

Terminate il wizard configurando la replica in base alle vostre esigenze di schedulazione e retention.

Una volta effettuata almeno una replica correttamente potete passare alla configurazione dei **Failover Plan.**

### Configurazione Failover Plans

I Failover Plans sono appunto i piani in cui andiamo a specificare le tempistiche e modalità di attivazione delle macchine replicate nel sito di disaster recovery in caso di necessità.

I failover plans possono essere di 2 tipi:

1. **Full:** nel caso in cui tutta l’infrastruttura risulta non più disponibile viene attivato questo piano che prevede la riaccensione di tutte le macchine specificate nel piano e nell’ordine specificato. Nel mentre, Veeam attiva una network appliance nel sito di DR che risulterà essere il default gateway delle macchine replicate e di conseguenza verranno pubblicate tramite gli IP pubblici specificati in fase di attivazione del servizio di Disaster Recovery. Questa appliance si occuperà di fare anche del port-forwading specificato nel plan. Probabilmente in questo caso anche il Server B&R Veeam non sarà disponibile per cui è possibile far partire il job dalla VAC ([vac.cloudfire.it](http://vac.cloudfire.it)) oppure da Cortex nella sezione Disaster Recovery.![](./attachments/image-20221209-113853.png)
2. **Partial:** caso in cui solo parte dell’infrastruttura risulta non più disponibile ma l’infrastruttura local Veeam è rimasta operativa e disponibile. Questo tipo ti piano prevede che Veeam tramite l’attivazione di 2 network appliance (una in locale ed una nel sito di DR) instauri una VPN site to site in modo da trasportare il layer 2 e far comunicare l’infrastruttura locale con le macchine replicate attivate nel sito di DR.  
![](./attachments/image-20221209-114000.png)

### Creazione Failover Plan

Selezionare la VM replicate da inserire nel piano ed indicare il delay in secondi della riaccensione:

![](./attachments/image-20221209-152548.png)

Selezionare il default gateway per le VM replicate, avete a disposizione 7 sotto-reti private che potete configurare a piacere cliccando su “Manage Default Gateways”. Questa operazione andrà a configurare la network appliance nell’infrastruttura di DR.

![](./attachments/image-20221209-152353.png)

Nella sezione Public IP address avete la possibilità di configurare il o gli indirizzi pubblici assegnati con relativi port forwarding in caso di Full Failover in modo da poter raggiungere la vostra infrastruttura replicata direttamente da internet.

![](./attachments/image-20221209-152847.png)

### Testare il Failover Plan

Dalla Dashboard è possibile anche lanciare un test del failover plan.

Il test provvederà ad eseguire la procedura di accensione della macchina replicata in cloud e di conseguenza a lanciare un ping dalla network appliance verso le macchine replicate ed accese.

Se il ping va a buon fine il test è considerato superato. La replica verrà spenta nuovamente.

### Eseguire i Failover Plan

Se siete costretti a far partire un **Full failover plan** potete farlo in 2 modi:

1. Dalla console del Veeam B&R Server, Failover Plan → Selezioni il piano → start  
![](./attachments/image-20221209-172335.png)
2. Dalla VAC ([vac.cloudfire.it](http://vac.cloudfire.it)), Failover Plans → Selezioni il piano → Start  
![](./attachments/image-20221209-172552.png)

Se invece volete eseguire un **Partial failover plan** dovete procedere dalla console del Veeam B&R Server Replicas → Ready → selezionate la replica → Failover now

![](./attachments/image-20221209-172810.png)