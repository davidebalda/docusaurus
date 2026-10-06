**Problema**

Possibile problematica legata al database di Veeam Agent per Windows.  
Prima di effettuare le azioni seguenti, assicurarsi di aver controllato il software antivirus e il firewall per eventuali blocchi del servizio Veeam.

**Possibili soluzioni**

1. Creare o modificare la seguente chiave di registro sull’host in cui è installato l’agente Veeam.**Key Location:** `HKLM\SOFTWARE\Veeam\Veeam Endpoint Backup`  
**Value Name:** `RecreateDatabase`  
**Value Type:** `DWORD (32-bit) Value`  
**Value Data:** `1`
2. Riavviare il servizio **Veeam Agent for Windows**.  
Durante il riavvio del servizio, il database verrà ricreato e il volore della chiave di registro tornerà a 0.
3. Riavviato il servizio, bisognerà rifare uno scan dell’host in inventory e far ripartire il job di backup completo.  
Le vecchie retention resteranno comunque disponibili, ma non verranno più considerate per gli incrementali.