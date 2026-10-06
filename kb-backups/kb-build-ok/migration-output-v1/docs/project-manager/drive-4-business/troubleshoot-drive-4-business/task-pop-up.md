---
title: "Task Pop-UP"
---

## Problema

Apparizione di un Pop-up, in basso a destra dello schermo, che mostra il progresso di task che però non avete fatto partire volontariamente. In generale fa riferimento a dei download di file.

![](/kb-assets/c1dbe50a9a-d4b-pop-up.png)

## Possibili cause e soluzioni

Questo Pop-up fa riferimento al download di file di grosse dimensioni. Questo pop-up, solitamente, compare nel momento in cui, il vostro antivirus (durante una scansione) va ad analizzare il contenuto del vostro Cloud Drive. Quando incontra dei file di grosse dimensioni, scarica i file per analizzarli.

Il download del file non impatta sulle prestazioni del Drive, ma se vi infastidisce vedere il pop-up potete agire in 2 modi.

1. Escludere il vostro Cloud Drive dalle scansioni del vostro antivirus, e questa soluzione cambia in base al prodotto anti-virus che utilizzate
2. Potete evitare che venga visualizzato il Pop-Up, qui di seguito vi mostriamo come fare.

## Eliminazione della notifica

- Collegarsi alla pagina [https://drive4business.cloudfire.it](https://drive4business.cloudfire.it), oppure dal portale Cortex cliccare sul pulsante "Gestisci" nella dashboard di **Drive 4 Business**.
- Effettuare l'accesso con un account che abbia i privilegi di **Tenant Admin.**
- Cliccare sull'icona a forma di ingranaggio in alto a destra:  
![](/kb-assets/30084874de-image2019-8-20-10-33-18.png)
- In questa schermata cliccare su **Group Policy:**  
![](/kb-assets/ed5f8cbaed-image2019-8-20-10-34-45.png)
- In questa schermata muoversi nel form **Common Settings,** e cliccare su **Client Setting Manager.**  
![](/kb-assets/b505d24adf-image2019-8-20-10-37-38.png)
- In seguito muoversi nel sotto-menù **Mapped Control Drive,** e selezionare la chebox sull'opzione:  
**Hide Large File Download Tracker (popup progress window on the bottom-right when downloading large files)**  
![](/kb-assets/0d641378f4-image2019-8-20-10-40-19.png)

  

- Riavviate il vostro Client Drive 4 Business.

  

:::note
**Sommario**



- [Problema](#problema)
- [Possibili cause e soluzioni](#possibili-cause-e-soluzioni)
- [Eliminazione della notifica](#eliminazione-della-notifica)
* * *
**Articoli collegati**


- Page:
[Task Pop-UP](task-pop-up.md)
- Page:
[Icone di file e cartelle non presentano lo stato della sync o presentano una "X" grigia (2) (2)](icone-di-file-e-cartelle-non-presentano-lo-stato-della-sync-o-presentano-una-x-grigia-2-2.md)
- Page:
[Guida Base per gli utenti](../how-to-drive-4-business/guida-base-per-gli-utenti.md)
- Page:
[Status dei file](../how-to-drive-4-business/status-dei-file.md)
:::