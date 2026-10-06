---
title: "Dettaglio costi servizi"
---

Questa pagina spiega come leggere ed operare sul file di dettaglio costi servizi (formato CSV) che include l’elenco completo dei consumi registrati in un determinato intervallo temporale.

La registrazione dei consumi di tutti i servizi avviene su base **oraria per garantire** la massima flessibilità. I consumi riportati all’interno del dettaglio sono basati su intervalli orari e ed utilizzano i prezzi orari dei prodotti come riferimento

Il dettaglio costi servizi è disponibile per il periodo di riferimento nella sezione [**Fatture**](../fatture/index.md) e può inoltre essere richiesto, anche in versione parziale per il mese corrente, dalla sezione [**Riepilogo costi**](index.md).

:::info
La guida utilizza Microsoft Excel come riferimento. Le funzionalità indicate sono comunque presenti in qualsiasi software per la gestione dei fogli elettronici.
:::

# Lettura del file

Apri il file utilizzando Microsoft Excel. Il formato dei dati (importi, date, ecc) verrà riconosciuto in automatico secondo la convenzione italiana.

:::warning
Prima di effettuare qualsiasi modifica al file consigliamo di salvarne una copia nel formato nativo del software utilizzato (XLSX nel caso di Microsoft Excel).
:::

Il file contiene l'elenco completo delle registrazioni dei consumi di ciascun prodotto.

## Colonne

Di seguito verrà indicata la descrizione di ogni colonna (campo) presente nel file:

|     |     |
| --- | --- |
| **Colonna** | **Descrizione** |
| account\_id | Nome dell’Account di riferimento |
| service\_provider | Nome del Service Provider di riferimento |
| sp\_id | ID univoco del Service Provider di riferimento |
| nome\_listino\_sp | Nome del Listino applicato al Service Provider |
| id\_listino\_sp | ID univoco del Listino applicato al Service Provider |
| cliente | Nome del Cliente di riferimento (coincide con *service\_provider* in caso il consumo sia relativo a quest'ultimo) |
| id\_cliente | ID univoco del Cliente di riferimento (coincide con *sp\_id* in caso il consumo sia relativo a quest'ultimo) |
| tipologia\_cliente | tipologia cliente (si riferisce a quanto selezionato in fase di creazione di un nuovo cliente) |
| nome\_listino\_cliente | Nome del Listino applicato al Cliente di riferimento (coincide con *nome\_listino\_sp* in caso il consumo sia relativo a quest'ultimo) |
| id\_listino\_cliente | ID univoco del Listino applicato al Service Provider (coincide con *id\_listino\_sp* in caso il consumo sia relativo a quest'ultimo) |
| nome\_progetto | Nome del Progetto di riferimento |
| id\_progetto | ID univoco del Progetto di riferimento |
| servizio | Servizio al quale appartiene il prodotto |
| prodotto | Nome del prodotto registrato |
| quantita | Quantità del prodotto registrato espressa in unità |
| data\_inizio\_utilizzo | Data ed ora di inizio della registrazione del consumo |
| data\_fine\_utilizzo | Data ed ora di fine della registrazione del consumo |
| ore\_utilizzo | Ore di utilizzo del prodotto nella registrazione del consumo (ottenuta come differenza tra *data\_fine\_utilizzo* e *data\_inizio\_utilizzo*) |
| tot\_ore\_utilizzo | Totale di ore di utilizzo del prodotto nella registrazione del consumo (ottenuta come moltiplicazione tra *quantita* e *ore\_utilizzo*) |
| costo\_unitario\_sp | Canone unitario del prodotto per il SP su base oraria o mensile |
| costo\_totale\_sp | Canone totale del prodotto per il SP nella registrazione del consumo (ottenuto come moltiplicazione tra *tot\_ore\_utilizzo* e *costo\_unitario\_sp*) |
| costo\_attivazione\_sp | Costo di attivazione del prodotto per il SP nella registrazione del consumo |
| costo\_unitario\_cliente | Canone unitario del prodotto per il Cliente su base oraria o mensile |
| costo\_totale\_cliente | Canone totale del prodotto per il Cliente nella registrazione del consumo (ottenuto come moltiplicazione tra *tot\_ore\_utilizzo* e *costo\_unitario\_cliente*) |
| costo\_attivazione\_cliente | Costo di attivazione del prodotto per il Cliente nella registrazione del consumo |

## Righe

Nel file viene registrata una nuova riga ogni qualvolta, per un singolo prodotto di un singolo cliente, varia almeno uno di questi campi:

- *quantita* → a causa di una riduzione o aumento di consumo
- *costo\_unitario\_sp* → a causa di una modifica sui prezzi del Listino di acquisto, compresa l’applicazione di promo
- *costo\_attivazione\_sp* → a causa di una modifica sui prezzi del Listino di acquisto, compresa l’applicazione di promo
- *costo\_unitario\_cliente* → a causa di una modifica sui prezzi del Listino di vendita
- *costo\_attivazione\_cliente* → a causa di una modifica sui prezzi del Listino di vendita

La nuova riga avrà *data\_inizio\_utilizzo* valorizzata con data ed ora immediatamente successive alla *data\_fine\_utilizzo* della riga precedente per quello specifico prodotto.

## Formattazione

Per aumentare la leggibilità del contenuto consigliamo di formattare i dati come tabella con intestazioni.

### Guida passo-passo per Microsoft Excel

1. Seleziona tutte le celle piene nel file
2. Utilizza lo strumento "Formatta come tabella" presente nella TAB "Home" e seleziona uno stile tabella![](/kb-assets/73fcc798f8-formatta-come-tabella.png)
3. Mantieni il flag sulla voce "Tabella con intestazioni" e conferma l'operazione.![](/kb-assets/620036afbe-mantieni-intestazioni.png)

Ora che la formattazione è applicata sarà semplice filtrare il file per singoli clienti, servizi o prodotti in modo da ricavare gli importi parziali sia di acquisto che di vendita.

# Operazioni sul file

Di seguito è riportato un breve elenco di operazioni che è possibile effettuare sul file.

## Nascondi colonne

Per migliorare la leggibilità del file consigliamo di nascondere tutte le colonne che riportano dati tecnici o non di interesse. ES: tutte le colonne riportanti gli ID univoci.

## Calcola il totale dei costi di acquisto

Per ricavare il totale dei costi di acquisto è sufficiente sommare tutti i valori presenti nelle colonne *costo\_totale\_sp* e *costo\_attivazione\_sp*.

Per ricavare i parziali per ciascun cliente, servizio o prodotto è sufficiente applicare un filtro sulla colonna relativa, selezionando il dato desiderato

## Calcola il totale dei costi di vendita

Per ricavare il totale dei costi di vendita è sufficiente sommare tutti i valori presenti nelle colonne *costo\_totale\_cliente* e *costo\_attivazione\_cliente.*

Per ricavare i parziali per ciascun cliente, servizio o prodotto è sufficiente applicare un filtro sulla colonna relativa, selezionando il dato desiderato.