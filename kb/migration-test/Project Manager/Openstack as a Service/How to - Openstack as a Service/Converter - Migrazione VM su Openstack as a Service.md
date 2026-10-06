## Coriolis

### Accesso Coriolis

accedere alla web page di coriolis utilizzando l'IP preso in DHCP con credenziali user : **admin** - password :  **CFCoriolis2019!**

In about-coriolis (in alto a destra, icona account) copiate l'appliance id e fornite il dato al supporto Cloudfire per l'attivazione licenza demo o produzione. 

  

Collegarsi a Coriolis Endpoints > Editare default con credenziali servizio public IP:

Username: ES. 19CF000000  
Password :  
Project name : ES.  19CF000000 - XXXXX  
Save & Validate

![](./attachments/Screenshot%202019-10-29%20at%2012.10.44.png)

## Aggiungere Endpoint VMWare

Compilare con ip password vcenter. 

![](./attachments/Screenshot%202019-10-29%20at%2012.13.11.png)

Aggiunto i target necessari andare nel menu **Replicas > Create a Replica**

![](./attachments/Screenshot%202019-10-29%20at%2012.21.07.png)

  

![](./attachments/replica1.PNG)

  

Next per procedere con la replica "Coriolis Replica"

![](./attachments/replica2.PNG)

Selezionare la "Source", in questo caso un endpoint vmware chiamato esx3 come l'host puntato.

![](./attachments/replica3.PNG)

Selezionare la compatibilità della libreria in base alla versione di VmWare sugli host/vCenter

Inoltre forzare l'abilitazione del CBT nel caso non fosse attivo sulla macchina replicata (se sottoposta a backup incrementali questo è già in essere).

![](./attachments/replica4.PNG)

Selezionare la o le VM da replicare.

![](./attachments/replica5.PNG)

Selezionare l'endpoint di destinazione

![](./attachments/replica6.PNG)

Definire quindi nelle Target options (ADVANCED) se eseguire o meno la replica subito.

Definire qual'è lo storage di Default che verrà utilizzato (tipo di storage di destinazione).

Impostare qemu come tipo di Hypervisor.

Definire il Flavor che soddisfi i requisiti richiesti della macchina di partenza.

Decidere se mantenere o meno il MAC Address (necessario in alcuni casi per software che fanno binding della licenza al mac address).

Forzare o meno il DHCP sulla macchina in Openstack as a Service.

Selezionare il security group da applicare all'istanza replicata (il default è assegnato automaticamente).

Selezionare il keypair name da assegnare nel caso sia un'istanza linux based.

![](./attachments/replica7.PNG)

cloudfire\_public1 sarà il pool di allocazione del floating ip.

Migration flavor name, che definirà le risorse della macchina temporanea "Worker".

Definire la mappatura delle immagini per la migrazione (come da immagine).

Selezionare la network di destinazione, facendo attenzione che abbia accesso a internet.

![](./attachments/replica8.PNG)

Specificare la mappatura delle singole schede di rete.

![](./attachments/replica9.PNG)

Specificare la mappatura dei dischi. Se lasciate Default, verrà utilizzato quello specificato nel punto precedente: "Target oprions".

![](./attachments/replica10.PNG)

Specificare una schedulazione, nel caso si intendesse effettuare più repliche incrementali prima della migrazione.

![](./attachments/replica11.PNG)

Visualizzare il riepilogo e proseguire.

![](./attachments/replica12.PNG)

A questo punto potete lanciare la replica.

![](./attachments/replica13.PNG)

A replica completata, quando siete pronti alla definitiva migrazione potete procedere con la sua creazione: "Create Migration".

Ciò porterà alla creazione dell'istanza in cloud.