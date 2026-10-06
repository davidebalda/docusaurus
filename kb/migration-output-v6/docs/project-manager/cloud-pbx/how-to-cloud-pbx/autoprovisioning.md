---
title: "Autoprovisioning"
---

## Introduzione {#introduzione}

Accedete al **[Portale Tenant](https://cloudfireit.atlassian.net/wiki/pages/createpage.action?spaceKey=~239475519&title=Portale%20Tenant)**  ed accedete al sotto menù **[Config → Device](portale-tenant-cloud-pbx/config-2-2/device-autoprovisioning-2-2.md).**

In questo sotto menù è possibile configurare l'**auto-provisioning** dei telefoni IP.

## Prerequisiti {#prerequisiti}

Per auto-provisionare i telefoni sip dovete collegarli ad una rete che abbia la possibilità di comunicare con la sub-net **185.132.68.112/28**, per cui controllate le regole firewall per la rete telefonica.

Per fare in modo che i telefoni si possano provisionare dovete aggiungere l'**option 66 (tipologia ascii)** all'interno del DHCP server che distribuisce gli IP alla rete telefonica, il valore da assegnare a questa opzione è il seguente:

**[http://{user}:{password}@pbx.cloudfire.it/hpm/provision/](https://hpmaccess:7488R!9TREIq@pbx.cloudfire.it/hpm/provision/)**

## Guida passo-passo {#guida-passo-passo}

Ora vi illustreremo come eseguire l'associazione Dispositivo → Extension

## Funzionalità aggiuntive {#funzionalita-aggiuntive}

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Guida passo-passo](#guida-passo-passo)
- [Funzionalità aggiuntive](#funzionalita-aggiuntive)

* * *
**Articoli collegati**



- Page:
[Impossibile chiamare o ricevere chiamate](../troubleshoot-cloud-pbx/impossibile-chiamare-o-ricevere-chiamate.md)
- Page:
[SNOM - Factory Reset](snom-factory-reset.md)
- Page:
[Portale Extension - Profile](portale-extension/portale-extension-profile.md)
- Page:
[Portale Extension - Opzioni e Funzionalità](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/1966256717/Portale+Extension+-+Opzioni+e+Funzionalit)
- Page:
[Funzionalità Call Flow Control - Day/Night](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/1966256564/Funzionalit+Call+Flow+Control+-+Day+Night)
:::