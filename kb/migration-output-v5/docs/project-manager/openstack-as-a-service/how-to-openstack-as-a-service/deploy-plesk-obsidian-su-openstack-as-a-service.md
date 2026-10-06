---
title: "Deploy Plesk Obsidian su Openstack as a Service"
---

Questa guida mostra in modo dettagliato quali sono i passaggi necessari per la creazione di una VPS Plesk Obsidian funzionante su infrastruttura Openstack as a Service.  

:::info
Prima di proseguire con la lettura di questa guida, assicurarsi di aver attivato il servizio **Openstack as a Service** su **Cortex**.  
Questa operazione può essere eseguita solo se si dispone di privilegi **Admin** o **Tecnico** alla propria utenza Cortex.
:::

## Creazione dell’istanza {#creazione-dell-istanza}

Per poter ospitare Plesk, bisogna creare un istanza e configurarla seguendo il metodo di sotto indicato:

1. Accedi al progetto **Openstack as a Service** sul quale vuoi creare l’istanza e vai sulla voce del menu **Istances**
2. Premi su **Launch Instance** e segui la creazione guidata dell’istanza  
![](/kb-assets/8823f2d305-public-cloud-plesk-1.png)
3. Assegna un nome etichetta alla nuova istanza nella sezione **Instance Name**  
![](/kb-assets/57dee9f6e4-public-cloud-plesk-2.png)
4. Seleziona **Image** come sorgente di boot e imposta un valore al **Volume**.  
Successivamente dalle Immagini disponibili nell’elenco seleziona **OPERATING\_SYSTEM: Ubuntu 20.04 Plesk 18.0.44**  
![](/kb-assets/e69b420930-public-cloud-plesk-3.png)
5. Seleziona il **Flavor** che ritieni più opportuno per la creazione dell’istanza Plesk.  
Se non sai quale **Flavor** scegliere, allora puoi fare riferimento alla seguente [Tabella Flavors](../primi-passi-openstack-as-a-service/flavor-e-storage-disponibili-in-openstack-as-a-service-v2.md)
6. Seleziona la voce **Private** nella sezione **Network**.  
Una volta terminata la creazione dell’istanza, associare un **Floating IP** per rendere la macchina pubblica.  
![](/kb-assets/d31caa4a2c-public-cloud-plesk-4.png)
7. Selezionare la voce **Configuration** e fare riferimento a questa guida per abilitare l’[accesso tramite Username e Password](../primi-passi-openstack-as-a-service/cloud-init-utente-con-password-e-configurazioni-aggiuntive.md) in SSH alla macchina.
8. Premere su **Launch Instance** e attendere il completamento dell’operazione. Al termine, l’istanza creata sarà presente nella sezione **Instances** iniziale.  

:::warning
**Passaggio 7:** Questo passaggio è essenziale se si vuole accedere la macchina tramite Terminal **SSH** esterno alla console Openstack as a Service utilizzando come metodo di autenticazione Username e Password.
:::

## Creazione e associazione dei Security Groups {#creazione-e-associazione-dei-security-groups}

La funzione dei Security Groups è quella di firewalling, ovvero sono regole che si interpongono tra la rete dell’infrastruttura IaaS del Openstack as a Service con la rete globale.  
Per poter sfruttare al meglio le funzioni di Plesk, dobbiamo abilitare diverse porte.  

|     |     |     |
| --- | --- | --- |
| **Protocollo** | **Porte** | **Descrizione** |
| HTTP, HTTPS | 80, 443 | Porte utilizzate per la comunicazione HTTP e HTTPS per trasmissione dati criptati e non. Utilizzate anche per l’installazione automatica di certificati Let’s Encrypt. |
| FTP | 21  | Porta utilizzata per trasferimento dati tramite protocollo FTP. Generalmente utilizzato per caricare i contenuti dei siti web nelle repository di destinazione ed essere poi visualizzati come pagine web. |
| SSH | 22  | È un protocollo che permette di stabilire una sessione remota cifrata tramite interfaccia a riga di comando con un host di una rete informatica. |
| Passive port range | 49152 - 65535 | Range di porte che permette la gestione simultanea di connessioni passive al server. |

Per aprire queste porte è sufficiente seguire i seguenti passaggi:

1. Dall’interfaccia Openstack as a Service seleziona la voce **Network** e poi premi su **Security Groups**
2. Premi su **Create security group**  
![](/kb-assets/1516b02c1f-public-cloud-plesk-5.png)
3. Associa un nome al Security Group e premi su **Create security group**  
![](/kb-assets/a0aa14cfce-public-cloud-plesk-6.png)
4. All’interno del **Security Group**, premendo su **Add rules**, si potranno aggiungere le regole per aprire le porte citate nella tabella soprastante.  
![](/kb-assets/20eccf6410-public-cloud-plesk-7.png)
5. Dalla voce **Instances**, selezionare la macchina alla quale associare il nuovo **Security Groups**
6. Dalla selezione multipla selezionare **Edit Security Groups** e spostare nella colonna di sinistra il Security Group da associare

:::warning
Aprire il protocollo **SSH** solo agli **IP Pubblici** di chi deve gestire la macchina. Altrimenti potrebbe essere vulnerabile da intromissioni indesiderate.
:::

## Inizializzare Plesk per accesso Web {#inizializzare-plesk-per-accesso-web}

Dopo aver creato l’istanza ed aver associato le regole di connessione, è necessario lanciare un comando tramite Command Line Interface per inizializzare Plesk.  
L’inizializzazione di Plesk è fondamentale per poter accedere al pannello di gestione Web.  

```
login as: adminuser
adminuser@your-floating-ip's password:
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-120-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 System information disabled due to load higher than 2.0


0 updates can be applied immediately.


The list of available updates is more than a week old.
To check for new updates run: sudo apt update


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.


adminuser@plesk-test:~$ sudo plesk bin init_conf --init -name "Administrator" -passwd Default2022!

SUCCESS: Plesk initialization is completed.
adminuser@plesk-test:~$ SUCCESS: Plesk initialization is completed.
adminuser@plesk-test:~$

```

1. Accedi alla console dell’istanza tramite un **Terminal SSH**
2. Esegui il seguente comando: *sudo plesk bin init\_conf --init -name "Administrator" -passwd \*\*\*\*\*\*\*\*\**
3. Accedi all’interfaccia web digitando: **https://<il-tuo-floating-ip:8443/**
4. Utilizzare le credenziali  
Username: **admin**  
Password: **\*\*\*\*\*\*\***