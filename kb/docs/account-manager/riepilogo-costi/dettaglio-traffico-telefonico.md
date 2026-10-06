---
title: "Dettaglio traffico telefonico"
---

Questa pagina spiega come leggere ed operare sul file di dettaglio del traffico telefonico (formato CSV) che include l’elenco completo delle telefonate effettuate e ricevute in un determinato intervallo temporale.

Il dettaglio traffico telefonico è disponibile nella sezione [**Fatture**](../fatture/index.md) e può inoltre essere richiesto, anche in versione parziale per il mese corrente, dalla sezione [**Riepilogo costi**](index.md).

:::info
La guida utilizza Microsoft Excel come riferimento. Le funzionalità indicate sono comunque presenti in qualsiasi software per la gestione dei fogli elettronici.
:::

## Apertura del file {#apertura-del-file}

Apri il file utilizzando Microsoft Excel. Il formato dei dati (importi, date, ecc) verrà riconosciuto in automatico secondo la convenzione italiana.

:::warning
Prima di effettuare qualsiasi modifica al file consigliamo di salvarne una copia nel formato nativo del software utilizzato (XLSX nel caso di Microsoft Excel).
:::

Il file contiene l'elenco completo delle telefonate in ingresso ed in uscita.

### Colonne {#colonne}

Di seguito verrà indicata la descrizione di ogni colonna (campo) presente nel file:

|     |     |
| --- | --- |
| **Colonna** | **Descrizione** |
| cliente | Nome del Cliente di riferimento |
| id\_cliente | ID univoco del Cliente di riferimento |
| nome\_progetto | Nome del Progetto di riferimento |
| id\_progetto | ID univoco del Progetto di riferimento |
| nome\_account | Username del Account SIP, espresso come il numero telefonico principale collegato ad esso |
| data\_inizio | Ora di inizio della chiamata, espressa nel formato AAAA-MM-GG hh:mm:ss |
| data\_fine | Ora di fine della chiamata, espressa nel formato AAAA-MM-GG hh:mm:ss |
| durata | Durata della chiamata, espressa in secondi (s) |
| numero\_chiamante | Numero di origine della chiamata (chiamante) |
| numero\_chiamato | Numero di destinazione della chiamata (chiamato) |
| direzione | Direzione della chiamata:<br><br>- out → in caso di chiamata in uscita<br>- in → in caso di chiamata in ingresso |
| costo\_sp | Costo della chiamata per il SP |
| costo\_cliente | Costo della chiamata per il Cliente |

### Righe {#righe}

Nel file viene registrata una nuova riga ogni qualvolta effettuata o ricevuta una telefonata.

### Formattazione {#formattazione}

Per aumentare la leggibilità del contenuto consigliamo di formattare i dati come tabella con intestazioni.

#### Guida passo-passo per Microsoft Excel {#guida-passo-passo-per-microsoft-excel}

1. Seleziona tutte le celle piene nel file
2. Utilizza lo strumento "Formatta come tabella" presente nella TAB "Home" e seleziona uno stile tabella![](/kb-assets/73fcc798f8-formatta-come-tabella.png)
3. Mantieni il flag sulla voce "Tabella con intestazioni" e conferma l'operazione.![](/kb-assets/620036afbe-mantieni-intestazioni.png)

Ora che la formattazione è applicata sarà semplice filtrare il file per singoli Clienti, Account o Numerazioni in modo da ricavare gli importi parziali sia di acquisto che di vendita.

## Operazioni sul file {#operazioni-sul-file}

### Nascondi colonne {#nascondi-colonne}

Per migliorare la leggibilità del file consigliamo di nascondere tutte le colonne che riportano dati tecnici o non di interesse. ES: tutte le colonne riportanti gli ID univoci.

### Totale costi di acquisto {#totale-costi-di-acquisto}

Per ricavare il totale dei costi di acquisto è sufficiente sommare tutti i valori presenti nelle colonne *costo\_sp*.

Per ricavare i parziali per ciascun Cliente, Account o Numerazione è sufficiente applicare un filtro sulla colonna relativa, selezionando il dato desiderato.

### Totale costi di vendita {#totale-costi-di-vendita}

Per ricavare il totale dei costi di acquisto è sufficiente sommare tutti i valori presenti nelle colonne *costo\_cliente*.

Per ricavare i parziali per ciascun Cliente, Account o Numerazione è sufficiente applicare un filtro sulla colonna relativa, selezionando il dato desiderato.