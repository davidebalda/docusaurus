---
title: "Pianificazione del backup job - Acronis Cyber Protect Cloud"
---

:::tip
É disponibili un Quick start relativo all' [**Attivazione e Configurazione di**](https://www.cloudfire.it/tech-talks/quick-start-acronis-cyber-backup) **Acronis Cyber Protect Cloud**.
:::

Questa pagina spiega come pianificare il job di backup correttamente (anche definito protection plan).

Con il termine pianificare un job di backup, si intende **definire le policy di retention** di un job, e per farlo correttamente occorre eseguire una corretta schedulazione.

# Guida passo-passo

Se già disponi di un Protection Plan o job di backup e intendi definirne la pianificazione è necessario seguire i seguenti passaggi:

1. Seleziona la voce **Management** nel menù a sinistra,
2. Seleziona la voce **Protection Plans**
3. Premi sul Nome del Job di cui vuoi modificare la pianificazione
4. Premi sul menù a destra su **edit**
5. Apri il menù a tendina che trovi nella sezione **Backup**
6. Premi su **Schedule.**

Nella sezione **Schedule** o **pianificazione** puoi modificare ed eseguire la pianificazione dei backup che desideri.

:::note
La pianificazione, attiva di default in fase di creazione di un job, ha le impostazioni come da immagine.
:::

![](/kb-assets/ba38ca84a6-retention1.png)

- Nello specifico, lo **schema di backup** definisce la modalità in cui vengono effettuati ed archiviati i backup. Le opzioni sono le seguenti:
-   **Sempre incrementale (a file singolo)** è l'opzione di default, eseguirà un solo backup completo iniziale per poi, in ogni circostanza, eseguire un incrementale.  
  In base ai suoi algoritmi interni definirà e ricostruirà i backup "Full" in base alla retention specificata.
-   **Sempre completo**, come indica il nome farà ad ogni occorrenza il backup per intero della risorsa.
-   Le altre tre voci sono un composto di occorrenze di backup "**Full**", "**Differenziali**" ed "**Incrementali**".

:::info
Il **differenziale** è un backup completo costruito trasportando solo le differenze ed applicandole sul full precedente.
:::

- Nella sezione "**Personalizzato**" puoi definire lo schema in base alle necessità, alternando i meccanismi a disposizione.

:::note
La pianificazione di default è "**oraria**", ovvero si indica l'orario di esecuzione dei job in giorni specifici.  
Le altre tre voci, che trovi nel menù a tendina, sono da utilizzare nel caso volessi avere i backup distanziati da uno specifico intervallo oppure all'avvio/arresto del sistema.
:::

![](/kb-assets/53778d23ee-retention2.png)

- Di default L'attività pianificata verrà eseguita in base all'ora locale della macchina è spuntata su Backup settimanale.

:::info
Si consiglia di utilizzare il backup "**Giornaliero**" per una gestione più semplice della retention.  
Quello che può accadere è un'eccessiva ridondanza dei retention points: impostando per esempio il settimanale, con spuntati i giorni da lunedì a venerdì, alle ore 13.00.  
Visto che la modalità è "settimanale", la **retention indicata nel campo successivo**, nella configurazione del job, è applicata AD OGNUNO DEI GIORNI selezionati.
:::

![](/kb-assets/dd137aeacc-retention3.png)

Seguendo l'esempio nell'immagine avremo quindi 7 giornalieri per lunedì, 7 per martedì, 7 per mercoledì e così via.  
Allo stesso modo avremo 4 settimanali del backup di lunedì, 4 settimanali di martedì ecc..  
I mensili seguono lo stesso concetto. La retention complessiva sarà di 7+4+6 punti moltiplicati per i 5 giorni: 85.

Eseguendo il backup in modalità daily, avremo invece una gestione lineare: le policy di pulizia manterranno gli ultimi 7 backup giornalieri, 4 settimanali e 6 mensili (ovviamente in riferimento all'immagine del punto precedente).

:::info
Si può eseguire il giornaliero ogni giorno, oppure da lunedì a venerdì.
:::

![](/kb-assets/6f5e37c86c-retention4.png)

Le ulteriori opzioni permettono di gestire al meglio lo stato della macchina e le sue condizioni per eseguire il backup.

  

[](https://cloudfireit.atlassian.net/wiki/plugins/servlet/confluence/placeholder/unknown-macro?name=easy-heading-free&locale=en_US&version=2)

:::note
**Articoli collegati**


##### Filter by label

There are no items with the selected labels at this time.
:::