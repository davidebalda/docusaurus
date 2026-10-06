---
title: "Deploy NethServer su Openstack"
---

### Procedimento

Effettuare il deploy di un’istanza con le seguenti caratteristiche:

- A seconda della soluzione *NethServer* che si vuole andare ad utilizzare, scegliere il **flavor adeguato** basandosi sulla tabella sottostante;

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| #### **Taglio NethServer(\*)** | #### **Flavor Openstack** | #### **vCPU** | #### **RAM** | #### **Storage** |
| **CF-50** | **Openstack As a Service - Region MI2 - Flavor G3-24** | 2   | 4   | 80 GB |
| **CF-100** | **Openstack As a Service - Region MI2 - Flavor G3-48** | 4   | 8   | 120 GB |
| **CF-200** | **Openstack As a Service - Region MI2 - Flavor G3-832** | 8   | 32  | 380 GB |
| **CF-300** | *Contattaci per maggiori informazioni.* | \-  | \-  | \-  |

> *(\*)Il numero del taglio indica una stima di canali voce totali per singolo nodo, nel caso in cui il nodo venisse utilizzato solo per soluzioni NethVoice.*

- Scegliere successivamente l’immagine "OS Rocky Linux 9 x86-64 UEFI SWAP 2025-06" dalla lista dei sistemi operativi;

![image-20260109-162534.png](/kb-assets/d44687c235-image-20260109-162534.png)

- Per la parte di networking selezionare la rete “external\_transparent”, così da assegnare un IP pubblico all’interfaccia della VM;

![image-20260109-163927.png](/kb-assets/8b9a6d73a7-image-20260109-163927.png)

- Selezionare poi il **Security Group adeguato**, per permettere accessi e servizi di rete;

:::warning
Ricordarsi di **aprire le porte necessarie** al funzionamento dei servizi di *NethServer*, come ad esempio l’HTTPS per l’accesso via web.  
Per maggiori info sulla configurazione dei Security Group, fare riferimento a [questa guida](../primi-passi-openstack-as-a-service/gestione-reti-porte-ip-pubblici-router-e-security-group.md).
:::

- **Fondamentale**, per il deploy di *NethServer*, è l’utilizzo del seguente cloud-init, da poter copiare direttamente nella console di Openstack:
```
#cloud-config
ssh_pwauth: False
chpasswd:
  expire: False
  list: |
    root: <password di root>
timezone: UTC
users:
 - name: cloud-user
   ssh_authorized_keys:
     - <your private key>
runcmd:- |curl 'https://raw.githubusercontent.com/NethServer/ns8-core/main/core/install.sh' | bash
```

![image-20260109-170418.png](/kb-assets/f9745c1d04-image-20260109-170418.png)

:::info
La modifica di `<password di root>` e `<your private key>` è **facoltativa**, a seconda delle esigenze.

[!WARNING]
L’autenticazione SSH tramite password è **disabilitata** di default.
:::

- Una volta compilato tutto, si può procedere con la conferma e il deploy dell’istanza;

:::info
Ci vorranno circa 5 minuti per avere la VM operativa.
:::

- Procedere infine con il login via web GUI con le seguenti credenziali di default (**da cambiare al primo accesso**):  
URL d’accesso:  `https://`<server_ip_or_fqdn>`/cluster-admin/`  
Nome utente: `admin`  
Password: `Nethesis,1234`

Tutto pronto, il vostro *NethServer* è ora operativo!