---
title: "Mac Client, errori con FUSE su Mac OSX High Sierra e Mojave"
---

## Problema

Può capitare che nell'installazione del Mac Client per D4B, possano essere riportati degli errori da FUSE. 

- Errore sulla compatibilità:

![](/kb-assets/145db0b3c0-image2019-8-6-9-32-3.png)

- Errore su permessi e sicurezza

![](/kb-assets/a8701fdaf2-image2019-8-6-9-33-8.png)

## Possibili cause e soluzioni

FUSE (Filesystem in Userspace) è un software open source che estende le funzionalità di Mac OS per la gestione dei file, come per esempio il supporto per NTFS e altri file system. Il client Mac di Drive 4 Business di basa su FUSE per montare l'unità Cloud Drive.

Per risolvere i vari problemi vi illustriamo come procedere:

:::warning
**Attenzione per gli utilizzatori di Mac OSX 10.14.5**
Il recente upgrade rilasciato il 13 Maggio 2019, ha aumentato i parametri di sicurezza e quindi potrebbe capitare che vengano segnalati problemi durante l'installazione, come quello indicato sopra.
Per risolvere la problematica è necessario scaricare l'ultima versione aggiornata del client, che potete trovare qui: [most recent build of the mac client](https://tinyurl.com/y49wkvj6).
:::

## Errore sulla compatibilità

In caso venga segnalato un problema di compatibilità con la versione di FUSE verificare di aver scaricato l'ultima versione del client compatibile con la vostra versione di MacOS.

Dalla Dashboard di Drive 4 Business presente su Cortex è già presente un link con la versione più aggiornata del client:

![](/kb-assets/8f3b452f42-image2019-8-6-12-23-38.png)

Se seguite l'accesso direttamente alla dashboard di Drive 4 Business, potrete trovare il link di download qua:

![](/kb-assets/3fb40a7e39-image2019-8-6-12-19-0.png)

Nella pagina che seguirà assicuratevi di scaricare il client compatibile con la vostra versione di MacOS:

![](/kb-assets/3d72ea598d-image2019-8-6-12-24-15.png)

## Errore su permessi e sicurezza

In caso si presenti il problema su permessi o sicurezza verificare e in caso aggiornare la propria versione del client come indicato sopra.

Se l'aggiornamento non risolva la problematica, riprovare ad avviare l'installazione dopo un reboot del vostro MAC.

Se anche questa procedura non risolve la problematica controllate quanto segue:

- Verificate le **System Preferences → Security & Privacy** del vostro MAC, sotto la tab **Privacy**, assicuratevi che tutto ciò che è etichettato come "**Cloud Drive**", "**Gladinet**" e/o "**FUSE**" è abilitato all'esecuzione senza restrizioni

  

Se anche questa soluzione non risolve il problema contattate il nostro supporto tecnico.

  

  

:::note
**Sommario**


- [Problema](#problema)
- [Possibili cause e soluzioni](#possibili-cause-e-soluzioni)
- [Errore sulla compatibilità](#errore-sulla-compatibilit)
- [Errore su permessi e sicurezza](#errore-su-permessi-e-sicurezza)
* * *
**Articoli collegati**


- Page:
[Reset MAC Client Cache](reset-mac-client-cache.md)
- Page:
[Problemi visualizzazione finestre contestuali Client Windows versione >= 11.2.2963 (2) (2)](problemi-visualizzazione-finestre-contestuali-client-windows-versione-11-2-2963-2-2.md)
- Page:
[Mac Client, errori con FUSE su Mac OSX High Sierra e Mojave](mac-client-errori-con-fuse-su-mac-osx-high-sierra-e-mojave.md)
- Page:
[Status dei file](../how-to-drive-4-business/status-dei-file.md)
- Page:
[Sincronizzazione automatica dei Permessi tramite Server Agent](../how-to-drive-4-business/drive4business-ibrido-hybrid-d4b/sincronizzazione-automatica-dei-permessi-tramite-server-agent.md)
:::