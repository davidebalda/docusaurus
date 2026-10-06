---
title: "Impossibile chiamare o ricevere chiamate"
---

## Problema {#problema}

E' possibile che alcuni telefoni IP non riescano a chiamare o ricevere chiamate pur essendo correttamente registrati sul CloudPBX.

## Prerequisiti {#prerequisiti}

Accesso alla configurazione del telefono IP.

## Possibili cause {#possibili-cause}

Se i telefoni non sono stati configurati utilizzando l'[auto-provisioning](../how-to-cloud-pbx/portale-tenant-cloud-pbx/config-2-2/device-autoprovisioning-2-2.md) (cliccare sul link per la guida per auto-provisionare i telefoni IP), le possibili cause potrebbero le seguenti:

1. Codec del dispositivo configurati erroneamente.
2. Parametri di registrazione configurati erroneamente.

## Soluzione {#soluzione}

### Codec del dispositivo configurati erroneamente {#codec-del-dispositivo-configurati-erroneamente}

Entrare nella configurazione del telefono IP e verificare di aver abilitato gli stessi codec abilitati nel menù di configurazione della corrispondente extension nel CloudPBX:

![](/kb-assets/69beaa9d7b-image2019-5-30-17-23-51.png)

### Parametri di registrazione configurati erroneamente {#parametri-di-registrazione-configurati-erroneamente}

Per alcuni dispositivi (come per esempio le Dect della Gigaset) il CloudPBX, necessita che sia l'**Username** che l'**Authentication Username** vengano specificati nel formato "**TenantID+ExtensionNumber**". 

Esempio qui sotto:

![](/kb-assets/aa7fb15050-image2019-5-30-17-34-38.png)

  

:::warning
Nel caso tutte e 2 le soluzioni proposte non risolvessero il problema, contattate il nostro supporto tecnico compilando il modulo che trovate nel menù a fianco.
:::

  

  

:::note
**Sommario**



- [Problema](#problema)
- [Prerequisiti](#prerequisiti)
- [Possibili cause](#possibili-cause)
- [Soluzione](#soluzione)
-   [Codec del dispositivo configurati erroneamente](#codec-del-dispositivo-configurati-erroneamente)
-   [Parametri di registrazione configurati erroneamente](#parametri-di-registrazione-configurati-erroneamente)
* * *
**Articoli collegati**


- Page:
[Estendere volume Guest OS (Linux) senza riavviare](../../openstack-as-a-service/how-to-openstack-as-a-service/estendere-volume-guest-os-linux-senza-riavviare.md)
- Page:
[Impossibile chiamare o ricevere chiamate](impossibile-chiamare-o-ricevere-chiamate.md)
- Page:
[Portale Extension - Profile](../how-to-cloud-pbx/portale-extension/portale-extension-profile.md)
- Page:
[Portale Extension - Voicemail](../how-to-cloud-pbx/portale-extension/portale-extension-voicemail.md)
- Page:
[Accesso Portale Extension](../how-to-cloud-pbx/portale-extension/accesso-portale-extension.md)
:::