---
title: "VPNaaS - Sonicwall Firewall"
---

## Introduzione {#introduzione}

Questa procedura è rivolta ai service provider/partner che vogliono attivare il servizio per se o per i propri clienti.

Di seguito i semplici passaggi di attivazione del servizio VPN su Openstack as a Service

## Prerequisiti {#prerequisiti}

Per realizzare la VPN occorre avere accesso al Firewall Sonicwall in modalità "administrator"

## Guida passo-passo {#guida-passo-passo}

### Configurazione Openstack as a Service {#configurazione-openstack-as-a-service}

![](/kb-assets/bca58f4224-vpn-2.png)

![](/kb-assets/ac8ee272f8-vpn-1.png)

![](/kb-assets/12b30e9770-vpn-4-1.png)

![](/kb-assets/41f88fdca3-vpn-3.png)

![](/kb-assets/a4708472bc-vpn-5.png)

![](/kb-assets/6fec01d8fe-vpn-4-2.png)

Configurazione Sonicwall

![](/kb-assets/54720b03da-clipboard-september-9-2019-5-40-pm-5.png)

![](/kb-assets/ffa59a8ca3-clipboard-september-9-2019-5-39-pm.png)

:::info
NOTE: Nella sezione Remote Networks l 'oggetto selezionato deve appartenere alla zona VPN !
:::

![](/kb-assets/2d9501a00a-clipboard-september-9-2019-5-39-pm-3.png)

![](/kb-assets/91471b7516-clipboard-september-9-2019-5-39-pm-2.png)

![](/kb-assets/6e83f5459b-clipboard-september-9-2019-5-39-pm-4.png)

:::info
Spuntare Enable keepalive
:::

![](/kb-assets/854dc47d8b-screenshot-2019-09-09-at-17-31-46.png)

:::info
NOTE: La zona di destinazione DEVE essere l'interfaccia specifica ! non utilizzare la zona se è associata a più interfacce
:::

  

  

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Guida passo-passo](#guida-passo-passo)
-   [Configurazione Openstack as a Service](#configurazione-openstack-as-a-service)
* * *
**Articoli collegati**


- Page:
[Recovery VM su Openstack as a Service via Acronis Cyber Backup Service](recovery-vm-su-openstack-as-a-service-via-acronis-cyber-backup-service.md)
- Page:
[VPNaaS - FortiGate Firewall](vpnaas-fortigate-firewall.md)
- Page:
[VPNaaS - Sonicwall Firewall](vpnaas-sonicwall-firewall.md)
- Page:
[Migrazione VM su Openstack as a Service via Acronis Universal Restore](migrazione-vm-su-openstack-as-a-service-via-acronis-universal-restore.md)
- Page:
[Deploy Sophos Firewall su Openstack as a Service](deploy-sophos-firewall-su-openstack-as-a-service.md)
:::