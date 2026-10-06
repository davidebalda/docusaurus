## Introduzione

In questa guida verrà illustrato come attivare la linea FIBRA P2P tramite il collegamento del router allo switch installato durante la stesura della linea in fibra.

## Prerequisiti

Una volta acquistato il servizio FIBRA P2P, seguiranno diversi interventi che comprendono, la stesura della fibra vera e propria e l'installazione di 2 apparati che servono per la consegna della stessa, per la precisioni verrà installato un cassetto ottico con ingresso e uscita in fibra ottica ed uno switch con 1/2 porte in fibra (SFP) e diverse porte ethernet (comunemente verrà installato uno switch CISCO ME 3400E da 24 porte). Dopo alcuni giorni dall'installazione di questi apparati, previa conferma di collaudo da parte degli installatori vi verrà consegnato il nostro router Cisco per l'attivazione effettiva della linea.

## Guida passo-passo

Ora vi illustreremo come collegare il nostro router Cisco allo Switch di consegna della FIBRA P2P.

### Router Cisco

All'interno della scatola del router Cisco troverete un cavo RJ45 (cavo ethernet o di rete), prendete questo cavo e collegate, una estremità alla presa **GE0/0** e l'altra, alla porta **FE0/1** dello switch Cisco**.**

![](./attachments/Cisco%20Radio.png)

- La porta etichettata come **VDSL/ADSLoPOTS** è dedicata all'eventuale aggiunta di una seconda connettività.
- La porta etichettata come **GE0/1** è dedicata alla LAN del cliente.

- Una  volta collegato il cavo come indicato e acceso il router, dopo alcuni minuti di boot, la connettività dovrebbe essere funzionante. Se così non dovesse essere, contattate il nostro supporto tecnico per verifiche sulla linea.
- L'unica porta dedicata alla LAN del cliente per questo router è la porta etichettata come "**GE0/1**".

> [!NOTE]
> **Sommario**
> 
> 
> - [Introduzione](#introduzione)
> - [Prerequisiti](#prerequisiti)
> - [Guida passo-passo](#guida-passo-passo)
> -   [Router Cisco](#router-cisco)
> * * *
> **Articoli collegati**
> 
> 
> - Page:
> [Attivazione linea FTTC/ADSL](/wiki/spaces/KB/pages/1966257612/Attivazione+linea+FTTC+ADSL)
> - Page:
> [Attivazione linea FIBRA P2P](/wiki/spaces/KB/pages/1966257539/Attivazione+linea+FIBRA+P2P)
> - Page:
> [Attivazione linea FTTH](/wiki/spaces/KB/pages/1966257466/Attivazione+linea+FTTH)
> - Page:
> [Attivazione linea Radio senza DCE](/wiki/spaces/KB/pages/1966257386/Attivazione+linea+Radio+senza+DCE)
> - Page:
> [Attivazione linea Radio con DCE Mikrotik](/wiki/spaces/KB/pages/1966257313/Attivazione+linea+Radio+con+DCE+Mikrotik)