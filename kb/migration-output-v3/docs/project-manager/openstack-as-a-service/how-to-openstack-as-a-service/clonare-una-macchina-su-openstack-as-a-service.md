---
title: "Clonare una macchina su Openstack as a Service"
---

Questa guida mostra come clonare una macchina su Openstack as a Service.

## Prerequisiti

Disporre di almeno una Istanza su Openstack as a Service per poter procedere.

## Come procedere

Per clonare una macchina è sufficiente seguire i seguenti passaggi:

1. Accedi al tenant su Openstack as a Service  
![](/kb-assets/e1b3bb8771-public-cloud-clone-1.png)
2. Premi su **Volumes** nel menu laterale, dopo seleziona la nuova voce **Volumes** per entrare nella pagina dedicata ai volumi del tuo tenant.  
![](/kb-assets/e09e566cf6-public-cloud-clone-2.png)
3. Sotto la voce **Actions** è possibile andare a eseguire una serie di operazioni per ogni volume. Premi su **Create a snapshot**.  
![](/kb-assets/051545103f-public-cloud-clone-3.png)
4. Inserisci un **Nome** da associare allo snapshot, premi su **Create volume snapshot**  
Se la macchina risulta accesa verrà mostrato un warning. Proseguire in ogni caso.  
![](/kb-assets/a1a044e7d6-public-cloud-clone-4.png)
5. Una volta terminata la fase di creazione, il nuovo snapshot sarà presente nella pagina **Volume Snapshots**.  
![](/kb-assets/d907b7897d-public-cloud-clone-5.png)
6. Da questa pagina è possibile eseguire diverse azioni per ogni snapshot creato. Sotto la voce **Actions** premi su **Launch as istances** sullo snapshot che vuoi clonare come istanza.  
![](/kb-assets/ef7e84ec92-public-cloud-clone-6.png)
  
7. Procedi con la creazione della nuova istanza. Una volta terminato, premi il pulsante **Launch instance**.  
![](/kb-assets/42c30fed51-public-cloud-clone-7.png)
8. La nuova istanza sarà visibile nella sezione **Instances**. Attendi che il volume venga montato sulla nuova istanza.  
![](/kb-assets/32357f0d77-public-cloud-clone-8.png)
9. Una volta terminati tutti i **Task**, la nuova istanza clone della nostra prima macchina sarà in stato **Active**.  
![](/kb-assets/75c5511c28-public-cloud-clone-9.png)