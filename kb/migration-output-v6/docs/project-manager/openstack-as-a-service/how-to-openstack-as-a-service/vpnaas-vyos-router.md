---
title: "VPNaaS - VyOS Router"
---

## Introduzione {#introduzione}

In questa guida vi illustreremo come realizzare un tunnel VPN tra un VyOS router virtuale e il servizio VPN offerto da Openstack as a Service

## Prerequisiti {#prerequisiti}

Per evitare problemi di NAT è consigliabile che la WAN del VyOS sia configurata con un IP Pubblico e quindi non sia presente NAT.

## Guida passo-passo {#guida-passo-passo}

### Configurazione VPNaaS {#configurazione-vpnaas}

Eseguite l'accesso al vostro progetto **Openstack as a Service** e spostatevi nel sotto-menù **Network → VPN.**

![](/kb-assets/991b827d2d-image2019-11-18-9-21-57.png)

Nella compilazione delle varie Policy **Name** e **Description** potete compilarli a vostra discrezione.

- All'interno del form **IKE Policies** cliccate su **\+ ADD IKE POLICY** e compilate i campi come segue:

![](/kb-assets/27af3dbcc9-image2019-11-18-9-24-52.png)

- Cliccate su **ADD** e passate al form **IPsec Policies**.

**All'interno del form IPsec Policies cliccate su +ADD IPSEC POLICY e compilate i campi come segue:**

![](/kb-assets/5c94fb03d6-image2019-11-18-9-29-41.png)

- Cliccate su **ADD** e passate al form **VPN Services.**

**All'interno del form VPN Services cliccate su +ADD VPN SERVICE e compilate i campi:**

![](/kb-assets/b4c46ad5f4-image2019-11-18-13-15-51.png)

- Come **Router** selezionate il Router Virtuale posto davanti alla rete privata in cloud che volete connettere in VPN.Come **Subnet** selezionate la rete privata in cloud che volete connettere in VPN.
- Cliccate su **ADD** e passate al form **Endpoint Groups.**

**All'interno del form Endpoint Groups dovrete creare 2 endpoint, uno per la rete locale e una per la rete in cloud.**

- Cliccate su **+ENDPOINT GROUP.**  
Endpoint per la rete remota (subnet locale dietro al vostro FortiGate):

![](/kb-assets/8d96b20d8c-image2019-11-18-13-18-50.png)

:::info
Nel campo **External System CIDRs** inserire l'indirizzo di rete della rete LAN dietro al vostro FortiGate
:::

#### Endpoint per la rete in cloud (subnet locale dietro il router del Openstack as a Service) {#endpoint-per-la-rete-in-cloud-subnet-locale-dietro-il-router-del-openstack-as-a-service}

![](/kb-assets/791295fff2-image2019-11-18-13-24-42.png)

Infine spostatevi nel form **IPsec Site Connections,** cliccate su **+ADD IPSEC CONNECTION** e compilate i campi come seguono:

![](/kb-assets/8d36d8e16a-image2019-11-18-15-6-14.png)

Cliccate su **ADD**  e passate alla configurazione del vostro VyOS.

Assegnare un IP della lan per management e accesso SSH  
E gateway della lan.  

Su un editor di testo copiare la seguente configurazione:  

```
set esp-group remote-rtr-esp compression 'enable'
set esp-group remote-rtr-esp lifetime '86400'
set esp-group remote-rtr-esp mode 'tunnel'
set esp-group remote-rtr-esp pfs 'enable'
set esp-group remote-rtr-esp proposal 1 encryption 'aes256'
set esp-group remote-rtr-esp proposal 1 hash 'sha1'
set ike-group remote-rtr-ike ikev2-reauth 'no'
set ike-group remote-rtr-ike key-exchange 'ikev1'
set ike-group remote-rtr-ike lifetime '86400'
set ike-group remote-rtr-ike proposal 1 encryption 'aes256'
set ike-group remote-rtr-ike proposal 1 hash 'sha1'
set ipsec-interfaces interface 'eth1'
set site-to-site peer 69.172.98.89 authentication mode 'pre-shared-secret'
set site-to-site peer 69.172.98.89 authentication pre-shared-secret 'Tobagi8687'
set site-to-site peer 69.172.98.89 ike-group 'remote-rtr-ike'
set site-to-site peer 69.172.98.89 local-address '185.214.3.30'
set site-to-site peer 69.172.98.89 tunnel 0 allow-nat-networks 'disable'
set site-to-site peer 69.172.98.89 tunnel 0 allow-public-networks 'enable'
set site-to-site peer 69.172.98.89 tunnel 0 esp-group 'remote-rtr-esp'
set site-to-site peer 69.172.98.89 tunnel 0 local prefix '192.168.52.0/24'
set site-to-site peer 69.172.98.89 tunnel 0 remote prefix '192.168.168.0/24'
set site-to-site peer 69.172.98.89 connection-type respond
set firewall name OUTSIDE-LOCAL rule 32 action 'accept'
set firewall name OUTSIDE-LOCAL rule 32 source address '192.168.52.0/24
```

**Quindi editare:**

Riga 12: inserendo la vostra interfaccia su cui è configurato l’ip pubblico

Riga dalla 13 alla 21: modificare l’indirizzo ip del router di peer con l’ip pubblico del router Openstack as a Service (che ha interfaccia sulla lan da mettere in vpn)

Riga 16: voce local-address utilizzare l’ip pubblico assegnato all’interfaccia del vyos

Riga 20: Local prefix, utilizzare l’ip della lan locale dove collocato il vyos

Riga 21: remote prefix, utilizzare l’ip della lan di openstack

Riga 23: source address è la lan locale del vyos

**Creare una rotta statica utilizzando il gateway associato all’ip pubblico per uscire verso openstack**

**Ora creare un security group che permette l’ingresso di connessioni dall’ip pubblico del vyos su openstack e assegnarla alla porta del router.**