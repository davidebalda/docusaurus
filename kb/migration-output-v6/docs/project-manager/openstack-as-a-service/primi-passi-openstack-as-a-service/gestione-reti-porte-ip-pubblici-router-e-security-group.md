---
title: "Gestione reti, porte, ip pubblici, router e security group"
---

## Introduzione {#introduzione}

Questa è la parte più importante in quanto permette la gestione delle comunicazioni del vostro public cloud, internamente e verso il www.

Come per i volumi, si consiglia la preventiva messa in opera della parte di rete ed in seguito procedere al deployment delle istanze per una gestione più granulare e specifica del vostro sistema.

Di seguito il percorso per configurare una nuova rete privata; mettere in comunicazione 2 istanze virtuali su reti private comunicanti via router ed infine esporre un servizio in WAN (semplice ping).

## Prerequisiti {#prerequisiti}

Accesso come administrator al progetto di public cloud su public.cloudfire.it

## Creazione nuova rete privata. {#creazione-nuova-rete-privata}

La situazione di partenza è simile alla seguente:

![](/kb-assets/8b2e12012f-base.jpg)

- Nella sezione "*Networks*" > "**+CREATE NETWORK**" si apre il menù in cui definisco il nome della nuova rete.

![](/kb-assets/3b0e154924-create.jpg)

- Nello stesso sotto-menù viene definita la subnet:

![](/kb-assets/6e31ccfda7-subnet.jpg)

- In questo modo indico gli indirizzi della subnet, lasciando vuoto il gateway (che in automatico sarà considerato il primo IP della subnet) (è anche possibile disabilitarlo con il check-box sottostante)
- La sezione "Subnet Details" permette di definire un range DHCP sulla rete in questione (in formato: Ip\_Iniziale,Ip\_Finale), i DNS da utilizzare, e eventuali rotte statiche.  

![](/kb-assets/64a3e31037-details.jpg)

- Cliccare “**CREATE”**.

![](/kb-assets/c6435fd3f4-aggiunta.jpg)

## Creazione Router {#creazione-router}

Per creare un nuovo router portarsi nella sezione "*Routers*" > "**+CREATE ROUTER**"  

![](/kb-assets/93c99a8521-router21.jpg)

- Cliccare quindi "**CREATE ROUTER**".
- Le opzioni disponibili nel menù a tendina sulla destra sono solo 3:  
**DELETE:** la cancellazione è possibile se non vi sono componenti attivi associati;  
**EDIT**: utile per rinominare il router;  
**CLEAR GATEWAY:** permette di rimuovere la comunicazione con la rete esterna, utile se si vuole una comunicazione isolata intra LAN private.

![](/kb-assets/27559cf951-opzrouter22.jpg)

- Cliccando invece sul nome del Router troviamo il menù che comprende "Overview", Pannello per la definizione di "Static Routes" e "Interfaces", dove definirò le interfacce relative alle subnet private.

![](/kb-assets/4b3b6a24b6-iface24.jpg)

- Cliccando "**+ADD INTERFACE**" si indica la subnet a cui l'interfaccia verrà agganciata ed eventualmente l’IP che gli si vuole attribuire.
- Eseguo le stesse operazioni per quello che riguarda la seconda rete in questione. → In questo caso specifico l'ip (192.168.168.250) che voglio venga assegnato al router, in quanto quello di default è già impegnato dall'altro

## Creazione Porte di Rete {#creazione-porte-di-rete}

Portandosi in "Networks" e cliccando sul nome della rete su cui si vuole definire la porta, si arriva a un menù simile a quello relativo al router: "*Overview", "Subnets*" e "*Ports*". Ci interessa proprio quest'ultima schermata, che riassume tutte le Porte presenti sulla rete presa in considerazione.

- Clicco **"+CREATE PORT**".

![](/kb-assets/61bb37a108-addport3.jpg)

- Qui definisco il nome;
- Specifico il tipo: nel mio caso *FIXED IP*, che definisco sotto. In alternativa si può scegliere la subnet, lasciando il compito al lease DHCP. Oppure non specificare rimanendo con una porta Layer2; si può infatti definire un MAC Address nel campo sottostante.

:::info
Ci occuperemo in seguito della definizione dei "Security Groups" > "CREATE".
:::

## Floating IP, Ip pubblici {#floating-ip-ip-pubblici}

- Sotto "Network" > "Public IPs" clicco "**ALLOCATE IP TO PROJECT**".

![](/kb-assets/9b56a038da-floatip51.jpg)

- Metto una descrizione e procedo con "**ALLOCATE IP**"

![](/kb-assets/864cd0fad7-22222floatip52.jpg)

- Adesso l'IP assegnato in modo randomico può essere rilasciato (se non necessario) oppure associato a un'interfaccia di rete privata. 

![](/kb-assets/1779e87724-associate53.jpg)

- Cliccando **"ASSOCIATE**" si apre infatti la schermata in cui scelgo la porta "**172.81.82.10**" dal menù a tendina (ovvero *portaServer1* nel mio caso).
- Confermare con "**ASSOCIATE**" (sfondo blu). → Ora "server1" (proprietario della porta "portaServer1") è puntabile da WAN via ip pubblico 185.132.70.17 ma non accessibile su nessuna porta.  

## Definizione Security Groups {#definizione-security-groups}

Completati tutti i passaggi e create le istanze (in questo caso Server1 e Server2) seguendo eventualmente la guida [Creazione/gestione istanze e uso delle "Key Pairs"](gestione-istanze.md) , e assegnandogli le interfacce definite nei punti precedenti si arriva alla configurazione desiderata (o quasi). 

![](/kb-assets/04812b2a7e-secgroup61.jpg)

- Definisco un nome significativo e confermo cliccando "**CREATE SECURITY GROUP**".
- Cliccare quindi "**MANAGE RULES**" per portarsi nella schermata con la lista delle regole esistenti all'interno dello specifico gruppo; di default vi sono 2 regole che permettono tutto il traffico in uscita, IPv4 e IPv6.
- Cliccare "**\+ ADD RULE**".
- La prima regola che definisco è quella per aprire il "ping" da WAN.

![](/kb-assets/8611cab499-icmpwan62.jpg)

- Definisco il protocollo nel primo campo, una descrizione, la direzione (ingresso o uscita), e la sorgente: questa può essere rappresentata dal CIDR identificativo della rete (0.0.0.0/0 nel mio caso per indicare "any") oppure un Security Group.

:::info
Se si seleziona un security group, tutte le istanze che presentano quel security group applicato potranno seguire questa regola nei confronti delle altre.
:::

- Creo una seconda regola per permettere al "server2", nell'altra subnet privata di accedere a tutte le porte TCP di "server1".

![](/kb-assets/70c86f18ce-alltcp63.jpg)

![](/kb-assets/7274897113-rules64.jpg)

- Nello stesso modo creo un nuovo security group "Server2" per permettere il traffico nel *verso opposto*.
- Ora non rimane che applicare il Security Group "Server1" all'interfaccia "portaServer1".  
"Network" > "Networks" > click sulla rete in questione (PrivateNetwork2) > "Ports"  
Click su "EDIT PORT" relativo a "portaServer1"  
Sezione "Security Groups"  
Rimuovere il gruppo "default" da "Port Security Groups" e aggiungere il gruppo specifico (come nell'immagine).

![](/kb-assets/53be421931-segapply65.jpg)

- Nel caso in cui si stia applicando il security group a porte già in uso da parte di istanze si può procedere andando sul menù a tendina dell'istanza ci sono due opzioni per modificare i security groups:

![](/kb-assets/15e05adfec-menu66.jpg)

:::info
**Edit Security Groups** permette l'associazione del gruppo direttamente all'istanza.
Mentre l'altro porta alla schermata che comprende tutte le porte, dove eseguire l'assegnazione come nel punto precedente.
:::

![](/kb-assets/031a6c8bd2-total.jpg)

Questa è la topologia finale.

Dall'esterno:

```
PING 185.132.70.17 (185.132.70.17) 56(84) bytes of data.
64 bytes from 185.132.70.17: icmp_seq=1 ttl=57 time=11.3 ms
64 bytes from 185.132.70.17: icmp_seq=2 ttl=57 time=11.3 ms
```

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Creazione nuova rete privata.](#creazione-nuova-rete-privata)
- [Creazione Router](#creazione-router)
- [Creazione Porte di Rete](#creazione-porte-di-rete)
- [Floating IP, Ip pubblici](#floating-ip-ip-pubblici)
- [Definizione Security Groups](#definizione-security-groups)
-   Filter by label
* * *
**Articoli collegati**


##### Filter by label {#filter-by-label}

There are no items with the selected labels at this time.
:::