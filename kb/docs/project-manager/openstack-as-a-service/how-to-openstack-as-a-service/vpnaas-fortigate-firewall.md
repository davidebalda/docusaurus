---
title: "VPNaaS - FortiGate Firewall"
---

## Introduzione {#introduzione}

In questa guida vi illustreremo come realizzare un tunnel VPN tra un firewall locale Fortigate e il servizio VPN offerto da Openstack as a Service

## Prerequisiti {#prerequisiti}

Per evitare problemi di NAT è consigliabile che la WAN del FortiGate sia configurata con un IP Pubblico e quindi non sia presente NAT tra il firewall stesso e il router d''accesso a Internet.

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

Cliccate su **ADD**  e passate alla configurazione del vostro FortiGate.

### Configurazione FortiGate {#configurazione-fortigate}

#### **Abilitare la funzione di Policy-based IPsec VPN.** {#abilitare-la-funzione-di-policy-based-ipsec-vpn}

Entrare nella GUI del vostro FortiGate, spostarsi nel sotto-menù **System → Feature Visibility** e abilitare l'opzione **Policy-based IPsec VPN:**

![](/kb-assets/fd23fc0d56-image2019-11-18-15-10-10.png)

#### Creare l'oggetto "address per la rete remota" {#creare-l-oggetto-address-per-la-rete-remota}

Spostarsi nel sotto-menù **Policy & Objects → Addresses,** cliccare su **+Create New** ed inserire l'indirizzo IP della subnet privata in cloud.

![](/kb-assets/0fa7a25034-image2019-11-18-15-14-58.png)

#### Creare il tunnel VPN {#creare-il-tunnel-vpn}

Spostarsi nel sotto-menù **VPN → IPsec Wizard,** cliccate su **Custom** ed inserite il nome del vostro Tunnel VPN: 

![](/kb-assets/7dc69bfdce-image2019-11-18-15-35-19.png)

Cliccate su **Next** e compilate i vari form come segue:

![](/kb-assets/8a536a3a0e-image2019-11-18-15-39-29.png)

![](/kb-assets/f0ab54b32a-image2019-11-18-15-39-51.png)

![](/kb-assets/d9b9937b6e-image2019-11-18-15-40-22.png)

![](/kb-assets/1ba997537a-image2019-11-18-15-40-40.png)

![](/kb-assets/f75442e00a-image2019-11-18-15-41-33.png)

#### Creare le ACL per permettere il traffico Cloud ↔ LAN attraverso il Tunnel {#creare-le-acl-per-permettere-il-traffico-cloud-lan-attraverso-il-tunnel}

Spostarsi nel sotto-menù **Policy & Objects → IPv4 Policy,** cliccare su **+Create New** e compilare i campi come segue:

**LAN → Cloud**

![](/kb-assets/86c7c6a0aa-image2019-11-18-15-45-56.png)

Creare una seconda ACL per il traffico inverso:

**Cloud → LAN**

![](/kb-assets/bdb88e7320-image2019-11-18-15-46-51.png)

#### Creare rotta statica per traffico VPN {#creare-rotta-statica-per-traffico-vpn}

Spostatevi nel sotto-manù **Network → Static Routes,** cliccate su **\+ Create New** e compilate i campi come segue:

![](/kb-assets/2b0bb7e301-image2019-11-18-15-49-55.png)

:::info
Se durante la creazione della rotta dovesse richiedervi il **Gateway,** lasciate quello di default cioè **0.0.0.0**
:::

Terminate entrambe le configurazioni per verificare che il tunnel sia correttamente **Up & Running** potete controllare qua:

- **FortiGate:** sotto-menù **VPN → IPsec Tunnels,** nella colonna **Status** dovreste vedere il simbolo ![](/kb-assets/4d8aa452b7-image2019-11-18-15-54-54.png)
  
![](/kb-assets/cde7628c4f-image2019-11-18-15-56-31.png)
- Oppure nel sotto-menù **Monitor → IPsec Monitor,** nella colonna **Status** dovreste vedere il simbolo ![](/kb-assets/4d8aa452b7-image2019-11-18-15-54-54.png)
- **Openstack as a Service:** nel sotto-menù **Network → VPN** all'interno del form **IPsec Site Connection** in corrispondenza della colonna Status dovreste vedere ![](/kb-assets/1737a02d72-image2019-11-18-16-1-10.png)

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Guida passo-passo](#guida-passo-passo)
-   [Configurazione VPNaaS](#configurazione-vpnaas)
  
  -   [Endpoint per la rete in cloud (subnet locale dietro il router del Openstack as a Service)](#endpoint-per-la-rete-in-cloud-subnet-locale-dietro-il-router-del-openstack-as-a-service)
-   [Configurazione FortiGate](#configurazione-fortigate)
  
  -   [Abilitare la funzione di Policy-based IPsec VPN.](#abilitare-la-funzione-di-policy-based-ipsec-vpn)
  
  -   [Creare l'oggetto "address per la rete remota"](#creare-l-oggetto-address-per-la-rete-remota)
  
  -   [Creare il tunnel VPN](#creare-il-tunnel-vpn)
  
  -   [Creare le ACL per permettere il traffico Cloud ↔ LAN attraverso il Tunnel](#creare-le-acl-per-permettere-il-traffico-cloud-lan-attraverso-il-tunnel)
  
  -   [Creare rotta statica per traffico VPN](#creare-rotta-statica-per-traffico-vpn)
* * *
**Articoli collegati**


- Page:
[VPNaaS - FortiGate Firewall](vpnaas-fortigate-firewall.md)
- Page:
[VPNaaS - Sonicwall Firewall](vpnaas-sonicwall-firewall.md)
:::