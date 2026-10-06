> [!NOTE]
> Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.

Questa pagina spiega come Collegare il servizio di Veeam Cloud Connect alla repository in cloud di CloudFire e di disporre di uno spazio di archiviazione per i backup scalabile e sicuro.

# Veeam Cloud Connect

Veeam Cloud Connect consente di portare facilmente backup e repliche off-site verso un provider di Backup as a Service (BaaS) o Disaster Recovery as a Service (DRaaS) senza il costo e la complessità della gestione di una seconda infrastruttura.

## Collega Veeam Cloud Connect

Per collegare Veeam Cloud Connect è necessario aver attivato **Cloud Connect**. Non sai come fare? Segui la [**guida**](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/2190213245/Cloud+Connect+-+Veeam+Cloud+Platform#Accedi-a-Cloud-Connect).

![Screenshot 2024-05-13 at 17.01.39.png](./attachments/Screenshot%202024-05-13%20at%2017.01.39.png)

### Collega Veeam Cloud Connect

> [!INFO]
> Il collegamento a Veeam Cloud Connect è necessario per poter usufruire della repository in Cloud.  
> L’hostname [**vcg.cloudfire.it**](http://vcg.cloudfire.it) punta all’indirizzo **IP 185.132.69.58**, porta **6180**.

Per effettuare il collegamento a Veeam Cloud Connect è sufficiente seguire i seguenti passaggi:

1. Effettua l’accesso alla console di Veeam Backup and Replication sulla quale si vuole effettuare il collegamento![](./attachments/BK%20Veeam%20-%20Cloud%20Connect%20-%201.png)
2. Seleziona la voce **Backup Infrastructure** dal menù laterale, in basso a sinistra.
3. Seleziona la voce **Service Providers** dal menù dedicato alla sezione Backup Infrastructure.  
Prosegui cliccando su **Add service provider** presente nella finestra.![](./attachments/BK%20Veeam%20-%20Cloud%20Connect%20-%203.png)
4. Inserisci “[vcg.cloudfire.it](http://vcg.cloudfire.it)” nel campo **DNS name or IP address**, lasciando la porta **6180** come preimpostata.  
Premi **Next** nella finestra di dialogo per proseguire con il collegamento.![](./attachments/BK%20Veeam%20-%20Cloud%20Connect%20-%204.png)
5. Nella finestra di dialogo **Credentials** aggiungi un nuovo set di credenziali premendo **Add**.  
Inserisci username e password che trovi sotto la voce Accessi su Cortex e **Conferma** le credenziali inserite.![](./attachments/BK%20Veeam%20-%20Cloud%20Connect%20-%206.png)
6. Premi su **Next** per proseguire con il collegamento alla repository in Cloud mostrata nella finestra di dialogo **Backup Storage**.![](./attachments/BK%20Veeam%20-%20Cloud%20Connect%20-%207.png)
7. La network extension appliance è una macchina virtuale ausiliaria basata su sistema operativo Linux, che permette la comunicazione tra le macchine della produzione e le repliche di quest'ultime in ambiente Cloud.  
Premi **Apply** per proseguire.![](./attachments/BK%20Veeam%20-%20Cloud%20Connect%20-%208.png)
8. Successivamente vengono mostrate le operazioni applicate per il collegamento della repository in Cloud e il loro tempo di completamento. Prosegui premendo il pulsante **Next**.![](./attachments/BK%20Veeam%20-%20Cloud%20Connect%20-%209.png)
9. Nell’ultima finestra di dialogo viene mostrato il **Summary** delle operazioni svolte dal processo di collegamento di Veeam Cloud Connect. Termina la fase di collegamento guidata premendo sul pulsante **Finish**.![](./attachments/BK%20Veeam%20-%20Cloud%20Connect%20-%2010.png)
10. La repository in Cloud collegata può essere visualizzata nella pagina **Backup Repositories** selezionandola dal menù laterale.  
A questo punto la repository può essere utilizzata come contenitore per i vostri backup.![](./attachments/BK%20Veeam%20-%20Cloud%20Connect%20-%2011.png)

> [!INFO]
> Se il servizio non si attiva o il collegamento fallisce ti invitiamo ad aprire un [**Case**](../../../../../knowledge-base/account-manager/supporto.md) al nostro supporto.