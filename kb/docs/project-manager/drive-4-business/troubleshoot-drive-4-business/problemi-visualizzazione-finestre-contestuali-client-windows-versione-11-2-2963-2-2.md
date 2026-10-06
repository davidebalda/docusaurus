---
title: "Problemi visualizzazione finestre contestuali Client Windows versione >= 11.2.2963 (2) (2)"
---

## Problema {#problema}

Nel nuovo client windows le finestre dei menù contestuali, come la condivisione di un link pubblico oppure l'apertura del portale web vengono gestite da un motore interno e non più dal browser predefinito del sistema operativo.

In alcuni casi possono esserci problemi con il caricamento di tali pagine (principalmente un loading che non giunge mai a termine).

  

## Possibili cause e soluzioni {#possibili-cause-e-soluzioni}

Una possibile causa è la corruzione dei file nel seguente percorso: C:\\Users\\`<vostro utente>`\\AppData\\Local\\gbin\\

I 2 file sono : 

DotNetBrowser.Chromium32.dll di dimensione 65,943 KB

e

DotNetBrowser.Chromium64.dll di dimensione 68,730 KB

  

Nel caso ledimensioni fossero diverse oppure ne mancasse uno:

- cancellatelo/i
- chiudete il client drive4business
- riaprite il client
- verificate che i due file vengano ricreati (ci vorranno alcuni minuti, dipende dalla velocità della connessione)

A questo punto il problema dovrebbe essere risolto.

  

[](https://cloudfireit.atlassian.net/wiki/plugins/servlet/confluence/placeholder/unknown-macro?name=easy-heading-free&locale=en_US&version=2)

  

:::note
**Articoli collegati**


##### Filter by label {#filter-by-label}

There are no items with the selected labels at this time.
:::