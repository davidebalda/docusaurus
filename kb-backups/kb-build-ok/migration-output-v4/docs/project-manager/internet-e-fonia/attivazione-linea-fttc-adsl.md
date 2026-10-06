---
title: "Attivazione linea FTTC/ADSL"
---

## Introduzione

In questa guida verrà illustrato come attivare la linea FTTC/ADSL tramite il collegamento del router che vi consegneremo

## Prerequisiti

Una volta acquistato il servizio FTTC o ADSL, seguirà l'intervento di un tecnico per la stesura della nuova linea previa appuntamento con il referente indicato in fase di ordinamento del servizio. Terminato l'intervento il tecnico avrà installato una presa telefonica come indicato nell'immagine sottostante:

![](/kb-assets/7886c96bdd-image2019-3-29-11-2-45.png)

Generalmente il tecnico incaricato dovrebbe anche indicare su di essa un codice numerico identificativo della linea, ma questo non sempre viene fatto. Ad intervento terminato, il tecnico procederà al collaudo della linea e se tutto è ok ci farà pervenire notifica di corretta installazione. Dopo alcuni giorni vi verrà consegnato il nostro router.

## Guida passo-passo

Ora vi illustreremo come collegare il nostro router alla presa della linea FTTC/ADSL

### Router Aethra

All'interno della scatola del router Aethra troverete un cavo RJ11 (doppino telefonico), prendete questo cavo e collegate, una estremità alla presa **line** del router Aethra e l'altra alla presa FTTC/ADSL.

![](/kb-assets/6c44bf322e-aethra-a-vdsl.png)

- Tutte e 4 le porte etichettate come **ETH0** sono dedicate alla LAN del cliente.
- La porta etichettata come **ETH1** è dedicata all'eventuale aggiunta di una seconda connettività.

Una volta collegato il cavo come indicato e acceso il router, dopo alcuni minuti di boot, il led frontale etichettato come "**LINE**" comincerà a lampeggiare in rosso, se la linea funziona correttamente dopo un po' smetterà di lampeggiare stabilizzandosi sul colore verde.

- Le porte dedicate alla LAN del cliente per questo router sono tutte e quattro le porte etichettate come "**ETH0**", per la precisione le porte "**1X**", "**2X**", "**3X**" e "**4X**".

### Router Cisco

All'interno della scatola del router Cisco troverete un cavo RJ11 (doppino telefonico), prendete questo cavo e collegate, una estremità alla presa "**VDSL/ADSL o POTS**" del router Cisco e l'altra estremità alla presa FTTC/ADSL.

![](/kb-assets/3322171c08-cisco-a-vdsl.png)

- La porta etichettata come **GE0/1** è dedicata alla LAN del cliente.
- La porta etichettata come **GE0/0** è dedicata all'eventuale aggiunta di una seconda connettività.

Una  volta collegato il cavo come indicato e acceso il router, dopo alcuni minuti di boot, il led etichettato come "**CD**" comincerà a lampeggiare in verde, se la linea funziona correttamente dopo un po' smetterà di lampeggiare stabilizzandosi sempre di verde.

- L'unica porta dedicata alla LAN del cliente per questo router è la porta etichettata come "**GE0/1**".

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Guida passo-passo](#guida-passo-passo)
-   [Router Aethra](#router-aethra)
-   [Router Cisco](#router-cisco)
* * *
**Articoli collegati**


- Page:
[Attivazione linea FTTC/ADSL](attivazione-linea-fttc-adsl.md)
- Page:
[Attivazione linea FIBRA P2P](attivazione-linea-fibra-p2p.md)
- Page:
[Attivazione linea FTTH](attivazione-linea-ftth.md)
- Page:
[Attivazione linea Radio senza DCE](attivazione-linea-radio-senza-dce.md)
- Page:
[Attivazione linea Radio con DCE Mikrotik](attivazione-linea-radio-con-dce-mikrotik.md)
:::