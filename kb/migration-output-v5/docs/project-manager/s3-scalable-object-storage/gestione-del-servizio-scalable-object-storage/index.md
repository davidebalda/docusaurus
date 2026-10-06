---
title: "Gestione del servizio - Scalable Object Storage"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina spiega come attivare e gestire buckets in Openstack as a Service.

I **buckets** sono contenitori di dati archiviati mediante protocollo S3. Per ciascuno di questi esiste un utente proprietario che può accedervi e gestirne le funzionalità.

## Accedi al servizio Scalable Object Storage {#accedi-al-servizio-scalable-object-storage}

Per accedere al servizio Scalable Object Storage puoi seguire i seguenti passaggi:

## Crea un nuovo Bucket {#crea-un-nuovo-bucket}

Per creare un nuovo bucket in Scalable Object Storage puoi seguire i seguenti passaggi:

1. Accedi al servizio **Scalable Object Storage** nella categoria Infrastructure as a Service;
2. Premi il bottone **Nuovo bucket** in alto a destra, oppure al centro della pagina;
3. Inserisci lo **spazio da allocare** per il bucket, potrai aumentare o diminuire il valore anche dopo la creazione del bucket;  
Per impostazione predefinita supportiamo bucket con spazio allocato compreso tra 1 TB e 150 TB, se necessiti di uno spazio maggiore puoi aprire un [**Case**](../../../account-manager/supporto/case.md) al tuo Account Manager per sottoporgli la richiesta.![](/kb-assets/8e1e1b6fc2-image-20230608-085644.png)
4. Seleziona la **Modalità di preservazione dei dati** all’interno del bucket. Non sai quale selezionare? Approfondisci le differenze in questa [**guida**](https://cloudfireit.atlassian.net/l/cp/aRZ1g8tr).![](/kb-assets/605b216b45-image-20230608-085733.png)
1.   Se hai selezionato la modalità di preservazione **Compliace** o **Governance**, inserisci il periodo di preservazione dei dati tra 1 e 365 giorni. Questo è il periodo per il quale tutti i dati all'interno del bucket verranno protetti da sovrascrittura o eliminazione. Potrai aumentare o diminuire il valore anche dopo la creazione del bucket.
2.   Se hai selezionato la modalità di preservazione **Nessuna**, seleziona se abilitare o disabilitare la gestione delle versioni dei file. Potrai modificare questa impostazione anche dopo la creazione del bucket.  
  Per le altre modalità di preservazione la gestione delle versioni è abilitata di default.
5. Inserisci il **nome del bucket**, questo deve essere univoco e non può contenere spazi o lettere maiuscole;
6. Premi sul bottone **Crea bucket** per confermare la creazione;

:::info
La procedura di creazione può impiegare fino a **2 minuti** per completare le operazioni. Se trascorso questo tempo il nuovo bucket non compare nella lista in stato **Attivo** ti invitiamo ad aprire un [**Case**](../../../account-manager/supporto/case.md) al nostro supporto.

[!TIP]
Una volta completata la creazione ti verranno mostrate le **credenziali S3 (Access key ID e Secret access key)** dell’utente proprietario, che potrai utilizzare per accedere al bucket.

[!WARNING]
Per motivi di sicurezza, la Secret access key non verrà più mostrata dopo la creazione del bucket. Ti consigliamo di salvarla in quel momento e conservarla in un luogo sicuro.
:::

## Accedi al dettaglio di un bucket {#accedi-al-dettaglio-di-un-bucket}

Per accedere al dettaglio di un bucket creato in Scalable Object Storage puoi seguire i seguenti passaggi:

1. Accedi alla **Scalable Object Storage** nella categoria Infrastructure as a Service;
2. Premi sul **Nome del bucket** del quale vuoi accedere al dettaglio.

![](/kb-assets/7f52afa352-image-20230619-111419.png)

### Azioni disponibili {#azioni-disponibili}

Queste sono le azioni disponibili dalla pagina di dettaglio del bucket.

#### Collegamento tramite Cloud Storage Browser {#collegamento-tramite-cloud-storage-browser}

Per sfogliare il contenuto del bucket e operare sugli oggetti contenuti come utente proprietario devi utilizzare un **Cloud storage browser**.

![](/kb-assets/a54705b907-image-20230619-111154.png)

Per impostare il collegamento puoi seguire i seguenti passaggi:

1. Premi sul bottone **Cloud Storage Browser** in alto a destra;
2. Seleziona il Cloud Storage Browser tra quelli supportati ([**S3cmd**](https://s3tools.org/s3cmd) o [**Cyberduck**](https://cyberduck.io/download/)), verrà scaricato il file di configurazione già compilato con Server/URL di accesso e Access key ID del bucket;![](/kb-assets/9e19850858-image-20230608-091506.png)
3. **Importa** il file di configurazione sul Cloud Storage Browser e inserisci la Secret access key precedentemente salvata per accedere al bucket.

:::info
Se utilizzi un altro Cloud Storage Browser puoi trovare il **Server/URL** nella TAB [**Overview**](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/2117763087/Scalable+Object+Storage#Overview) e l'**Access key ID** nell’intestazione di pagina, sotto al nome del bucket.
:::

#### Reimposta credenziali S3 {#reimposta-credenziali-s3}

Se vuoi disabilitare l’accesso esistente o hai dimenticato la Secret access key, puoi reimpostare le credenziali S3 dell’utente proprietario del bucket.

![](/kb-assets/8ffe51e5b1-image-20230619-111228.png)

Per reimpostare le credenziali puoi seguire i seguenti passaggi:

1. Premi sul bottone **Reimposta credenziali S3** in alto a destra;
2. Premi sul bottone **Reimposta** per confermare l’operazione.

:::tip
Una volta completata l’operazione ti verranno mostrate le **nuove credenziali S3** (Access key ID e Secret access key) dell’utente proprietario, che potrai utilizzare per accedere al bucket.

[!WARNING]
Le vecchie credenziali verranno **eliminate** e perderai l’accesso al bucket dovunque queste siano state configurate. Dovrai riconfigurare gli accessi utilizzando le nuove credenziali appena generate.
:::

#### Disattiva bucket {#disattiva-bucket}

Puoi disattivare il bucket per interrompervi momentaneamente l’accesso mediante le credenziali S3 del suo utente proprietario.

![](/kb-assets/158a09beb4-image-20230619-111243.png)

Per disattivare il bucket puoi seguire i seguenti passaggi:

1. Premi sul bottone **Disattiva bucket** in alto a destra;
2. Premi sul bottone **Disattiva** per confermare l’operazione.

:::warning
Disattivando il bucket non potrai più sfogliarlo utilizzando le credenziali S3 dell’utente proprietario e tutti i sub-users verranno eliminati.
Tutti i dati e le impostazioni configurate non verranno modificati.
:::

#### Riattiva bucket {#riattiva-bucket}

Puoi riattivare il bucket per ripristinarvi l’accesso mediante le credenziali S3 del suo utente proprietario.

Per riattivare il bucket puoi seguire i seguenti passaggi:

1. Premi sul bottone **Riattiva bucket** in alto a destra;
2. Premi sul bottone **Riattiva** per confermare l’operazione.

:::warning
Tutti i dati e le impostazioni configurate non verranno modificati.
:::

#### Elimina bucket {#elimina-bucket}

![](/kb-assets/42bee71b85-image-20230619-111315.png)

Per eliminare il bucket puoi seguire i seguenti passaggi:

1. Premi sul bottone **Elimina bucket** in alto a destra;
2. Inserisci il testo **conferma-eliminazione** per confermare l’operazione;
3. Premi sul bottone **Elimina** per confermare l’operazione.

:::caution
**Questa operazione non può essere annullata né interrotta.**

[!INFO]
La procedura di eliminazione può impiegare fino a **15 minuti** per completare le operazioni. Se trascorso questo tempo il bucket non risulta **Eliminato** ti invitiamo ad aprire un [**Case**](../../../account-manager/supporto/case.md) al nostro supporto.
:::

### Overview {#overview}

Nella TAB **Overview** puoi visualizzare il **Server/URL** di accesso, da configurare in un **cloud storage browser.**

:::info
Per effettuare l’accesso ti occorreranno anche le credenziali S3 (Access Key ID e Secret Access Key) dell’utente proprietario del bucket o di uno dei suoi sub-users.
:::

![](/kb-assets/48d8e2a666-image-20230619-111446.png)

### Sub-users {#sub-users}

Nella TAB **Sub-users** puoi visualizzare i sub-users creati e i loro permessi di accesso.

I sub-users sono utenti con funzionalità limitate che hanno accesso al bucket, sui quali è possibile impostare permessi di **sola lettura** o **scrittura** dei dati all’interno del bucket stesso.

![](/kb-assets/d13366daed-image-20230619-111836.png)

Per creare un sub-user puoi seguire i seguenti passaggi:

1. Premi sul bottone **Nuovo** **sub-user** in alto a destra;
2. Seleziona il permesso da applicare all’utente sul bucket tra:
1.   **Sola lettura**: l’utente potrà solamente leggere i dati all'interno del bucket. Questi non potrà caricare nuovi file, modificare i dati esistenti o agire sulle impostazioni del bucket.
2.   **Lettura e scrittura**: l’utente potrà leggere e scrivere dati all'interno del bucket.Questi potrà caricare nuovi file e modificare i dati esistenti ma non agire sulle impostazioni del bucket.![](/kb-assets/9f958976fb-image-20230608-091111.png)
3. Inserisci il **nome** per il sub-user;
4. Premi sul bottone **Crea sub-user** per confermare la creazione.

:::tip
Una volta completata la creazione ti verranno mostrate le **credenziali S3 (Access key ID e Secret access key)** del sub-user, che potrai utilizzare per accedere al bucket.

[!WARNING]
Per motivi di sicurezza, la Secret access key non verrà più mostrata dopo la creazione del sub-user. Ti consigliamo di salvarla in quel momento e conservarla in un luogo sicuro.
:::

#### Collegamento tramite Cloud Storage Browser {#collegamento-tramite-cloud-storage-browser-1}

Per sfogliare il contenuto del bucket e operare sugli oggetti contenuti come sub-user devi utilizzare un **Cloud storage browser**.

Per impostare il collegamento puoi seguire i seguenti passaggi:

1. Premi sul bottone **Cloud Storage Browser** in corrispondenza del sub-user;
2. Seleziona il Cloud Storage Browser tra quelli supportati ([**S3cmd**](https://s3tools.org/s3cmd) o [**Cyberduck**](https://cyberduck.io/download/)), verrà scaricato il file di configurazione già compilato con Server/URL di accesso e Access key ID del bucket;
3. **Importa** il file di configurazione sul Cloud Storage Browser e inserisci la Secret access key precedentemente salvata per accedere al bucket.

:::info
Se utilizzi un altro Cloud Storage Browser puoi trovare il **Server/URL** nella TAB [**Overview**](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/2117763087/Scalable+Object+Storage#Overview) e l'**Access key ID** in pagina, in corrispondenza del sub-user.
:::

![](/kb-assets/6512c3a26c-image-20230619-111858.png)

#### Elimina sub-user {#elimina-sub-user}

Puoi eliminare il sub-user per interrompere in modo permanente le possibilità di accesso al bucket mediante le sue credenziali S3.

Per eliminare il sub-user puoi seguire i seguenti passaggi:

1. Premi sul bottone **Elimina** in corrispondenza del sub-user;
2. Premi sul bottone **Elimina** per confermare l’operazione.

:::caution
**Questa operazione non può essere annullata né interrotta.**
:::

![](/kb-assets/4875316d93-image-20230619-111918.png)

### Impostazioni {#impostazioni}

Nella TAB **Impostazioni** puoi visualizzare e modificare le configurazioni del bucket.

Per modificare le impostazioni del bucket puoi seguire i seguenti passaggi:

1. Premi sul bottone **Modifica** in basso a destra;
2. Modifica le impostazioni ai nuovi valori che vuoi impostare;
3. Premi sul bottone **Salva** in basso a destra.

:::warning
Alcune impostazioni potrebbero non essere modificabili in base alla modalità di preservazione dei dati selezionata.
:::

![](/kb-assets/43a31649ba-image-20230619-112030.png)