---
title: "Configurazione Recovery Server per Disaster Recovery su Public Cloud - Acronis Cyber Protect Cloud"
---

Questa guida mostra come configurare correttamente i recovery server per eseguirne un orchestrazione perfetta e non intercorrere in problematiche quando si eseguono le operazioni di Disaster Recovery.

## Configurare il Recovery Server {#configurare-il-recovery-server}

1. Accedere alla dashboard sul sito [https://backup.cloudfire.it](https://backup.cloudfire.it)
2. Nella sezione **Devices**, selezionare il server che si vuole proteggere
3. Dalla tab visualizzata a destra, premere su **Disaster Recovery**
4. Premere su **Create recovery server**
5. Dalla tab **General**:
1.   \[Obbligatorio\] Scegliere il quantitativo di **Risorse computazionali** del server di ripristino
2.   \[Obbligatorio\] Specificare il **MAC address** del server in produzione su Public Cloud  
  Potete trovarlo andando su: nome istanza → **Interfaces**
3.   \[Obbligatorio\] Specificare indirizzo **IP della macchina in produzione**  
  Di default, viene inserito da Acronis sfruttando l’agente installato sulla macchina
4.   \[Obbligatorio\] Spuntare la voce **Internet Access** per abilitare la navigazione durante lo stato di Failover della macchina
5.   \[Facoltativo\] Spuntare la voce **Use public IP address** se la macchina ospita servizi aperti a internet
6.   \[Facoltativo\] Impostare RPO spuntando la voce **Set RPO threshold**
7.   \[Facoltativo\] Assegnare un nome al Recovery Server
6. Dalla tab **Cloud firewall rules**:
1.   Impostare regole **Inbound** → Allow all
2.   Impostare regole **Outbound** → Allow all
3.   Implementare regole di firewall in un secondo momento
7. Premere su **Create**

Una volta terminata la configurazione di sopra mostrata, la situazione sarà la seguente, come mostrato negli screenshot:

Dalla tab **Devices**:

![](/kb-assets/b4c58b05c0-dr-acronis-openstack-recovery-ok.png)

Dalla tab **Disaster Recovery → Servers**:

![](/kb-assets/06f7121880-dr-acronis-openstack-recovery-ok-2.png)