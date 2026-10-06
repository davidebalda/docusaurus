---
title: "Listini"
---

Questa pagina spiega come visualizzare e gestire i Listini di vendita su Cortex.

## Accedi alla pagina Listini {#accedi-alla-pagina-listini}

Per accedere alla pagina Listini puoi seguire i seguenti passaggi:

1. Effettua il **login** su Cortex, verrai indirizzato su **Account Manager**;
2. Effettua l’accesso a **Partner Portal** utilizzando il bottone apposito in alto a destra. Il portale si aprirà in una nuova tab del browser
3. Seleziona la voce **Listini** dal menu di navigazione laterale

Nella pagina è riportato l’elenco dei Listini di vendita creati, comprensivi di nome, indicatore di listino predefinito, azioni rapide e stato.

:::info
Il Listino di vendita denominato **Prezzo al pubblico** è sempre presente e visibile in pagina. Questo non è modificabile o eliminabile e può essere utilizzato come riferimento per i prezzi di mercato consigliati e per la creazione di nuovi listini.
Se non vengono creati ulteriori Listini di vendita, il listino Prezzo al pubblico viene utilizzato come listino predefinito alla creazione dei Clienti.
:::

![](/kb-assets/f0d13c85bf-image-20220905-103917.png)

## Crea nuovo Listino {#crea-nuovo-listino}

Puoi creare nuovi Listini per modificare i prezzi di vendita dei singoli prodotti ed applicare condizioni personalizzate ai tuoi Clienti

Per creare un nuovo Listino puoi seguire i seguenti passaggi:

1. Premi il bottone **Nuovo listino** posto in alto a destra nella sezione;
2. Inserisci il **Nome** da applicare al nuovo listino nella finestra di dialogo;
3. Seleziona il **Listino di partenza** da utilizzare per la creazione del nuovo listino nella finestra di dialogo;
4. Premi il bottone **Crea listino** nella finestra di dialogo per confermare l’operazione, verrà ricaricata la lista Listini con il nuovo Listini in stato **Attivo**.

:::info
Tutti i prezzi di vendita nuovo listino verranno ereditati dal listino selezionato in fase di creazione.
:::

![](/kb-assets/ccf1ca1fe4-image-20220905-104039.png)

## Accedi al dettaglio Listino {#accedi-al-dettaglio-listino}

Nel dettaglio del Listino sono riportati tutti i Prodotti con i propri prezzi di acquisto e vendita.

Per accedere al dettaglio di un Listino puoi seguire i seguenti passaggi:

1. Premi sul **Nome** del Listino nella lista dei listini.

![](/kb-assets/18bd35c4c4-image-20220905-104602.png)

### Stati dei Prodotti {#stati-dei-prodotti}

Un Prodotto può assumere i seguenti stati:

- **Attivo** → Prodotto richiedibile ed attivabile.
- **Deprecato** → Prodotto non più richiedibile e mantenuto solo per la rilevazione dei consumi. Potrebbe venire dismesso ed eliminato senza preavviso.

### Visualizza prezzi orari e mensili {#visualizza-prezzi-orari-e-mensili}

É possibile visualizzare i prezzi di acquisto e vendita dei Prodotti in formato orario o mensile.

Per modificare la visualizzazione del prezzo dei Prodotti puoi seguire i seguenti passaggi:

1. Premi sul bottone di selezione **Prezzi mensili/Prezzi orari** posto in alto a destra nella sezione

:::info
I prezzi di riferimento dei prodotti sono quelli **orari**. I prezzi mensili sono calcolati automaticamente, basandosi su un mese di 730 ore. L'importo presente in fattura potrebbe variare in funzione delle ore effettive del mese.

[!NOTE]
I prezzi **mensili** sono espressi con valori a **2 cifre decimali**. I prezzi **orari** sono espressi con valori a **5 cifre decimali**.
:::

### Modifica prezzi di vendita {#modifica-prezzi-di-vendita}

Puoi modificare i prezzi di vendita di ciascuno dei prodotti presenti sul listino, agendo direttamente sul prezzo o sulla percentuale di ricarico.

Per modificare il prezzo di vendita di un Prodotto puoi seguire i seguenti passaggi:

1. Scorri la pagina fino a trovare il prodotto selezionato, puoi anche avvalerti della ricerca e dei filtri per velocizzare l’operazione;
2. Premi il bottone **Modifica** posto in corrispondenza del prodotto, all’estrema destra della riga;
3. Inserisci il nuovo **prezzo di vendita** o opera sulla **percentuale di ricarico**. In base al valore sul quale agisci l’altro verrà ricalcolato automaticamente;
4. Premi il bottone **Salva** posto in corrispondenza del prodotto, all’estrema destra della riga;
5. Verifica il nuovo prezzo impostato sia correttamente mostrato in corrispondenza del prodotto.

:::info
La visualizzazione dei prezzi in formato orario o mensile determina anche il prezzo di riferimento in fase di modifica:
- Se viene modificato il prezzo mensile, il prezzo orario verrà automaticamente calcolato dividendo il prezzo mensile per 730. ES: Impostando il prezzo di un prodotto a **10,00€/mese**, il suo prezzo orario verrà calcolato come 10,00/730=**0,01370€/ora**.
- Se viene modificato il prezzo orario, il prezzo mensile verrà automaticamente calcolato moltiplicando il prezzo mensile per 730. ES: Impostando il prezzo di un prodotto a **0,00274€/mese**, il suo prezzo mensile verrà calcolato come 0,00274\*730=**2,00€/mese**.

[!WARNING]
La raccolta dei consumi e la fatturazione si basa sui **prezzi orari**. Se vuoi avere la massima precisione sugli importi ti consigliamo di operare sui prezzi orari ed utilizzare i prezzi mensili come stima indicativa.
:::

![](/kb-assets/07cb8f10bb-image-20220908-092528.png)

### Imposta listino predefinito {#imposta-listino-predefinito}

Il Listino impostato come predefinito è quello selezionato automaticamente alla creazione di nuovi Clienti.

Per impostare un Listino come predefinito puoi seguire i seguenti passaggi:

1. Premi sul bottone **Imposta predefinito** posto in alto a destra nella pagina;
2. Visualizzerai un messaggio di **conferma** avvenuta operazione.

![](/kb-assets/d74451cbfa-image-20220908-092602.png)

### Modifica nome listino {#modifica-nome-listino}

Per modificare il nome di un Listino puoi seguire i seguenti passaggi:

1. Premi sul bottone **Modifica** posto accanto al nome del listino nella sezione listini, il bottone compare solo quando avvicini il puntatore al nome del Listino;
2. Inserisci il nuovo **Nome** del Listino;
3. Premi il bottone **Conferma** accanto al nome del Listino.

![](/kb-assets/32dac0767c-image-20220908-092905.png)

### Elimina listino {#elimina-listino}

:::info
Per eliminare un Listino questo non deve più risultare assegnato ad alcun Cliente.
:::

Per eliminare il listino puoi seguire i seguenti passaggi:

1. Premi il bottone **Elimina listino** posto in alto a destra nella pagina;
2. Premi il bottone **Elimina** nella finestra di dialogo per confermare l’operazione.

:::caution
L’eliminazione del cliente è un’operazione **definitiva** ed **irreversibile**.
:::

![](/kb-assets/2b10768236-image-20220908-092623.png)