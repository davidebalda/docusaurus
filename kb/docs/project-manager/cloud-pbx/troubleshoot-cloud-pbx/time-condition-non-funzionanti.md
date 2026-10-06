---
title: "Time Condition non funzionanti"
---

## Problema {#problema}

Le regole temporali che avete impostato non funzionano correttamente e quindi agli orari e i giorni indicati non vengono rispettate le regole impostate.

## Possibili cause e soluzioni {#possibili-cause-e-soluzioni}

Spesso il problema è dovuto una completa comprensione di come il PBX interpreta e va a controllare i range impostati nelle time condition. Di seguito un grafico ed un esempio di come procedere in questo caso.

## Diagramma di flusso di decisione delle time condition {#diagramma-di-flusso-di-decisione-delle-time-condition}

![](/kb-assets/0e5a282462-tc-fc.png)

## Esempio {#esempio}

ipotizziamo che dobbiate impostare una chiusura estiva al 06 Agosto al 09 Settembre, probabilmente vi verrebbe da impostarla come segue.

![](/kb-assets/fa5e5efc54-image2020-9-9-14-48-45.png)

Ma se seguiamo il grafico sopra e una chiamata arrivasse il giorno lunedì 17/08 alle 15:00, vedete che il primo check (quello del time) sarebbe rispettato, mentre il secondo no, in quanto la chiamata è arrivata di lunedì.

Per configurare correttamente questa finestra temporale dovete configurare 2 regole distinte 1 per Agosto e 1 per Settembre, come nelle immagini sotto.

![](/kb-assets/554919e762-image2020-9-9-14-53-3.png)

![](/kb-assets/2cd3ecf8a8-image2020-9-9-14-53-48.png)

Così vedrete che, se per prova, ipotizzate l'arrivo di una chiamata all'interno della finestra temporale voluta, seguendo il grafico sopra almeno una delle 2 regole andrà sempre ad essere metchata.

:::note
**Sommario**



- [Problema](#problema)
- [Possibili cause e soluzioni](#possibili-cause-e-soluzioni)
- [Diagramma di flusso di decisione delle time condition](#diagramma-di-flusso-di-decisione-delle-time-condition)
- [Esempio](#esempio)
* * *
**Articoli collegati**


- Page:
[Time Condition (2) (2)](../how-to-cloud-pbx/portale-tenant-cloud-pbx/timing/time-condition-2-2.md)
- Page:
[CID Routing](../how-to-cloud-pbx/portale-tenant-cloud-pbx/call-routing/cid-routing.md)
- Page:
[DID Routing](../how-to-cloud-pbx/portale-tenant-cloud-pbx/call-routing/did-routing.md)
- Page:
[Primi passi - Cloud PBX](../primi-passi-cloud-pbx.md)
:::