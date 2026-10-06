## Introduzione

Questa procedura è rivolta ai service provider/partner che vogliono attivare il servizio per se o per i propri clienti.

Di seguito i semplici passaggi di attivazione del servizio VPN su Openstack as a Service

## Prerequisiti

Per realizzare la VPN occorre avere accesso al Firewall Sonicwall in modalità "administrator"

## Guida passo-passo

### Configurazione Openstack as a Service

![](./attachments/VPN%202.png)

![](./attachments/VPN%201.png)

![](./attachments/VPN%204.1.png)

![](./attachments/VPN%203.png)

![](./attachments/VPN%205.png)

![](./attachments/VPN%204.2.png)

Configurazione Sonicwall

![](./attachments/Clipboard%20-%20September%209,%202019%205_40%20PM_5.png)

![](./attachments/Clipboard%20-%20September%209,%202019%205_39%20PM.png)

> [!INFO]
> NOTE: Nella sezione Remote Networks l 'oggetto selezionato deve appartenere alla zona VPN !

![](./attachments/Clipboard%20-%20September%209,%202019%205_39%20PM_3.png)

![](./attachments/Clipboard%20-%20September%209,%202019%205_39%20PM_2.png)

![](./attachments/Clipboard%20-%20September%209,%202019%205_39%20PM_4.png)

> [!INFO]
> Spuntare Enable keepalive

![](./attachments/Screenshot%202019-09-09%20at%2017.31.46.png)

> [!INFO]
> NOTE: La zona di destinazione DEVE essere l'interfaccia specifica ! non utilizzare la zona se è associata a più interfacce

  

  

> [!NOTE]
> **Sommario**
> 
> 
> 
> - [Introduzione](#introduzione)
> - [Prerequisiti](#prerequisiti)
> - [Guida passo-passo](#guida-passo-passo)
> -   [Configurazione Openstack as a Service](#configurazione-openstack-as-a-service)
> * * *
> **Articoli collegati**
> 
> 
> - Page:
> [Recovery VM su Openstack as a Service via Acronis Cyber Backup Service](/wiki/spaces/KB/pages/2012610561/Recovery+VM+su+Openstack+as+a+Service+via+Acronis+Cyber+Backup+Service)
> - Page:
> [VPNaaS - FortiGate Firewall](/wiki/spaces/KB/pages/1966249067/VPNaaS+-+FortiGate+Firewall)
> - Page:
> [VPNaaS - Sonicwall Firewall](/wiki/spaces/KB/pages/1966248911/VPNaaS+-+Sonicwall+Firewall)
> - Page:
> [Migrazione VM su Openstack as a Service via Acronis Universal Restore](/wiki/spaces/KB/pages/1966248673/Migrazione+VM+su+Openstack+as+a+Service+via+Acronis+Universal+Restore)
> - Page:
> [Deploy Sophos Firewall su Openstack as a Service](/wiki/spaces/KB/pages/1966248396/Deploy+Sophos+Firewall+su+Openstack+as+a+Service)