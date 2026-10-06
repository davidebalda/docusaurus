---
title: "Attivazione linea FTTH"
---

## Introduzione

In questa guida verrà illustrato come attivare la linea FTTH tramite il collegamento del router al Media Converter installato durante la stesura della linea in fibra.

  

## Prerequisiti

Una volta acquistato il servizio FTTH, seguirà l'intervento di un tecnico per l'installazione degli apparati, previa appuntamento con il referente indicato in fase di ordinamento del servizio. Terminato l'intervento il tecnico una tratta un fibra collegata ad un dispositivo (**Media Converter**) che presenterà una porta Ethernet libera che utilizzerete per collegarlo al nostro router.

## Guida passo-passo

Ora vi illustreremo come collegare il nostro router al Media Converter.

### Router Aethra

All'interno della scatola del router Aethra troverete un cavo RJ45 (cavo ethernet o di rete), prendete questo cavo e collegate, un'estremità alla presa **ETH1** del router Aethra e l'altra alla presa ethernet libera del **Media Converter.**

![](/kb-assets/66b7787317-radiodce.png)

- La porta etichettata come LINE è dedicata all'eventuale aggiunta di una seconda connettività.
- Tutte e 4 le porte etichettate come ETH0 del router Aethra sono dedicate alla LAN del cliente. 

Una volta collegato il cavo come indicato e acceso il router, dopo alcuni minuti di boot, il led frontale etichettato come "**LINE**" da spento dovrebbe accendersi e rimanere stabile di colore verde. Se dopo diversi minuti dovesse rimanere spento oppure acceso ma di colore rosso, contattare il nostro servizio tecnico per verifiche sulla linea.

- Le porte dedicate alla LAN del cliente per questo router sono tutte e quattro le porte etichettate come "**ETH0**", per la precisione le porte "**1X**", "**2X**", "**3X**" e "**4X**"

### Router Cisco

All'interno della scatola del router Cisco troverete un cavo RJ45 (cavo ethernet o di rete), prendete questo cavo e collegate, una estremità alla presa **GE0/0** e l'altra, alla porta ethernet libera del **Media Converter.**

![](/kb-assets/bcb6f034a5-cisco-radio.png)

- La porta etichettata come **VDSL/ADSLoPOTS** è dedicata all'eventuale aggiunta di una seconda connettività.
- La porta etichettata come **GE0/1** è dedicata alla LAN del cliente.

Una  volta collegato il cavo come indicato e acceso il router, dopo alcuni minuti di boot, la connettività dovrebbe essere funzionante. Se così non dovesse essere, contattate il nostro supporto tecnico per verifiche sulla linea.

- L'unica porta dedicata alla LAN del cliente per questo router è la porta etichettata come "**GE0/1**"

  

  

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