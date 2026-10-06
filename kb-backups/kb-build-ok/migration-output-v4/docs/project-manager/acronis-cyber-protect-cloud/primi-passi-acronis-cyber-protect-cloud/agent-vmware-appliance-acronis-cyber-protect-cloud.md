---
title: "Agent VMware Appliance - Acronis Cyber Protect Cloud"
---

## Introduzione

  

Per proteggere le vostre vm (vmware) utilizzando l’appliance dedicata (e non l’agent di gestione da installare su OS windows) prima di tutto dovrete scaricarla dalla dashboard.

Effettuate il login con le vostre credenziali in base alla region attiva su:

- URL - Region Acronis-Eu2 - Francoforte, Germania: [eu2.backup.cloudfire.it](http://eu2.backup.cloudfire.it)
- URL - Region Acronis-Eu8 - Francoforte, Germania: [eu8.backup.cloudfire.it](http://eu8.backup.cloudfire.it)
- URL - Region Acronis-It01 - Roma, Italia: [it01.backup.cloudfire.it](http://it01.backup.cloudfire.it) (in sostituzione a URL:  [**backup.cloudfire.it**](http://backup.cloudfire.it/))

Cliccate sull’icona utente in alto a destra ed entrate nella sezione Download.

Scaricate quindi “Virtual appliance (OVF)”.

Effettuate il deployment dell’OVF nella vostra infrastruttura vmware.

## Guida passo-passo

- Recatevi nella console della VM appena creata.

![](/kb-assets/df1bc5d51d-1.png)

- In questo caso la VM è stata collegata a una rete con *DHCP*.
- In caso contrario impostare l’ip statico sull’interfaccia “eth0” cliccando su “Change…” nella relativa sezione.
- Entrate nella sezione “vCenter/ESX(i)” , per specificare le credenziali del vostro endpoint, cliccando su “Change…”
- Indicate l’ip dell’host/vcenter (o nome in caso di corretta risoluzione da parte del server DNS indicato durante la configurazione di rete); username es: [root/Administrator@vsphere.local](mailto:root/Administrator@vsphere.local) e la relativa password. Testate la connessione e chiudete con **"OK"**.

![](/kb-assets/4188026131-2.png)

- Entrate quindi nella sezione *“Management Server”* cliccando “Change…” nella relativa sezione.

![](/kb-assets/b70200a24f-3.png)

- Qui cambiate “Local” in “Cloud” ed impostate l’indirizzo che raggiungete via web per effettuare l’accesso alla dashboard di Acronis Cyber Backup Backup in base alle region attiva su:
-   URL - Region Acronis-Eu2 - Francoforte, Germania: [eu2.backup.cloudfire.it](http://eu2.backup.cloudfire.it)
-   URL - Region Acronis-Eu8 - Francoforte, Germania: [eu8.backup.cloudfire.it](http://eu8.backup.cloudfire.it)
-   URL - Region Acronis-It01 - Roma, Italia: [it01.backup.cloudfire.it](http://it01.backup.cloudfire.it) (in sostituzione a URL:  [**backup.cloudfire.it**](http://backup.cloudfire.it/))
- Inserite quindi le vostre credenziali utilizzate per la Web Dashboard in “User name” e “Password”.
- Confermate con “OK”.
- A questo punto nella console web potrete vedere tutte le vm gestite dall’host o dal vCenter collegato precedentemente, a cui quindi potete applicare i backup job presenti o futuri, in cloud o su storage locali.
- Scorrendo verso il basso nella console relativa alla vostra appliance potete specificare un nome macchina e la “*Time zone*”.

![](/kb-assets/99e579967f-4.png)

**La sezione più bassa indica “LOCAL STORAGES”.**

:::info
Esiste la possibilità di aggiungere un disco all’appliance virtuale, a partire da un datastore della vostra infrastruttura, e vederlo come storage “locale” destinazione dei vostri backup.
:::

  

  

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Guida passo-passo](#guida-passo-passo)
-   Filter by label
* * *
**Articoli collegati**


##### Filter by label

There are no items with the selected labels at this time.
:::