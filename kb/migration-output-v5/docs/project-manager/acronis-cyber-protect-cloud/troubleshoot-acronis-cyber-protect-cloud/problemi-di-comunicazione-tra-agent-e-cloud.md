---
title: "Problemi di comunicazione tra Agent e Cloud"
---

## Problema {#problema}

I backup in Cloud falliscono o l'agente di backup risulta offline anche se la connettività risulta funzionante.

## Possibili cause e soluzioni {#possibili-cause-e-soluzioni}

A volte è possibile che a causa di policy di firewall o particolari configurazioni di rete, l'agent installato sulle vostre macchine locali abbia difficoltà ad eseguire correttamente in backup in cloud. In questa guida vi illustreremo come verificare che la comunicazione tra agent e cloud funzioni correttamente, installando un tool di verifica. Una volta che il tool avrà finito il check delle porte vi restituirà il risultato dove poterete vedere se è presente qualche sorta di blocco o filtro.

## Guida step by step: {#guida-step-by-step}

:::warning
"For successful installation and update of Acronis agents, white-list [download.acronis.com](http://download.acronis.com) and IP addresses 69.20.59.102, 69.20.59.103, 173.222.210.x, 88.221.48.x and 88.221.49.x"
Verificate inoltre che i seguenti IP non siano bloccati lato firewall/security appliance lato vostro: 185.132.68.61,185.132.68.54, 185.132.68.52, 185.132.68.50, 185.132.68.40.
:::

### Windows {#windows}

Il tool di verifica è già integrato nativamente nell'agent per Windows, e potete eseguirlo in fase di installazione dello stesso. Seguite la seguente guida se volete effettuare il check dopo l'installazione (in caso appunto un backup in cloud fallisca riportando errori di connessione). 

Scaricate il [Connection Verification Tool](https://kb.acronis.com/system/files/content/2017/03/47678/cloud_connection_verification_tool.zip) sulla macchina con l'agente installato e estraete il pacchetto.

Aprite il promt dei comando con privilegi di amministratore ed inserite i seguenti parametri:

```
port_checker_en-US_x86.exe -u=<login> -p=<password>
```

Inserite le vostre credenziali di accesso al servizio Backup Smart nei campi ***`<login>`*** e ***`<password>`.***

:::info
Se non inserite la password e premete invio, vi verrà chiesta subito dopo.
Se la vostra password contiene caratteri speciali come *$:; %#,* inserite la password tra doppi apici:
Es. ***port\_checker\_en-US\_x86.exe -u=[my@email.com](mailto:my@email.com) -p="MySecure;Pa$$word"***
:::

### Linux 64bit {#linux-64bit}

Scaricate il [Linux Connection Verification Tool (64bit)](https://kb.acronis.com/system/files/content/2017/03/47678/linux_connection_verification_tool.zip) sulla macchina con l'agente installato e estraete il pacchetto.

Da terminale, assicuratevi di fornire i permessi di esecuzione al tool:

```
chmod +x ./linux_port_checker_en-US_x86_64
```

Sempre da terminale eseguite il seguente comando per eseguire il tool:

```
./linux_port_checker_en-US_x86_64 -u=<login> -p=<password>
```

Inserite le vostre credenziali di accesso al servizio Backup Smart nei campi ***`<login>`*** e ***`<password>`.***

:::info
Se non inserite la password e premete invio, vi verrà chiesta subito dopo.
Se la vostra password contiene caratteri speciali come *$:; %#,* inserite la password tra doppi apici:
Es. ***./linux\_port\_checker\_en-US\_x86\_64 -u=[my@email.com](mailto:my@email.com) -p="MySecure;Pa$$word"***
:::

Ora il tool effettuerà un check di comunicazione sia con i Server di management sia con lo Storage (incluso anche la connessione SSL).

Controllate il report fornito se tutti gli host vengono raggiunti correttamente.

:::caution
Se dovessero essere presenti errori, il tool stesso vi indicherà quali sono le porte da aprire. Una volta effettuati i check/modifiche sulla vostra rete, se il problema dovesse persistere contattate la nostra assistenza tecnica.
:::

### Linux 32bit {#linux-32bit}

Scaricate il [Linux Connection Verification Tool(32bit)](http://dl.acronis.com/u/kb/linux_connection_verification_tool_32bit.zip) sulla macchina con l'agente installato e estraete il pacchetto

Da terminale, assicuratevi di fornire i permessi di esecuzione al tool:

```
chmod +x ./linux_port_checker_en-US_32bit
```

Sempre da terminale eseguite il seguente comando per eseguire il tool:

```
./linux_port_checker_en-US_32bit -u=<login> -p=<password>
```

Inserite le vostre credenziali di accesso al servizio Backup Smart nei campi ***`<login>`*** e ***`<password>`.***

:::info
Se non inserite la password e premete invio, vi verrà chiesta subito dopo.
Se la vostra password contiene caratteri speciali come *$:; %#,* inserite la password tra doppi apici:
Es. ***./linux\_port\_checker\_en-US\_32bit -u=[my@email.com](mailto:my@email.com) -p="MySecure;Pa$$word"***
:::

Ora il tool effettuerà un check di comunicazione sia con i Server di management sia con lo Storage (incluso anche la connessione SSL)

Controllate il report fornito se tutti gli host vengono raggiunti correttamente.

:::caution
Se dovessero essere presenti errori, il tool stesso vi indicherà quali sono le porte da aprire. Una volta effettuati i check/modifiche sulla vostra rete, se il problema dovesse persistere contattate la nostra assistenza tecnica.
:::

  

  

:::note
**Sommario**



- [Problema](#problema)
- [Possibili cause e soluzioni](#possibili-cause-e-soluzioni)
- [Guida step by step:](#guida-step-by-step)
-   [Windows](#windows)
-   [Linux 64bit](#linux-64bit)
-   [Linux 32bit](#linux-32bit)
* * *
**Articoli collegati**


- Page:
[Recovery VM su Openstack as a Service via Acronis Cyber Backup Service](../../openstack-as-a-service/how-to-openstack-as-a-service/recovery-vm-su-openstack-as-a-service-via-acronis-cyber-backup-service.md)
- Page:
[Esempi di utilizzo Cloud Storage su Synology](../../cloud-storage/how-to-cloud-storage/esempi-di-utilizzo-cloud-storage-su-synology.md)
- Page:
[Migrazione VM su Openstack as a Service via Acronis Universal Restore](../../openstack-as-a-service/how-to-openstack-as-a-service/migrazione-vm-su-openstack-as-a-service-via-acronis-universal-restore.md)
- Page:
[Invalid Credentials durante backup su share di rete (smb/cifs)](invalid-credentials-durante-backup-su-share-di-rete-smb-cifs.md)
- Page:
[Problemi di comunicazione tra Agent e Cloud](problemi-di-comunicazione-tra-agent-e-cloud.md)
:::