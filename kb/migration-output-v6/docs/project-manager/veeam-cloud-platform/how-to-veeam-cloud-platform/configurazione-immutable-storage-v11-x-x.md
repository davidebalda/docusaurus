---
title: "Configurazione Immutable Storage - v11.x.x"
---

- [Creazione Backup Repository: S3 Compatible](#creazione-backup-repository-s3-compatible)
- [Configurazione Scale-out Repositories](#configurazione-scale-out-repositories)
- [Note relative alla creazione del backup su Veeam](#note-relative-alla-creazione-del-backup-su-veeam)

## Creazione Backup Repository: S3 Compatible {#creazione-backup-repository-s3-compatible}

- In *Backup Infrastructure* selezionare *Backup Repositories* quindi **Add Repository**  

![](/kb-assets/a45fabc222-screenshot-2022-03-10-at-09-26-39.png)

- Selezionare la tipologia **Object Storage**  

![](/kb-assets/715187bfc3-screenshot-2022-03-10-at-09-26-51.png)

- Quindi **S3 Compatible**  

![](/kb-assets/8d664442f1-screenshot-2022-03-10-at-09-27-03.png)

- Assegnare il **nome** quindi su *Next*  

![](/kb-assets/54ebba0126-screenshot-2022-03-10-at-09-27-33.png)

:::caution
Mettere la spunta su **Limit concurrent tasks to:** e impostare il valore **2** in caso di `<20 vm di cui fare backup offload, **4** in caso di>`20 vm di cui fare backup offload
:::

- Configurare l' **Account** utilizzando l' **Endpoint** ricevuto insieme alle credenziali come **Service Point** e la **Region**  
Cliccare quindi su *Add* per aggiungere le credenziali di accesso al Bucket  

![](/kb-assets/3fc8e3176e-screenshot-2022-03-10-at-09-27-58.png)

- Compilare i campi **Access key** e **Secret key** utilizzando le credenziali ricevute  

![](/kb-assets/d07609d765-screenshot-2022-03-10-at-09-28-28.png)

- Alternativamente selezionare le credenziali create in precedenza quindi cliccare su *Next*  

![](/kb-assets/1e0ad8edd5-screenshot-2022-03-10-at-09-29-01.png)

- Nella sezione **Bucket** cliccare su **Browse** e, se le credenziali sono state inserite correttamente, verrà mostrato il bucket s3  

![](/kb-assets/095c76ed17-screenshot-2022-03-10-at-09-29-41.png)

- Selezionare il *bucket* quindi cliccare su *Next*  

![](/kb-assets/27eaeeb0f1-screenshot-2022-03-10-at-09-29-51.png)

- Cliccare quindi sul secondo **Browse** ovvero quello legato alla *Folder*  
- Nel caso in cui il bucket non sia mai stato utilizzato occorrerà **creare** una nuova folder cliccando sul tasto *New Folder* quindi selezionarla e cliccare su *Ok*  

![](/kb-assets/ff7ccef138-screenshot-2022-03-10-at-09-30-33.png)

- Per configurare la funzionalità di **Immutability** spuntare *”Make recent backups immutable for: XXX days”* e compilare il valore in giorni relativo all' immutabilità dei dati.  

![](/kb-assets/1d3eeae8aa-screenshot-2022-03-10-at-09-30-49.png)

- Cliccare quindi su *Apply* per completare la configurazione

:::caution
La quantità di giorni indicata nel campo *Make recent backups immutable for: XXX days* vincola l’eliminazione dei backup a tale data sia nel **Tier Performance** che nel **Tier Capacity**
  
Tale intervallo di tempo **NON** è modificabile successivamente.
:::

## Configurazione Scale-out Repositories {#configurazione-scale-out-repositories}

1. Fare tasto DX → Edit sul nome dello Scale-out Repositories  
![](/kb-assets/ce86ce3157-screenshot-2022-03-10-at-10-00-26.png)

:::note
Modificare la quantità di giorni nel campo **Move backups to object storage as they age out of the operational restore window** per ridurre lo spazio occupato nel Perfomance Tier
:::

2\. Nella sezione ***Capacity Tier*** mettere la spunta su \*”Extend scale-out backup repository capacity with object storage:”

3\. Selezionare il **Bucket S3** precedentemente creato  

![](/kb-assets/f16c5f1fd6-screenshot-2022-03-10-at-10-01-22.png)

4\. Cliccare su *Apply* quindi su *Finish* per terminare la modifica e applicarla.

:::info
Da questo momento tutti i backup che utilizzando questo Scale-out Repository usufruiranno della copia nel **Capacity Tier** con funzionalità **Immutable** attiva

[!TIP]
La copia offload del backup verso il bucket s3 appena configurato partirà successivamente al termine del backup nel Perfomance Tier.
:::

## Note relative alla creazione del backup su Veeam {#note-relative-alla-creazione-del-backup-su-veeam}

1. Nella selezione dello Storage cliccare su “Advanced”

![](/kb-assets/9bb7034866-screenshot-2022-05-06-at-17-12-39.png)

2\. Nella tab “Storage” alla voce “Storage optimization” selezionare “Local target (large block)” per questioni di ottimizzazione durante l’upload e il recovery dei backup a livello di performance.

![](/kb-assets/21cea106fe-screenshot-2022-05-06-at-17-14-27.png)

![](/kb-assets/4d45c5e256-screenshot-2022-05-06-at-17-14-42.png)

3\. In relazione alla configurazione default di Veeam legata al numero di connessioni contemporanee utilizzate per ogni task di backup offload, occorre modificare la seguente chiave di registro:

- `HKEY_LOCAL_MACHINE\SOFTWARE\Veeam\Veeam Backup and Replication\S3ConcurrentTaskLimit`

il cui valore va impostato a ***2***