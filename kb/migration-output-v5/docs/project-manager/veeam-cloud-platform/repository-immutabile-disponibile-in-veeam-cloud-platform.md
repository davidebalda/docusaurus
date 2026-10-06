---
title: "Repository Immutabile disponibile in Veeam Cloud Platform"
---

Questa pagina spiega i motivi per cui è disponibile il **Repository Immutabile** in Veeam Cloud Platform.

Non è un segreto che una forte sicurezza dei dati sia uno dei requisiti più critici nel mondo odierno. Con le reti costantemente prese di mira e aggredite tramite attacchi automatizzati, tentativi di phising o attacchi ransomware, i tuoi backup devono essere protetti. Senza un backup affidabile e protetto, il ripristino diventa significativamente più complicato, se non impossibile.

La risposta a questa esigenza può essere soddisfatta seguendo una strategia di backup **3-2-1-1-0** secondo cui è consigliabile avere **3 copie dei dati, su 2 media diversi, con 1 copia off-site, con 1 copia offline con air gap o immutabile e con 0 errori**.

Grazie all’ultima release di Veeam Cloud Platform, le nuove repliche in Cloud (Backup Resources e Disaster Recovery) **utilizzeranno di default un repository immutabile**, rafforzando ancor di più i tuoi piani di ripristino senza la necessità di uno storage predisposto come S3. La regola del 3-2-1-1-0 viene così ulteriormente rafforzata, garantendo che la copia off-site sia già immutabile.

D’ora in poi, Veeam Cloud Platform utilizzerà infatti **Veeam Hardened Repository** come repository di default, una soluzione creata appositamente per garantire backup immutabili, sicuri e affidabili, assicurando che i dati siano recuperabili in caso di disastro. Il precedente repository non sarà più attivabile. [**Scopri di più su Veeam Hardened Repository**](https://www.veeam.com/blog/immutable-backup-solutions-linux-hardened-repository.html)**.**

## Quali vantaggi ottieni con il Repository Immutabile in Veeam Cloud Platform? {#quali-vantaggi-ottieni-con-il-repository-immutabile-in-veeam-cloud-platform}

- **Maggior Sicurezza**: Il repository immutabile protegge i dati da modifiche non autorizzate e ransomware, conservando le copie di backup in modo sicuro per un periodo di 7 giorni. Questo periodo non è modificabile o personalizzabile.
- **Maggior Conformità e Resilienza dei Dati**: Questo repository soddisfa gli ultimi standard di sicurezza consigliati da Veeam, garantendo una gestione dei dati all'avanguardia e senza rischi.
- **Maggior Accessibilità all’Immutabilità**: I backup immutabili diventano tali direttamente con Veeam Cloud Connect, mantenendo semplicità e fruibilità tutt’ora in uso.

:::note
L’utilizzo di Backup Resources con Repository Immutabile non sostituisce l’utilizzo di un Repository S3 con Object Lock per ottenere l’immutabilità.
L’utilizzo di uno storage S3 infatti è consigliato per il recupero emergenziale e per il dato freddo, che non necessita di particolari performance nel restore e nel recupero.
CloudFire ci tiene infatti a ricordarti che per una strategia di backup efficiente è consigliabile utilizzare entrambe le soluzioni: **Backup off-site, da oggi immutabile, e Scalable Object Storage S3 Immutabile**.
:::

- **Maggiori performance**: utilizzando il Repository Immutabile disponi della funzionalità di WAN accelerator che rende più veloci i job di backup e ripristino.
- **Controllo sicuro sui costi:** attraverso la modalità disponibile di repository con Pay per allocation mantieni stabili e costanti i costi del servizio.

## Cosa cambia? {#cosa-cambia}

1. **Nuove Attivazioni**: Ottieni automaticamente il repository immutabile sulla region Milano MI1. Non devi fare nulla di aggiuntivo.
2. **Clienti Esistenti**: Se hai già attivato Backup Resources in Veeam Cloud Platform, puoi continuare ad utilizzare il servizio normalmente. É prevista una migrazione graduale e semplificata al nuovo repository immutabile. Segui questa [guida per la migrazione](https://cloudfireit.atlassian.net/wiki/x/AwB2lw).