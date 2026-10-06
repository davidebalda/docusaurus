---
title: "NethServer8"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina spiega come accedere e attivare il NethServer8 su Openstack as a Service.

## Che cos'è NethServer8?

[NethServer 8 (NS8)](https://docs.nethserver.org/projects/ns8/it/latest/introduction.html) è un'**application platform multi-nodo per il cloud ibrido**, che offre un’esperienza semplificata ma completa per distribuire, gestire e scalare applicazioni basate su container. Una delle sue caratteristiche chiave è la capacità di ospitare diverse applicazioni su una singola macchina o distribuire il carico di lavoro su più nodi. Questa flessibilità consente un utilizzo efficiente delle risorse e una scalabilità basate sulle esigenze dell’organizzazione.

**NethServer 8 è lo stack tecnologico alla base delle soluzioni** [**Nethesis**](https://www.nethesis.it/?_gl=1%2Anzz7nv%2A_up%2AMQ..%2A_ga%2AMTgxMTU0ODI4NC4xNzcyODA0NjE4%2A_ga_SX98756HBL%2AczE3NzI4MDQ2MTgkbzEkZzAkdDE3NzI4MDQ2MTgkajYwJGwwJGgxNDQzNDcyMjEw)**.**

NethServer può essere installato on-premise, auto-ospitato o **gestito nel cloud**, fornendo una gestione centralizzata e sicurezza su un’infrastruttura ibrida. Installando NethServer8 in cloud su Openstack as a Service in Cloud erediti:

- scalabilità dell’infrastruttura per soddisfare le esigenze della tua azienda in crescita;
- conformità e compliance di [CloudFire](https://www.cloudfire.it/it/why-cloudfire/compliance-sicurezza) e di [Openstack as a Service](https://www.cloudfire.it/it/why-cloudfire/certificazioni#acn);
- performance dell’installazione ed esecuzione di Nethserver8 su CloudFire [certificate da Nethesis](https://cdn.prod.website-files.com/61a61281728ca25bf8b63317/68e508082ee70e0cfd175197_CloudFire%20-%20Configurazione%20minima%20NethServer8.pdf)

# Attiva funzionalità NethServer8

:::note
**NethServer8 ad oggi è disponibile sulla** [Milano MI2](https://cloudfire-salesforce.s3.eu-south-1.amazonaws.com/Datasheet/OpenstackAsAServiceMI2Datasheet.pdf). È in roadmap la possibilità di attivare la funzionalità sulle altre region.
:::

## Requisiti - Creazione application credential

La scelta di creare e definire le application credential è un processo **Security-first e by design** voluto da CloudFire. Questo procedimento garantisce che solo le utenze con i permessi di creare istanze lato Openstack, siano in grado di creare istanze anche da Cortex.

:::note
Qualora l’application credential non funzioni più è possibile ripetere questo procedimento e crearne di nuove. Per qualsiasi attività su NethServer8 in Cortex è necessario disporre di questo oggetto attivo e funzionante.
:::

1. Accedi alla sezione **Gestione Istanze** in alto **per gestire le VM di Openstack**
2. **Accedi alla Dashboard Classica**. Verrai indirizzato al portale di gestione di Openstack as a Service in cui dovrai definire le application credential per gestire questa attività.
3. Seleziona il progetto in cui vuoi operare in alto
4. Naviga alla voce di menù **Identity** per definire gli utenti e i permessi che potranno deployare NethServer8
5. Vai alla voce **Application Credentials** per gestire gli accessi via API
6. Clicca su **Create Application Credential** per generare nuove credenziali
7. Inserisci una nome per riconoscere l' **Application Credential** che stai creando
8. Definisci una data di scadenza per le credenziali per limitarne la possibilità di deployare VM nel tempo
9. Assegna alla credenziale il ruolo **Member**
10. Flagga la voce **Unrestricted**
11. Conferma la configurazione delle application credential.
12. L'**ID** e la **secret** saranno visibili solo qui. Ti consigliamo pertanto di salvarle in un luogo sicuro o di scaricare i file.

# Deploy funzionalità NethServer8

Per attivare Nethserver8 puoi seguire i seguenti passaggi:

1. Accedi al servizio **Openstack as a Service** nel menu di navigazione. Non sai come fare? Segui la nostra [**guida**](index.md);
2. Clicca su **NETHSERVER 8** per definire i dettagli della gestione e creazione delle istanze
3. Clicca su **Crea Istanze** in Nethserver8
4. Scegli il profilo di configurazione che ritieni più idonea alle tue esigenze. **Tutte quelle proposte hanno ottenuto la validazione da parte di Nethesis di Configurazione Minima Certificata.** Quelle ad oggi disponibili sono

|     |     |     |     |
| --- | --- | --- | --- |
| #### **Flavor** | #### **vCPU** | #### **RAM** | #### **Storage** |
| **Openstack As a Service - Region MI2 - Flavor G3-24** | 2   | 4   | 80 GB |
| **Openstack As a Service - Region MI2 - Flavor G3-48** | 4   | 8   | 120 GB |
| **Openstack As a Service - Region MI2 - Flavor G3-832** | 8   | 32  | 380 GB |

Se preferisci configurazioni differenti puoi selezionare il flavor che preferisci dal menù a tendina. Puoi scegliere tra:

- **Flavor G3** New General Purpose - AMD Epyc Milan Series da 3.0GHz su hardware Dell PowerEdge Da 1 a 24 vCPU Da 1 a 128GB 1Gbit/s Simmetrica e **Direct Attached Storage**
- **Flavor G3S** New General Purpose AMD Epyc Milan Series da 3.0GHz su hardware Dell PowerEdge Da 1 a 24 vCPU Da 1 a 128GB 1Gbit/s Simmetrica Scalable Storage. Qualora selezioni questo flavor dovrai definire:
-   la **dimensione del volume attatched ridondato**
-   la **tipologia di volume.** Esistono due tipologie di storage Standard e Premium e di entrambi Encripted e Unencripted.

1. Inserisci Incolla qui sotto la tua chiave SSH pubblica oppure seleziona se hai già salvato chiavi SSH in Cortex. Se non sai come fare segui questa guida alla [rubrica chiavi SSH.](../primi-passi-openstack-as-a-service/key-pairs.md)
2. Inserisci uno o più IP. Non puoi utilizzare 0.0.0.0/00 e un IP non valido.
3. Definisci, modifica ed elimina i security grouop;
4. Dai un nome alla tua istanza
5. Inserisci l'Application ID e l'application secret che hai salvato poco fa.
6. Clicca su **Attiva istanza Nethserver**
7. Una volta conclusa la creazione apparirà un pop up con le credenziali di accesso web all'istanza di NethServer8 che ti consigliamo di salvare.

:::info
La procedura di attivazione può impiegare fino a **10 minuti** per completare le operazioni. Se trascorso questo tempo non risulta ancora attiva l’istanza ti invitiamo ad aprire un [**Case**](../../../account-manager/supporto/case.md) al nostro supporto.

[!NOTE]
Una volta attiva l’istanza NethServer8 puoi accedere alla piattaforma con le credenziali temporanee.

[!NOTE]
**É possibile anche deployare l’istanza per NethServer8 direttamente da Openstack in completa autonomia e con più possibilità di scelta nelle configurazioni**. Questa modalità richiede maggiori competenze lato Openstack. Puoi farlo ti consigliamo di seguire questa [guida](../how-to-openstack-as-a-service/deploy-nethserver-su-openstack.md).
:::

# Visualizzazione Istanze Nethserver 8 attive

Per visualizzare e gestire le Istanze Nethserver 8 attive puoi seguire i seguenti passaggi:

1. Accedi al servizio **Openstack as a Service** nel menu di navigazione. Non sai come fare? Segui la nostra [**guida**](index.md);
2. Seleziona alla sezione **NethServer8** nelle tab in alto
3. Clicca su Visualizza tabella per **cambiare modalità di visualizzazione delle istanze attive**
4. **User** e **Password** indicate nella tabella sono monouso. Copiale ed incollale, ti serviranno per accedere effettivamente a Nethserver8
5. **Clicca sull'URL** che ti porta direttamente al portale di gestione di Nethserver8, accedi con lo user e la password indicate in tabella. *Ti verrà richiesto di cambiarle al primo accesso.*

# Modifica Istanze Nethserver 8 attive

Per modificare le Istanze Nethserver 8 attive puoi seguire i seguenti passaggi:

1. Accedi al servizio **Openstack as a Service** nel menu di navigazione. Non sai come fare? Segui la nostra [**guida**](index.md);
2. Seleziona alla sezione **NethServer8** nelle tab in alto;
3. Visualizza le istanze attive;
4. Premi sull’icona **modifica** in corrispondenza dell’istanza che intendi modificare. Potrai modificare
1.   **Profilo**
2.   **Security Group**
5. Per farlo ti verrà richiesto nuovamente di inserire Client ID e Client Secret dell’application credential con i permessi. **Se i permessi sono scaduti puoi creare un’altra application credential.**

:::note
La modifica del profilo può avvenire solo con flavor compatibili rispetto a quello di partenza e di risorse e dimensioni maggiori

[!NOTE]
**La modifica dell’istanza prevede lo spegnimento della prima e la creazione della seconda. Non è richiesta alcuna operazione da parte tua.**

[!INFO]
La procedura può impiegare fino a **10 minuti**. Se trascorso questo tempo non risulta ancora attiva l’istanza ti invitiamo ad aprire un [**Case**](../../../account-manager/supporto/case.md) al nostro supporto.
:::

# Eliminazione Istanze Nethserver 8 attive

Per eliminare le Istanze Nethserver 8 attive puoi seguire i seguenti passaggi:

1. Accedi al servizio **Openstack as a Service** nel menu di navigazione. Non sai come fare? Segui la nostra [**guida**](index.md);
2. Seleziona alla sezione **NethServer8** nelle tab in alto;
3. Visualizza le istanze attive;
4. Premi sull’icona **elimina** in corrispondenza dell’istanza che intendi eliminare.
5. Per farlo ti verrà richiesto nuovamente di inserire Client ID e Client Secret dell’application credential con i permessi. **Se i permessi sono scaduti puoi creare un’altra application credential.**

:::note
L’eliminazione di qualsiasi istanza è completa e prevede, nei caso di flavor G3S anche dello storage scalable.

[!INFO]
La procedura può impiegare fino a **10 minuti**. Se trascorso questo tempo non risulta ancora attiva l’istanza ti invitiamo ad aprire un [**Case**](../../../account-manager/supporto/case.md) al nostro supporto.
:::