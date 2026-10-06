Questa pagina spiega come creare coppie di chiavi / key pairs.

> [!NOTE]
> Una chiave SSH o Key Pairs è una credenziale crittografica usata per autenticarsi in modo sicuro su server e servizi remoti. È composta da una **chiave privata**, che resta sul dispositivo dell’utente, e da una **chiave pubblica**, che viene caricata sul server o sulla piattaforma.
> Le coppie di chiavi sono importanti soprattutto per la configurazione delle istanze linux based, in quanto l'accesso SSH da esterno è basato su chiave e non su password.
> **L’accesso tramite chiavi SSH è più sicuro rispetto all’uso della sola password, perché riduce il rischio di accessi non autorizzati e consente un’autenticazione più affidabile per server, macchine virtuali e servizi remoti.**

## Prerequisiti

Accesso come amministratore del progetto

## Creazione coppia di chiavi

1. Selezionare il progetto corretto
2. Sotto la voce **Compute**, seleziona la voce di menù **Key Pairs / Coppia di chiavi**

![Screenshot 2026-03-25 at 12.41.16.png](./attachments/Screenshot%202026-03-25%20at%2012.41.16.png)

1. Selezionare la voce **\+ CREATE KEY PAIR** o **\+ CREA COPPIA DI CHIAVI**
2. Inserire un nome identificativo
3. Selezionare la tipologia di chiave SSH Key  
![Screenshot 2026-03-25 at 12.49.34.png](./attachments/Screenshot%202026-03-25%20at%2012.49.34.png)
4. Si scaricherà in automatico un file *KeiPairNameinserito.pem (nel mio caso* Key Sales SPdemo.pem) ovvero la **chiave privata corrispondente alla pubblica che si genera sul progetto**

> [!CAUTION]
> Conservate la chiave privata generata, se utilizzata per l'accesso a un'istanza può diventare cruciale per non rimanerne fuori per sempre

1. Sulla dashboard invece, aprendo la tendina in corrispondenza del nome puoi ottenere la chiave pubblica

![Screenshot 2026-03-25 at 12.58.58.png](./attachments/Screenshot%202026-03-25%20at%2012.58.58.png)

## Import coppia di chiavi

1. Selezionare il progetto corretto
2. Sotto la voce **Compute**, seleziona la voce di menù **Key Pairs / Coppia di chiavi**
3. Selezionare la voce **IMPORT PUBLIC KEY**
4. Inserire un nome identificativo
5. Selezionare la tipologia di chiave SSH Key
6. Scegli un file o via copia e incolla
7. ![Screenshot 2026-03-25 at 13.00.24.png](./attachments/Screenshot%202026-03-25%20at%2013.00.24.png)

> [!WARNING]
> Ricorda: La chiave caricata è abbinata all'utente di default "**Ubuntu**" / "**Centos**"
> Per creare un'utenza con password usate le configurazioni aggiuntive durante la creazione dell'istanza, specificando le istruzioni per Cloud-Init.

> [!INFO]
> Openstack as a Service accetta chiavi in formato pem: in caso di connessioni ricordatevi la corretta conversione via ***PuTTYgen***.
> - La chiave privata generata su Openstack as a Service deve essere convertita per essere utilizzata via Putty
> - In caso di generazione chiavi via Putty, la chiave pubblica (RSA) deve essere scritta in formato pem prima di essere importata

  

  

> [!NOTE]
> **Sommario**
> 
> 
> 
> - [Prerequisiti](#prerequisiti)
> - [Creazione coppia di chiavi](#creazione-coppia-di-chiavi)
> - [Import coppia di chiavi](#import-coppia-di-chiavi)
> -   Filter by label
> * * *
> **Articoli collegati**
> 
> 
> ##### Filter by label
> 
> There are no items with the selected labels at this time.