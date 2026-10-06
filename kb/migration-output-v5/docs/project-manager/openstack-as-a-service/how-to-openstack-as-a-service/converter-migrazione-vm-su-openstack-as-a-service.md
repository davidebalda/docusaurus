---
title: "Converter - Migrazione VM su Openstack as a Service"
---

## Coriolis {#coriolis}

### Accesso Coriolis {#accesso-coriolis}

accedere alla web page di coriolis utilizzando l'IP preso in DHCP con credenziali user : **admin** - password :  **CFCoriolis2019!**

In about-coriolis (in alto a destra, icona account) copiate l'appliance id e fornite il dato al supporto Cloudfire per l'attivazione licenza demo o produzione. 

  

Collegarsi a Coriolis Endpoints > Editare default con credenziali servizio public IP:

Username: ES. 19CF000000  
Password :  
Project name : ES.  19CF000000 - XXXXX  
Save & Validate

![](/kb-assets/8d356dd3c7-screenshot-2019-10-29-at-12-10-44.png)

## Aggiungere Endpoint VMWare {#aggiungere-endpoint-vmware}

Compilare con ip password vcenter. 

![](/kb-assets/5483b797f1-screenshot-2019-10-29-at-12-13-11.png)

Aggiunto i target necessari andare nel menu **Replicas > Create a Replica**

![](/kb-assets/65fb672317-screenshot-2019-10-29-at-12-21-07.png)

  

![](/kb-assets/36da9cfc9a-replica1.png)

  

Next per procedere con la replica "Coriolis Replica"

![](/kb-assets/d8e2cd9dfe-replica2.png)

Selezionare la "Source", in questo caso un endpoint vmware chiamato esx3 come l'host puntato.

![](/kb-assets/8f1add07c5-replica3.png)

Selezionare la compatibilità della libreria in base alla versione di VmWare sugli host/vCenter

Inoltre forzare l'abilitazione del CBT nel caso non fosse attivo sulla macchina replicata (se sottoposta a backup incrementali questo è già in essere).

![](/kb-assets/e1874e0806-replica4.png)

Selezionare la o le VM da replicare.

![](/kb-assets/9dbc375bce-replica5.png)

Selezionare l'endpoint di destinazione

![](/kb-assets/096bb347c9-replica6.png)

Definire quindi nelle Target options (ADVANCED) se eseguire o meno la replica subito.

Definire qual'è lo storage di Default che verrà utilizzato (tipo di storage di destinazione).

Impostare qemu come tipo di Hypervisor.

Definire il Flavor che soddisfi i requisiti richiesti della macchina di partenza.

Decidere se mantenere o meno il MAC Address (necessario in alcuni casi per software che fanno binding della licenza al mac address).

Forzare o meno il DHCP sulla macchina in Openstack as a Service.

Selezionare il security group da applicare all'istanza replicata (il default è assegnato automaticamente).

Selezionare il keypair name da assegnare nel caso sia un'istanza linux based.

![](/kb-assets/5e9621b795-replica7.png)

cloudfire\_public1 sarà il pool di allocazione del floating ip.

Migration flavor name, che definirà le risorse della macchina temporanea "Worker".

Definire la mappatura delle immagini per la migrazione (come da immagine).

Selezionare la network di destinazione, facendo attenzione che abbia accesso a internet.

![](/kb-assets/9e611b7f6f-replica8.png)

Specificare la mappatura delle singole schede di rete.

![](/kb-assets/f78ce6c8da-replica9.png)

Specificare la mappatura dei dischi. Se lasciate Default, verrà utilizzato quello specificato nel punto precedente: "Target oprions".

![](/kb-assets/4e486064b2-replica10.png)

Specificare una schedulazione, nel caso si intendesse effettuare più repliche incrementali prima della migrazione.

![](/kb-assets/07eb197402-replica11.png)

Visualizzare il riepilogo e proseguire.

![](/kb-assets/a4c662e046-replica12.png)

A questo punto potete lanciare la replica.

![](/kb-assets/c5fdc32ae4-replica13.png)

A replica completata, quando siete pronti alla definitiva migrazione potete procedere con la sua creazione: "Create Migration".

Ciò porterà alla creazione dell'istanza in cloud.