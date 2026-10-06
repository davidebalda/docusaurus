---
title: "Backup/Recovery lenti"
---

### Sintomi {#sintomi}

- Hai configurato backup Cloud in Acronis Cyber Protect Cloud
- La velocità delle operazioni di backup/ripristino è più lenta del previsto
- L'operazione di backup o ripristino inizia normalmente ma rallenta dopo alcune ore

### Verifiche di rete {#verifiche-di-rete}

1. Scarica lo Strumento di Verifica Connessione da [questo articolo](https://care.acronis.com/s/article/47678-Acronis-Cyber-Protect-Cloud-Acronis-Cyber-Protect-15-and-Acronis-Cyber-Backup-12-5-Connection-Verification-Tool?language=en_US) ed eseguilo.
2. Ottieni i risultati dai test di lettura e scrittura. Per esempio:

[](https://acronis.file.force.com/sfc/dist/version/download/?oid=00D300000000Zcb&ids=0681T00000Ofhd7&d=%2Fa%2F1T000001CKYW%2FGoL0_KM_L_Foca2z6agXBh7Fo.._cvgTHgHlBFiktJ0&asPdf=false)

1. Apri il sito web [http://speedtest.net](http://speedtest.net) (per macchine Linux CLI, usa [https://www.speedtest.net/apps/cli)](https://www.speedtest.net/apps/cli)).

**Cambia 'Connections' da 'Multi' a 'Single' e cambia il server nella posizione dove si trova lo storage cloud.** Questo è fondamentale perché l'opzione predefinita con la verifica multi-stream mostra la massima velocità possibile con più stream. Acronis funziona in modalità single stream, quindi per risultati corretti, **devi passare alla modalità Single nell'**[http://speedtest.net](http://speedtest.net) **utility.** 

Per trovare la posizione fisica dello storage cloud, usa un servizio web che fornisce GeoIP (per esempio [http://www.iplocation.net](http://www.iplocation.net) ). La posizione dei datacenter Acronis può essere trovata in [questo articolo](https://care.acronis.com/s/article/47189-Acronis-Cyber-Protect-Cloud-access-ports-and-hostnames?language=en_US).

[](https://acronis.file.force.com/sfc/dist/version/download/?oid=00D300000000Zcb&ids=0681T00000OfhVE&d=%2Fa%2F1T000001CKSf%2F5poGZ21Uzvhj4QBWbHi.WCTK8IqEh3jDCzqHnyj0hYY&asPdf=false)

[](https://acronis.file.force.com/sfc/dist/version/download/?oid=00D300000000Zcb&ids=0681T00000OfhXs&d=%2Fa%2F1T000001CKUI%2FxbN2rVRC.okk.CVfIv09sHm2FYe7C.pYxDtaJVfEWN0&asPdf=false)

1. Confronta la velocità di lettura/scrittura ottenuta con lo Strumento di Verifica Connessione con la Velocità di Download/Upload da Speedtest. Se i risultati corrispondono, allora la velocità di backup/ripristino è limitata dalla banda disponibile dalla macchina alla posizione indicata. Ricorda che Speedtest mostra i risultati verso un server terzo, quindi i risultati in Speedtest non dipendono dal datacenter Acronis.

### Verifiche avanzate {#verifiche-avanzate}

Ci possono essere situazioni in cui lo Strumento di Verifica Connessione non funziona, ma hai comunque bisogno di misurare la velocità di upload/download.

In questi casi, puoi usare lo strumento **archive\_io\_ctl** per eseguire questa operazione.  
Per maggiori informazioni, consulta [la seguente guida](https://care.acronis.com/s/article/70719-Slow-backup-recovery-speed?language=en_US) di Acronis.

### Cause {#cause}

Esistono vari fattori che influenzano la lentezza delle velocità di backup o ripristino verso lo storage cloud. Questi possono essere attribuiti a una combinazione di fattori architetturali e ambientali, alcuni dei quali sono elencati di seguito:

- **Instradamento di rete e latenza**: le velocità di trasferimento effettive dipendono fortemente dallo specifico percorso di rete, dal bilanciamento del carico e dalle limitazioni di routing tra il provider di servizi Internet (ISP) locale e la posizione fisica del datacenter Acronis assegnato.
- **Elevate operazioni di I/O disco** durante il processo (come lettura o decompressione di archivi di grandi dimensioni) possono creare limitazioni prestazionali locali indipendenti dalla larghezza di banda di rete disponibile.

### Risoluzione {#risoluzione}

Per migliorare la velocità di backup e ripristino, prova le seguenti soluzioni:

- **Abilitare il multistreaming:** Consulta questo articolo [Acronis Cyber Protect Cloud: Come abilitare il multistreaming per backup e ripristino da e verso lo storage cloud](https://care.acronis.com/s/article/Acronis-Cyber-Protect-Cloud-How-to-enable-multistreaming-for-backups-to-cloud-storage?language=en_US). Questa funzione utilizza più connessioni TCP in parallelo per sfruttare appieno la larghezza di banda di rete disponibile.
- **Verificare il throttling della larghezza di banda:** Controlla che il piano di protezione applicato non abbia una specifica [finestra di prestazioni](https://www.acronis.com/en/support/documentation/CyberProtectionService/#performance-and-backup-window.html?Highlight=performance%20window) o un limite di larghezza di banda abilitato che limiti la velocità di upload.
- **Escludere Acronis dalla scansione antivirus:** Disabilita temporaneamente l'antivirus di terze parti o aggiungi le cartelle eseguibili di Acronis alla lista delle esclusioni per assicurarti che il software di sicurezza non stia scansionando attivamente i processi di backup o bloccando i file.
- **Monitorare le risorse di sistema:** Controlla il Task Manager o il Resource Monitor della macchina locale durante un backup per assicurarti che CPU, RAM o I/O disco non siano saturi al 100%.

Se i passaggi proposti non risolvono il problema, raccogli le seguenti informazioni/log e invia un ticket al supporto tecnico:

1. Risultati del **Connection Verification Tool (CVT)** e dei test di Speedtest.   
*Riferimento:* [Connection Verification Tool (CVT)](https://care.acronis.com/s/article/47678-Acronis-Cyber-Protect-Cloud-Acronis-Cyber-Protect-15-and-Acronis-Cyber-Backup-12-5-Connection-Verification-Tool?language=en_US)
2. **Posizione fisica** dello storage cloud. Utilizza un servizio web GeoIP (ad esempio, [www.iplocation.net](https://www.iplocation.net/)) per determinarla (La posizione dei datacenter Acronis può essere trovata in [questo articolo](https://care.acronis.com/s/article/47189-Acronis-Cyber-Protect-Cloud-access-ports-and-hostnames?language=en_US).).
3. **Report di sistema** dalla macchina agente, raccolto immediatamente dopo aver riprodotto il problema.  
*Riferimento:* [Come raccogliere un Report di Sistema](https://care.acronis.com/s/article/54608-Acronis-Cyber-Protect-Cloud-Collecting-system-report?language=en_US)