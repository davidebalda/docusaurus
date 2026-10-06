---
title: "Forzare manualmente registrazione e de-registrazione dell'agent in cloud"
---

## Introduzione {#introduzione}

In alcuni casi in seguito all'installazione e registrazione dell'agent questo non viene visto nella dashboard web.

In questo caso potete forzare la registrazione manualmente, seguendo i passaggi della guida ufficiale Acronis.

### Windows OS {#windows-os}

**Acronis Backup Cloud 7.8 e versioni più recenti**

1. Aprire il prompt dei comandi e accedere a C:\\Program Files\\BackupClient:
```
cd "%ProgramFiles%\BackupClient\RegisterAgentTool"
```
2. Con questo si può registrare la service machine con utente e password
```
register_agent.exe -o register -t cloud -a https://eu2-cloud.acronis.com -u <account> -p <password>
```
o questo comando per la registrazione della macchina client usando un token:
```
"C:\Program Files\BackupClient\RegisterAgentTool\register_agent.exe" -a <your-datacenter> --token <token> -o register -t cloud
```

:::info
*`<your-datacenter>`* è l’indirizzo del datacenter che il browser mostra quando loggati nella console di backup , ad esempio: **[https://eu2-cloud.acronis.com/](https://eu2-cloud.acronis.com/)**
:::

**Acronis Backup Cloud 7.5 o versioni precedenti**

1. Apri il prompt dei comandi e accedi a C:\\Program Files\\BackupClient\\BackupAndRecovery:
```
cd "%ProgramFiles%\BackupClient\BackupAndRecovery"
```
2. Utilizza questo comando per creare la macchina client:
```
register_msp_mms.exe register https://eu2-cloud.acronis.com <account> <password>
```

### Linux OS {#linux-os}

**Acronis Backup Cloud 7.8 o versioni più recenti**

1. Apri il terminal come root.
2. Digita i seguenti comandi per registrare l’agent con utente e password:
```
./usr/lib/Acronis/RegisterAgentTool/RegisterAgent -o register -t cloud -a https://eu2-cloud.acronis.com -u <account> -p <password>
```
O utilizza questo comando per creare il client con un token:
```
./usr/lib/Acronis/RegisterAgentTool/RegisterAgent -o register -t cloud -a <your-datacenter> --token <token>
```

:::info
*`<your-datacenter>`* è l’indirizzo del datacenter che il browser mostra quando loggati nella console di backup , ad esempio: **[https://eu2-cloud.acronis.com/](https://eu2-cloud.acronis.com/)**
:::

**Acronis Backup Cloud 7.5 o versioni precedenti**

1. Apri il terminal come root.
2. Digita i seguenti comandi per registrare l’agent con utente e password::
```
./usr/lib/Acronis/RegisterAgentTool/RegisterAgent -o register -t cloud -a <your-datacenter> --token <token>
```

### OS X {#os-x}

**Acronis Backup Cloud 7.8 o versioni più recenti**

1. Apri il terminal.
2. Digita i seguenti comandi per registrare la macchina client con utente e password::
```
sudo "/Library/Application Support/BackupClient/Acronis/RegisterAgentTool/RegisterAgent" -o register -t cloud -a https://eu2-cloud.acronis.com -u <account> -p <password>
```
o questo comando per la registrazione della macchina client usando un token:
```
sudo "/Library/Application Support/BackupClient/Acronis/RegisterAgentTool/RegisterAgent" -o register -t cloud -a <your-datacenter> --token <token>
```

:::info
*`<your-datacenter>`* è l’indirizzo del datacenter che il browser mostra quando loggati nella console di backup , ad esempio: **[https://eu2-cloud.acronis.com/](https://eu2-cloud.acronis.com/)**
:::

**Acronis Backup Cloud 7.5 o versioni precedenti**

1. Apri il terminal.
2. Esegui il seguente comando:
```
sudo "/Library/Application Support/BackupClient/Acronis/BackupAndRecovery/AmsRegisterHelper" register https://eu2-cloud.acronis.com <login> <password>
```

***Per de-registrare l'opzione "-o" è unregister***