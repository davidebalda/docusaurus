---
title: "Protection Plans - Acronis Cyber Protect Cloud"
---

:::tip
É disponibili un Quick start relativo all' [**Attivazione e Configurazione di**](https://www.cloudfire.it/tech-talks/quick-start-acronis-cyber-backup) **Acronis Cyber Protect Cloud**.
:::

Acronis Cyber Protect Cloud offre molta flessibilità per quanto riguarda la gestione dei propri backup, offrendo infatti vari piani ed opzioni per personalizzare e mettere in sicurezza le vostre macchine, sia fisiche che virtuali.

Queste opzioni sono chiamate si trovano e definiscono il ***Protection Plan***, che questa guida vi mostrerà come creare e modificare.

- [Crea un Protection Plan - Guida passo-passo](#crea-un-protection-plan-guida-passo-passo)
- [Protection features](#protection-features)

### Crea un Protection Plan - Guida passo-passo {#crea-un-protection-plan-guida-passo-passo}

1. Accedi al tuo account attraverso Cortex, se non sai come segui la nostra [**Guida**](https://cloudfireit.atlassian.net/l/cp/5SixzfnP).
2. Sulla sinistra, sotto la sezione *Devices*, premi il bottone **Plans** e seleziona **Protection**.  
![](/kb-assets/de46e99de3-acronis-plans.png)
3. Nella pagina trovai una lista dei piani attivi - per crearne uno nuovo, premi su **Create Plan** (sotto Actions).  
![](/kb-assets/0ee88a6b19-create-plan.png)
4. A questo punto vi si aprirà una schermata per la creazione del vostro Protection Plan; prima di poter cominciare però dovrete aggiungere *almeno* una macchina.![](/kb-assets/162455f4f6-plantype.png)
  
![](/kb-assets/c0f79952ef-add-device.png)
5. Seleziona una o più macchine, facendo però attenzione che abbiano caratteristiche simili, dato che alcune opzioni potrebbero non essere supportate su sistemi diverso.  
![](/kb-assets/aec28c6008-select-device.png)
6. Date un nome al vostro piano.  
![](/kb-assets/c219d2f6e3-specify-name.png)
7. Seleziona tutte le opzioni che vi interessano - una volta soddisfatti, cliccate su **Create**.  
![](/kb-assets/61fe1d4704-featurelist.png)

:::info
Se doveste selezionare un’opzione non supportata dalla macchina, riceverete un messaggio d’errore.

[!WARNING]
Alcune features sono disponibili solo quando **funzionalità di protezione avanzate** sono attive.
:::

### Protection features {#protection-features}

Come già visto, esistono varie features che possono essere selezionate - qui di seguito potete trovare le loro funzioni.

- **Disaster Recovery:** permette l’accesso alla propria infrastruttura o macchina in caso di emergenza, ripristinandone i sistemi.
- **Anti-virus e Anti-Malware Protection:** protezione contro virus e malware. Permette la scansione manuale, ed è completamente personalizzabile (*compatibile con sistemi Linux e MacOS*).
- **URL filtering:** permette di controllare la navigazione verso vari URL da parte di dispositivi aziendali.
- **Windows Defender Anti-Virus & Windows Security Essentials:** antivirus per sistemi WinPe; permette la sincronizzazione con gli antivirus già presenti su Windows.
- **Vulnerability Assessment:** applicabile su qualunque OS, è un tool che analizza il sistema per verificare che non ci siano vulnerabilità. Può essere utilizzato sia on-demand sia personalizzando l’ora ed il giorno della scansione automatica.
- **Patch Management:** gestisce ed aggiorna varie patch, verificando che siano sicure per il sistema - può essere automatizzato o attivato manualmente.
- **Data Protection Map:** visualizza vari stored data per verificare l’integrità di file importanti. Almeno due assessment devono essere fatti per ottenere una mappatura completa.
- **Device Control:** monitoraggio e accesso a device di ogni tipo, applicando e personalizzando le protection features da device a device.

:::tip
Se si desiderasse controllare le attività delle features tramite interfaccia web basterà recarsi nella sezione **Activities**.
:::