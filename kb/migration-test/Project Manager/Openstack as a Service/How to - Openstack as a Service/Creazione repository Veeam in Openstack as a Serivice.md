## Introduzione

Di seguito le istruzioni per configurare la vostra repository veeam in cloud.

Prima di tutto dovrete avere un po’ di confidenza con il Openstack as a Service: nel caso fosse il primo approccio visionate le relative guide [How to - Openstack as a Service](../how-to-openstack-as-a-service.md)

## Guida passo-passo

- Create un istanza windows con l’interfacciamento desiderato a livello di rete:  
[Gestione istanze](../../openstack-as-a-service/primi-passi-openstack-as-a-service/gestione-istanze.md)  
[Gestione reti, porte, ip pubblici, router e security group.](../../openstack-as-a-service/primi-passi-openstack-as-a-service/gestione-reti-porte-ip-pubblici-router-e-security-group.md)
- All’istanza aggiungete un volume delle dimensioni desiderate (di solito un volume di tipo LTS) che fungerà da repository remota:  
[Gestione Volumi](../../openstack-as-a-service/primi-passi-openstack-as-a-service/gestione-volumi.md)
- Configurate un collegamento VPN fra il sito di partenza e la repository remota in cloud. Potete usare software di terze parti oppure predisporre un tunnel site-to-site come in questa guida (specifica per ASA ma facilmente adattabile per il vostro router, firewall o altro VPN end-point):  
[VPNaaS - Cisco ASA Firewall](../how-to-openstack-as-a-service/vpnaas-cisco-asa-firewall.md)
- Dalla console di Veeam, del vostro site principale, recatevi su “Managed Servers” all’interno di “BACKUP INFRASTRUCTURE” e aggiungete il vostro server Windows in cloud, puntanto l’ip raggiungibile in VPN, che diventerà repository esterna. Procedete immettendo le credenziali per l’accesso amministrativo ed installando il componente “Transport”.
- A installazione terminata recatevi su “**Backup Repositories**” in “**BACKUP INFRASTRUCTURE**” e procedete a crearne una nuova.  
Selezionate “*Direct attached storage*”  
![](./attachments/1.PNG)
- “Microsoft Windows” nella schermata successiva;
- Date un nome alla repository;

![](./attachments/2.PNG)

- Selezionate il server appena aggiunto dalla lista e selezionare il disco corrispondente alla repository: nel mio caso il server è “192.168.168.252” raggiunto via SoftEther VPN e il disco è “G:”

![](./attachments/3.PNG)

- Definite le opzioni desiderate:

![](./attachments/4.PNG)

- Nella schermata seguente definite le opzioni desiderate per il **vPower NFS**
- Revisionate ed applicate le modifiche.

![](./attachments/5.PNG)

  

Alla conclusione delle operazioni di inizializzazione la vostra repository è pronta per essere utilizzata come target dei job di backup e backup replication.

  

  

  

> [!NOTE]
> **Sommario**
> 
> 
> 
> - [Introduzione](#introduzione)
> - [Guida passo-passo](#guida-passo-passo)
> -   Filter by label
> * * *
> **Articoli collegati**
> 
> 
> ##### Filter by label
> 
> There are no items with the selected labels at this time.