Questa guida mostra come clonare una macchina su Openstack as a Service.

## Prerequisiti

Disporre di almeno una Istanza su Openstack as a Service per poter procedere.

## Come procedere

Per clonare una macchina è sufficiente seguire i seguenti passaggi:

1. Accedi al tenant su Openstack as a Service  
![](./attachments/Public%20Cloud%20-%20Clone%20-%201.png)
2. Premi su **Volumes** nel menu laterale, dopo seleziona la nuova voce **Volumes** per entrare nella pagina dedicata ai volumi del tuo tenant.  
![](./attachments/Public%20Cloud%20-%20Clone%20-%202.png)
3. Sotto la voce **Actions** è possibile andare a eseguire una serie di operazioni per ogni volume. Premi su **Create a snapshot**.  
![](./attachments/Public%20Cloud%20-%20Clone%20-%203.png)
4. Inserisci un **Nome** da associare allo snapshot, premi su **Create volume snapshot**  
Se la macchina risulta accesa verrà mostrato un warning. Proseguire in ogni caso.  
![](./attachments/Public%20Cloud%20-%20Clone%20-%204.png)
5. Una volta terminata la fase di creazione, il nuovo snapshot sarà presente nella pagina **Volume Snapshots**.  
![](./attachments/Public%20Cloud%20-%20Clone%20-%205.png)
6. Da questa pagina è possibile eseguire diverse azioni per ogni snapshot creato. Sotto la voce **Actions** premi su **Launch as istances** sullo snapshot che vuoi clonare come istanza.  
![](./attachments/Public%20Cloud%20-%20Clone%20-%206.png)
  
7. Procedi con la creazione della nuova istanza. Una volta terminato, premi il pulsante **Launch instance**.  
![](./attachments/Public%20Cloud%20-%20Clone%20-%207.png)
8. La nuova istanza sarà visibile nella sezione **Instances**. Attendi che il volume venga montato sulla nuova istanza.  
![](./attachments/Public%20Cloud%20-%20Clone%20-%208.png)
9. Una volta terminati tutti i **Task**, la nuova istanza clone della nostra prima macchina sarà in stato **Active**.  
![](./attachments/Public%20Cloud%20-%20Clone%20-%209.png)