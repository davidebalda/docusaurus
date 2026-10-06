## Problema

E' possibile che sul client Windows di Drive4Business le icone di cartelle e file non visualizzino più lo stato della sync oppure al loro posto venga visualizzata una X (croce) grigia al loro posto.

Questo è solo un bug grafico, la sincronizzazione dovrebbe funzionare correttamente.

![](./attachments/image2019-10-23_11-31-20.png)

## Possibili cause e soluzioni

Per indicare graficamente lo status di sincronizzazione di un file, Drive4Business, utilizza quelli che vengono chiamati **overlay** delle icone, e che hanno un significato ben preciso (consultare la guida **Status dei** **file**).  Il problema è che, almeno per il momento, **Windows** **supporta al massimo la gestione di 15 tipi diversi di questi overlay,** se sulla macchina, dove è installato il client di Drive4Business, sono installati altri Drive come Drop Box o One Drive, può succedere che gli **overlay** di questi altri Drive vadano in priorità su quelli di Drive4Business e questo causa la scomparsa di questi overlay, o più frequentemente, vengano sostituiti da una **X grigia.**

Per ovviare a questo problema dovete, o eliminare gli **overlay** che non vi servono, oppure mettere in priorità quelli di Drive4Business rispetto agli altri. Per fare questo seguite la guida sottostante:

## Guida passo passo

> [!NOTE]
> **Sommario**
> 
> 
> 
> - [Problema](#problema)
> - [Possibili cause e soluzioni](#possibili-cause-e-soluzioni)
> - [Guida passo passo](#guida-passo-passo)
> 
> * * *
> **Articoli collegati**
> 
> 
> 
> - Page:
> [Task Pop-UP](/wiki/spaces/KB/pages/1966252456/Task+Pop-UP)
> - Page:
> [Reset MAC Client Cache](/wiki/spaces/KB/pages/1966252422/Reset+MAC+Client+Cache)
> - Page:
> [Problemi visualizzazione finestre contestuali Client Windows versione >= 11.2.2963 (2) (2)](/wiki/spaces/KB/pages/1966252404/Problemi+visualizzazione+finestre+contestuali+Client+Windows+versione+11.2.2963+2+2)
> - Page:
> [Icone di file e cartelle non presentano lo stato della sync o presentano una "X" grigia (2) (2)](/wiki/spaces/KB/pages/1966252352/Icone+di+file+e+cartelle+non+presentano+lo+stato+della+sync+o+presentano+una+X+grigia+2+2)
> - Page:
> [Guida Base per gli utenti](/wiki/spaces/KB/pages/1966252158/Guida+Base+per+gli+utenti)