- [Creazione Backup Repository: S3 Compatible](#creazione-backup-repository-s3-compatible)
- [Configurazione Scale-out Repositories](#configurazione-scale-out-repositories)
- [Note relative alla creazione del backup su Veeam](#note-relative-alla-creazione-del-backup-su-veeam)

## Creazione Backup Repository: S3 Compatible

- In *Backup Infrastructure* selezionare *Backup Repositories* quindi **Add Repository**  

![](./attachments/Screenshot%202022-03-10%20at%2009.26.39.png)

- Selezionare la tipologia **Object Storage**  

![](./attachments/Screenshot%202022-03-10%20at%2009.26.51.png)

- Quindi **S3 Compatible**  

![](./attachments/Screenshot%202022-03-10%20at%2009.27.03.png)

- Assegnare il **nome** quindi su *Next*  

![](./attachments/Screenshot%202022-03-10%20at%2009.27.33.png)

> [!CAUTION]
> Mettere la spunta su **Limit concurrent tasks to:** e impostare il valore **2** in caso di <20 vm di cui fare backup offload, **4** in caso di >20 vm di cui fare backup offload

- Configurare l' **Account** utilizzando l' **Endpoint** ricevuto insieme alle credenziali come **Service Point** e la **Region**  
Cliccare quindi su *Add* per aggiungere le credenziali di accesso al Bucket  

![](./attachments/Screenshot%202022-03-10%20at%2009.27.58.png)

- Compilare i campi **Access key** e **Secret key** utilizzando le credenziali ricevute  

![](./attachments/Screenshot%202022-03-10%20at%2009.28.28.png)

- Alternativamente selezionare le credenziali create in precedenza quindi cliccare su *Next*  

![](./attachments/Screenshot%202022-03-10%20at%2009.29.01.png)

- Nella sezione **Bucket** cliccare su **Browse** e, se le credenziali sono state inserite correttamente, verrà mostrato il bucket s3  

![](./attachments/Screenshot%202022-03-10%20at%2009.29.41.png)

- Selezionare il *bucket* quindi cliccare su *Next*  

![](./attachments/Screenshot%202022-03-10%20at%2009.29.51.png)

- Cliccare quindi sul secondo **Browse** ovvero quello legato alla *Folder*  
- Nel caso in cui il bucket non sia mai stato utilizzato occorrerà **creare** una nuova folder cliccando sul tasto *New Folder* quindi selezionarla e cliccare su *Ok*  

![](./attachments/Screenshot%202022-03-10%20at%2009.30.33.png)

- Per configurare la funzionalità di **Immutability** spuntare *”Make recent backups immutable for: XXX days”* e compilare il valore in giorni relativo all' immutabilità dei dati.  

![](./attachments/Screenshot%202022-03-10%20at%2009.30.49.png)

- Cliccare quindi su *Apply* per completare la configurazione

> [!CAUTION]
> La quantità di giorni indicata nel campo *Make recent backups immutable for: XXX days* vincola l’eliminazione dei backup a tale data sia nel **Tier Performance** che nel **Tier Capacity**
>   
> Tale intervallo di tempo **NON** è modificabile successivamente.

## Configurazione Scale-out Repositories

1. Fare tasto DX → Edit sul nome dello Scale-out Repositories  
![](./attachments/Screenshot%202022-03-10%20at%2010.00.26.png)

> [!NOTE]
> Modificare la quantità di giorni nel campo **Move backups to object storage as they age out of the operational restore window** per ridurre lo spazio occupato nel Perfomance Tier

2\. Nella sezione ***Capacity Tier*** mettere la spunta su \*”Extend scale-out backup repository capacity with object storage:”

3\. Selezionare il **Bucket S3** precedentemente creato  

![](./attachments/Screenshot%202022-03-10%20at%2010.01.22.png)

4\. Cliccare su *Apply* quindi su *Finish* per terminare la modifica e applicarla.

> [!INFO]
> Da questo momento tutti i backup che utilizzando questo Scale-out Repository usufruiranno della copia nel **Capacity Tier** con funzionalità **Immutable** attiva

> [!TIP]
> La copia offload del backup verso il bucket s3 appena configurato partirà successivamente al termine del backup nel Perfomance Tier.

## Note relative alla creazione del backup su Veeam

1. Nella selezione dello Storage cliccare su “Advanced”

![](./attachments/Screenshot%202022-05-06%20at%2017.12.39.png)

2\. Nella tab “Storage” alla voce “Storage optimization” selezionare “Local target (large block)” per questioni di ottimizzazione durante l’upload e il recovery dei backup a livello di performance.

![](./attachments/Screenshot%202022-05-06%20at%2017.14.27.png)

![](./attachments/Screenshot%202022-05-06%20at%2017.14.42.png)

3\. In relazione alla configurazione default di Veeam legata al numero di connessioni contemporanee utilizzate per ogni task di backup offload, occorre modificare la seguente chiave di registro:

- `HKEY_LOCAL_MACHINE\SOFTWARE\Veeam\Veeam Backup and Replication\S3ConcurrentTaskLimit`

il cui valore va impostato a ***2***