---
title: "VPNaaS - Creazione / Modifica Route statiche su Windows"
---

Descrizione  
NetRouteView è un'alternativa GUI all'utilità di route standard (Route.exe) del sistema operativo Windows. Visualizza l'elenco di tutte le route correnti, inclusi destinazione, maschera, gateway, indirizzo IP dell'interfaccia, valore della metrica, tipo, protocollo, età (in secondi), nome dell'interfaccia e indirizzo MAC.  
NetRouteView consente inoltre di aggiungere facilmente nuove rotte, nonché di rimuovere o modificare le rotte statiche esistenti.  
Avviso: attualmente, questa utility non supporta IPv6.

[](https://www.nirsoft.net/utils/netrouteview.gif)

  

quando si utilizza vpnaas sull' istanza sono generalmente presenti più schede  di rete, 

in questo caso è necessario modificare la metrica della route installata sull'interfaccia vpn per evitare che il traffico in uscita verso internet venga bilanciato tra piu interfacce.

  

![](/kb-assets/30e0987322-screenshot-2020-06-30-at-10-19-41.png)

Per editare la metrica di una rotta esistente selezionare la rotta e fare click con il destro,

cliccare su Modify, Selected Route.

  

  

![](/kb-assets/1b0e9d8812-screenshot-2020-06-30-at-10-20-00.png)

se si vuole aggiungere un nuova route occorre fare click con il destro e selezionare "New Route"

  

![](/kb-assets/27fabcb891-screenshot-2020-06-30-at-10-21-17.png)

## Allegati {#allegati}

[netrouteview.zip](/kb-assets/03e4e77e1a-netrouteview.zip)