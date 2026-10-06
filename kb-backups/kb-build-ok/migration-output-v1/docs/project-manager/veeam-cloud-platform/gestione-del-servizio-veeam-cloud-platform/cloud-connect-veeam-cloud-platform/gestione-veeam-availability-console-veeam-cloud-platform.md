---
title: "Gestione Veeam Availability Console -  Veeam Cloud Platform"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina spiega come Accedere alla Console Web di Veeam. La Veeam Service Provider Console permette di usufruire di una piattaforma di controllo web dal quale è possibile amministrare le diverse operazioni del servizio.

:::note
Veeam Availability Console è stata rinominata **Veeam Service Provider Console**.
:::

# Veeam Service Provider Console

Veeam Service Provider Console è una piattaforma Cloud che offre tutto il necessario per implementare, gestire e monitorare gli ambienti Veeam virtuali, fisici o basati sul cloud, indipendentemente dalla loro locazione e complessità.

:::info
Veeam Service Provider Console viene attivata automaticamente durante il processo di attivazione di Veeam Cloud Connect.
:::

![Screenshot 2024-05-13 at 17.12.02.png](/kb-assets/67db6c1504-screenshot-2024-05-13-at-17-12-02.png)

## Accedere a Veeam Service Provider Console

Per accedere Veeam Service Provider Console è sufficiente seguire i seguenti passaggi:

1. Effettua il **login** su Cortex, verrai indirizzato al su Account Manager
1.   Se sei un partner effettua l’accesso a **Partner Portal** utilizzando il bottone apposito in alto a destra. Il portale si aprirà in una nuova tab del browser
2. Seleziona la voce **Project Manager**
3. Seleziona la voce **Veeam Cloud Platform** dalle voci di menù laterale nella categoria **Backup as a Service**;
4. Seleziona la voce **Cloud Connect** dalle voci nelle tab;
5. Premi sul bottone **Accedi a VAC** nel riquadro del servizio **Veeam Service Provider Console**.
6. Nella finestra di dialogo aperta ([https://vac.cloudfire.it/](https://vac.cloudfire.it/) ) inserisci le credenziali mostrate nella sezione Veeam Service Provider Console aiutandoti con il pulsante per copiare i contenuti.![](/kb-assets/2fde043dcf-2022-12-20-15-56-53.png)
7. Effettua il Login alla piattaforma per usufruire dei suoi strumenti.

## Funzionalità della Veeam Service Provider Console

I vantaggi e gli strumenti disponibili utilizzando la Veeam Service Provider Console sono:

1. Distribuzione automatizzata, configurazione e gestione degli Agent backup di Veeam
2. Monitoraggio e gestione centralizzate per Veeam Backup & Replication
3. Monitoraggio delle risorse per Veeam Cloud Connect
4. Monitoraggio e reporting dei backup
5. RESTful API. [Maggiori informazioni su REST API di Veeam](https://helpcenter.veeam.com/docs/vac/rest/about_rest.html?ver=50).

# Gestione degli agenti della console di Veeam Service Provider

Per gestire gli agenti di backup Veeam, Veeam ONE, Veeam Backup for Microsoft 365 e i server Veeam Backup & Replication nella Veeam Service Provider Console ed eseguire il rilevamento dei computer nell'infrastruttura client, è necessario installare l' agenti di gestione della Veeam Service Provider Console sulle macchine in cui sono distribuiti i prodotti Veeam . Gli agenti di gestione di Veeam Service Provider Console possono raccogliere dati, eseguire attività di gestione e configurazione su macchine gestite o effettuare rilevazioni nell'infrastruttura client.

Una volta terminata l’installazione dell’agente, sarà possibile installare sulla stessa l’agente di backup [https://cloudfireit.atlassian.net/wiki/spaces/~239475519/pages/2069234598/New+Gestione+Veeam+Availability+Console+-++Veeam+Cloud+Platform#Installare-Veeam-Backup-Agent](https://cloudfireit.atlassian.net/wiki/spaces/~239475519/pages/2069234598/New+Gestione+Veeam+Availability+Console+-++Veeam+Cloud+Platform#Installare-Veeam-Backup-Agent)

# Installare Veeam Management Agent

Per installare l’agente è sufficiente seguire questa sezione:

1. All’interno della VAC, selezionare **Discovery**, dalla tab in alto rimanere su **Discovered Computers**, premere su **Download Agent**![](/kb-assets/abe0dc06cf-2022-12-20-15-4233234.png)
2. Selezionare la versione desiderata e **Salvare** il file localmente sul computer.
3. **Eseguire** il file. Verrà eseguito il Wizard di installazione dell’agente.
4. Cliccare **Avanti**![](/kb-assets/83b9763e40-vac-communication-agent-wizard-1.png)
5. Spuntare la voce “**Accetto i termini di licenza…**” e proseguire cliccando **Avanti**![](/kb-assets/1aa0da4514-vac-communication-agent-wizard-2.png)
6. Cliccare su **Installa** e al termine su **Fine**![](/kb-assets/907d025fbd-vac-communication-agent-wizard-finish.png)

## Configurare la Connesione al Management Agent

Per stabilire una connessione tra il Management Agent e la VAC, è sufficiente seguire questi passaggi.

1. Nella sezione **Icone nascoste di Windows**, accanto all’orologio, cercare l’icona relativa al **Management Agent**
2. Cliccare con il tasto destro del mouse sull’icona dell’agente e selezionare **Agent Settings**
3. Inserire le seguenti informazioni per stabilire la connessione:
1.   **Cloud Gateway**: 185.132.69.58
2.   **Port**: 6180
3.   **Username** e **Password** che si usano per accedere alla VAC![](/kb-assets/e3ef852c37-2022-12-20-17-01-53sdasdawweweqw.png)
4. Cliccare su **Apply**
5. Una volta stabilita la connessione, se si ricarica la pagina indicata nel punto 1 della sezione precedente, comparirà la macchina.

:::info
Di default l’agente sarà già configurato con i parametri corretti, nel caso di re-configurazione (vecchia installazione) utilizzare i parametri indicati nel punto 3.
:::

# Installare Veeam Backup Agent

Per installare l’agente di Backup è sufficiente seguire questi passaggi.

1. Dalla voce **Managed Computers** selezionare il dispositivo e cliccare su **Install Backup Agent**![](/kb-assets/78c2e43bb8-2022-12-20-18-02-11.png)
2. Specificare le **credenziali** per accedere al sistema operativo
3. Applicare la configurazione desiderata e premere su **Apply**
4. Attendere il termine dell’Installazione remota dell’agente![](/kb-assets/c110c281ef-2022-12-20-18-34-42.png)

# Configurare Job di Backup

Per configurare e avviare un job di backup direttamente dalla VAC è sufficiente seguire i seguenti passaggi.

1. Cliccare sulla voce **Backup Jobs**, selezionare la macchina o più macchine, premere su **Create Job**![](/kb-assets/ee5090a6dd-2022-12-22-10-10-28.png)
2. Seguire il **Wizard** di configurazione del job di backup![](/kb-assets/af6b919068-2022-12-22-10-23-48.png)
3. Una volta terminata la configurazione, selezionare la macchina e premere su **Start** per avviare il backup![](/kb-assets/500fec9e8d-2022-12-22-10-27-26.png)