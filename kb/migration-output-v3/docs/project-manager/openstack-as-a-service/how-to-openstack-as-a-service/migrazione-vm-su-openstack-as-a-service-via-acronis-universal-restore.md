---
title: "Migrazione VM su Openstack as a Service via Acronis Universal Restore"
---

## Introduzione

La procedura di migrazione via Acronis Universal Restore a Openstack as a Service è un backup con conseguente recover.

## Prerequisiti

Per poter funzionare, la macchina necessita dei driver VirtIO in modo da poter riconoscere i dischi e le schede di rete. Linux solitamente ha solitamente i driver già installati. Per Windows invece se non già installati potete installarli tramite l’univeral restore prendendoli da una cartella inserita nella macchina stessa precedentemente al backup che volete recuperare.

I driver VirtIO per Windows li potete scaricare da qua: [https://pve.proxmox.com/wiki/Windows\_VirtIO\_Drivers](https://pve.proxmox.com/wiki/Windows_VirtIO_Drivers)

Su Openstack as a Service  procedere alla creazione di un volume (o più in caso di molteplici dischi), di dimensioni uguali o superiori, che sarà la destinazione del recovery dell’originale.

 La configurazione di rete è relativa al risultato che si vuole ottenere:

- Replica della rete originale, con conseguente creazione porta con l’IP corrispondente
- Riconfigurazione della macchia in cloud con ip dinamico

Avendo già un backup della sorgente si può procedere.

## Guida passo-passo

- Creare un’istanza a partire dall’immagine “Acronis\_BaaS\_UniversalRestore”, utilizzando il flavor che preferite (compatibilmente con le caratteristiche della macchina che state migrando), network con libero accesso a internet, disco di boot della stessa dimensione o più grande rispetto al disco di origine e senza l’utilizzo di “Key Pair” per l’autenticazione.![](/kb-assets/9dbc003335-1.png)
- A istanza creata, se la macchina d’origine prevedeva ulteriori dischi provvedete a crearli nella sezione **Volumes--> Volumes** e conseguentemente collegare i volumi di destinazione precedentemente creato (attach volume nella tendina delle operazioni) e riavviare.  
![](/kb-assets/89dee3feba-2.png)

:::info
Tutte le operazioni sono eseguite via console su Openstack as a Service.
:::

- Una volta terminata la configurazione della macchina, passate in console e selezionare “**Manage this machine locally**”.  
![](/kb-assets/b1cccbc3a0-3.png)
- Recarsi sotto “**Tools**” -> “**Configure Network**” e verificare che l’ip sia assegnato correttamente all’interfaccia di rete. In caso contrario impostatelo manualmente affinché sia concorde alle impostazioni della porta di rete su cui risiede.  
a questo punto potete procedere con il restore della VM.  
- Cliccare quindi su “**Recover**”.  

![](/kb-assets/938ffd6707-4.png)

- Sotto “**What to recover**” cliccate sulla sezione “**Required**”.![](/kb-assets/2d653d965f-5.png)

- Qui cliccate su “**Browse…**” e nella schermata successiva, in “**Cloud storage**” effettuate il login con le vostre credenziali di Acronis Cyber Backup.  
![](/kb-assets/ab11a1c9e2-6.png)

- Potrete quindi selezionare la cartella in cloud corrispondente al vostro tenant e cliccare su OK per proseguire.
- Qui selezionate l’archivio relativo alla macchina da recuperare, il recovery point che vi interessa, visualizzate il tipo di “**Backup contents**” come “**Disks**” e selezionate il disco da recuperare.  
![](/kb-assets/6c23023e84-7.png)
- In caso di un solo disco/volume di destinazione, l’assegnazione origine-destinazione avviene automaticamente. Altrimenti se si vuole personalizzare l’assegnazione, lo si può fare nell’opzione specifica a sinistra.  
![](/kb-assets/d0f71f486a-8.png)

- Cliccare quindi **ok** per far partire il task.
- Alla fine del recovery job (**Result Succeeded**) chiudete la schermata **ma aspettate ad eseguire il reboot della macchina**![](/kb-assets/3e6e803174-9.png)
- Se la macchina sorgente non aveva installati i driver VirtIO procediamo con l’inject tramite **Universal Restore:**
- Cliccate su Universal Restore e andate a recuperare i driver all’interno della sottocartella corrispondente al vostro sistema operativa per quanto riguarda i volumi (viostor e vioscsi)  
![](/kb-assets/c1916996f6-image-20220615-125220.png)

:::warning
Durante l’universal restore (quindi l’applicazione dei driver) potrebbe apparire un errore con richiesta di effettuare un’azione. Cliccate su ignora e proseguite.
:::

![](/kb-assets/5d7bd060b2-image-20221007-092852.png)

- Terminato l’**Universal Restore** potete riavviare la macchina. Al riavvio dovrebbe effettuare il boot con il sistema operativo recuperato.

:::note
**Sommario**


- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Guida passo-passo](#guida-passo-passo)
-   Filter by label
* * *
**Articoli collegati**


##### Filter by label

There are no items with the selected labels at this time.
:::