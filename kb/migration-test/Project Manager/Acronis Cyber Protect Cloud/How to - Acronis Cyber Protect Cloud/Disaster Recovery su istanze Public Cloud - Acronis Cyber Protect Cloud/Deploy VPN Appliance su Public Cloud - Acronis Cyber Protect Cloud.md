Questa guida mostra la corretta configurazione della VPN Appliance, un elemento fondamentale della struttura delle operazioni di Disaster Recovery.  
Senza questo elemento, la macchina in stato di Failover non riuscirebbe a comunicare con i dispositivi in rete su Public Cloud.

## Creare istanza VPN Appliance

Per creare un istanza dedicata alla VPN Appliance di Acronis, è sufficiente seguire queste indicazoni:

1. Effettuare l’accesso con i vostri dati al pannello [Public Cloud](https://public.cloudfire.it)
2. Premere su **Instances** e poi premere su **Launch Instance**
3. Associare un **Instance** **Name** alla tua macchina
4. Nella sezione Source, selezionare **Image** e scegliere le dimensioni della macchina  
Per un’istanza VPN, 10GB sono più che sufficienti.
5. Dall’elenco di ISO disponibili, selezionare **OTHER: Acronis VPN Appliance**
6. Nella sezione **Flavor** scegliere **N1-11**
7. Nella sezione **Networks** scegliere la rete **Private**
8. Premere su **Launch Instance** e attendere il completamento

> [!WARNING]
> Prima di procedere con la configurazione della VPN Appliance tramite console, **disattivare i Security Ports sulla macchina stessa.**  
> Se i Security Ports sulla macchina restano abilitati, la comunicazione tra macchina in Failover e rete locale sarà impossibile.

## Registrare tenant Acronis Cyber Protect

Una volta terminato il building dell’ISO nell’istanza, effettuare l’accesso in console alla macchina con le credenziali di default **admin - admin**  
Proseguire con i seguenti passaggi:

1. Nella sezione **Register** inserire i seguenti valori:  
Backup service address: [https://backup.cloudfire.it](https://backup.cloudfire.it)  
Login: *nome utente del tenant Acronis*  
Password: *password del tenant Acronis*
2. Premere **Invio e confermare**

> [!INFO]
> Se l’operazione va a buon fine compare la scritta **Done**. Se l’operazione non va a buon fine compare la scritta **Error** con relativo dettaglio.

## Configurazioni aggiuntive

Una volta registrata la VPN Appliance sul tenant di Acronis, assegnare un IP Address al VPN Gateway.  
Per farlo, è fondamentale seguire i seguenti passaggi:

1. Nella sezione **Networking** selezionare l’interfaccia di rete disponibile
2. Scegliere **Set static IP address**
3. Sostituire il valore **<nil>** associato alla voce VPN Gateway IP address con un indirizzo **IP disponibile della subnet** del vostro tenant Public Cloud

> [!INFO]
> Se l’operazione va a buon fine compare la scritta **Done**. Se l’operazione non va a buon fine compare la scritta **Error** con relativo dettaglio.

## Riepilogo finale

Una volta terminata questa serie di configurazioni, la situazione sarà come mostrato nei seguenti screenshot.

Sulla VPN Appliance:

![](./attachments/DR%20Acronis%20-%20OpenStack%20-%20VPN%20Appliance.png)

Nella sezione **Disaster recovery → Connectivity**:

![](./attachments/DR%20Acronis%20-%20OpenStack%20-%20Connectivity.png)