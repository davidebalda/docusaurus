## Introduzione

Accedete al **[Portale Tenant](/wiki/pages/createpage.action?spaceKey=~239475519&title=Portale%20Tenant)**  ed accedete al sotto menù **[Config → Device](../how-to-cloud-pbx/portale-tenant-cloud-pbx/config-2-2/device-autoprovisioning-2-2.md).**

In questo sotto menù è possibile configurare l'**auto-provisioning** dei telefoni IP.

## Prerequisiti

Per auto-provisionare i telefoni sip dovete collegarli ad una rete che abbia la possibilità di comunicare con la sub-net **185.132.68.112/28**, per cui controllate le regole firewall per la rete telefonica.

Per fare in modo che i telefoni si possano provisionare dovete aggiungere l'**option 66 (tipologia ascii)** all'interno del DHCP server che distribuisce gli IP alla rete telefonica, il valore da assegnare a questa opzione è il seguente:

**[http://{user}:{password}@pbx.cloudfire.it/hpm/provision/](https://hpmaccess:7488R!9TREIq@pbx.cloudfire.it/hpm/provision/)**

## Guida passo-passo

Ora vi illustreremo come eseguire l'associazione Dispositivo → Extension

## Funzionalità aggiuntive

> [!NOTE]
> **Sommario**
> 
> 
> 
> - [Introduzione](#introduzione)
> - [Prerequisiti](#prerequisiti)
> - [Guida passo-passo](#guida-passo-passo)
> - [Funzionalità aggiuntive](#funzionalit-aggiuntive)
> 
> * * *
> **Articoli collegati**
> 
> 
> 
> - Page:
> [Impossibile chiamare o ricevere chiamate](/wiki/spaces/KB/pages/1966256951/Impossibile+chiamare+o+ricevere+chiamate)
> - Page:
> [SNOM - Factory Reset](/wiki/spaces/KB/pages/1966256905/SNOM+-+Factory+Reset)
> - Page:
> [Portale Extension - Profile](/wiki/spaces/KB/pages/1966256865/Portale+Extension+-+Profile)
> - Page:
> [Portale Extension - Opzioni e Funzionalità](/wiki/spaces/KB/pages/1966256717/Portale+Extension+-+Opzioni+e+Funzionalit)
> - Page:
> [Funzionalità Call Flow Control - Day/Night](/wiki/spaces/KB/pages/1966256564/Funzionalit+Call+Flow+Control+-+Day+Night)