---
title: "Cloud-Init, utente con password e configurazioni aggiuntive"
---

## Introduzione

Durante la creazione di un'istanza Linux è possibile fornire istruzioni specifiche per l'installazione di pacchetti o, in questo caso per la creazione di un'utenza con password (di default l'utenza di default è "ubuntu" ed è accessibile con una chiave privata, quindi non da console).

## Prerequisiti

Accesso come amministratore del progetto.

Macchina d'appoggio unix based dove gestire il pacchetto specificato di seguito.

## Guida passo-passo

- Se si desidera l'implementazione di un utente con password da usare in console fin da subito, prima di effettuare il deployment dell'istanza generare un hash a partire dalla password desiderata con i seguenti passaggi:

```
sudo apt install whois #per installare il pacchetto

mkpasswd --method=SHA-512 --rounds=4096 #comando per richiedere l'hash, l'output richiede l'inserimento della password
```

- Immettete la vostra password e riceverete un'hash in questo formato:  $6$rounds=4096$STX6Ombh$Brldjdbpp8q/P97iKyXJql8S3yDOihGwobSYLXA7O0awLycn9xK6O3ASvMMkCp/ElGIc2szmrA0p68aJELfki/
- Riprendere quindi il seguente insieme di righe impostato il campo "passwd" appena generato ed eventualmente cambiando il nome dell'account   
```
#cloud-config
users:
  - default
  - name: adminuser
    sudo:  ALL=(ALL) NOPASSWD:ALL
    shell: /bin/bash
    lock_passwd: false
    passwd: $6$rounds=4096$STX6Ombh$Brldjdbpp8q/P97iKyXJql8S3yDOihGwobSYLXA7O0awLycn9xK6O3ASvMMkCp/ElGIc2szmrA0p68aJELfki/
```

Se si preferisce invece avere una password non criptata, è possibile cancellare la linea di comando "passwd" e seguire questo codice per creare una password temporanea, che il sistema vi chiederà di modificare al primo login:

```
#cloud-config
users:
 - default
 - name: adminuser
   groups: users, admin
   sudo: ALL=(ALL) NOPASSWD:ALL
   shell: /bin/bash
   lock_passwd: false
chpasswd:
  list: |
    root:tempPass
    adminuser:temp
```

Inoltre, se si volesse abilitare sempre via cloud init l’accesso ssh via user e password invece che con chiave privata, aggiungere i seguenti comandi al file cloud init:

```
runcmd:
  - sed -i -e '/^#PermitRootLogin/s/^.*$/PermitRootLogin yes/' /etc/ssh/sshd_config
  - sed -i 's|[#]*PasswordAuthentication yes|PasswordAuthentication yes|g' /etc/ssh/sshd_config
  - service sshd restart
```

:::warning
In caso nel vostro progetto Openstack as a Service aveste rimosso il router virtuale, ricordatevi di spuntare la casella in corrispondenza di “Configuration Drive” in modo che il
Cloud-init venga passato anche se non è presente il router.
:::

![](/kb-assets/0d4c178f18-image-20211012-092311.png)

# **Abilitare l'accesso in SSH con solo Username e Password** 

  
Dopo aver seguito i passaggi precedenti, entrare in console sulla macchina da Openstack as a Service. 

1. Autenticarsi con lo username impostato e la password. 
2. eseguire il comando: cd /etc/ssh/ per entrare nella directory
3. eseguire il comando: nano sshd\_config per andare a modificare il file di conf dell'ssh e assicurarsi che le seguenti stringhe non siano commentate (presenza del carattere # all’inizio della stringa) e che siano come indicato qui sotto
1.   `PasswordAuthentication yes` (garantisce di autenticarsi con utente e password in SSH)
2.   `PermitRootLogin yes` (garantice di autenticarsi con utente “root” in SSH)
4. Eseguite un restart del servizio SSH con il comando service sshd restart

  

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Prerequisiti](#prerequisiti)
- [Guida passo-passo](#guida-passo-passo)

- [Abilitare l'accesso in SSH con solo Username e Password](#Cloud-Init,utenteconpasswordeconfigurazioniaggiuntive-Abilitarel'accessoinSSHconsoloUsernameePassword)

-   Filter by label
* * *
**Articoli collegati**


##### Filter by label

There are no items with the selected labels at this time.
:::