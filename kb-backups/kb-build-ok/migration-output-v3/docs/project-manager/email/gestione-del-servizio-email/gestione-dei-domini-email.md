---
title: "Gestione dei Domini - Email"
---

Questa pagina spiega come Attivare ed Eliminare i Domini.

- **Attivare** un Dominio permette di renderlo disponibile sul servizio per la creazione di Caselle email e Liste di distribuzione.
- **Eliminare** un Dominio cancella tutti i dati a questo collegati.

# Prerequisiti di attivazione

Per attivare il servizio devi disporre di un **Dominio registrato** presso uno dei numerosi provider o hosting presenti in rete.

:::warning
Su Cortex è possibile utilizzare solamente Domini registrati e verificati. La registrazione del Dominio deve essere gestita separatamente.
:::

# Domini

Il Dominio è il nome di uno spazio Internet ben preciso, come un sito web. In genere è composto dal nome di una organizzazione seguito da un suffisso Internet standard, come [http://nomeazienda.it](http://nomeazienda.it) oppure [*universita.edu*](http://universita.edu).

:::info
Ad esempio, il tuo Dominio potrebbe essere [**azienda.it**](http://azienda.it) e potresti avere il sito web [*www.azienda.it*](http://www.azienda.it) e l'indirizzo email [*info@azienda.it*](mailto:info@azienda.it)*.*
:::

## Accedi alla sezione Domini

Per accedere al sezione Domini puoi seguire i seguenti passaggi:

1. Accedi al servizio **Email** dalle voci di menù laterale. Non sai come fare? Segui la nostra [**guida**](index.md#Accedi-al-servizio-Email).
2. Seleziona la voce **Domini** dalle voci di menù laterale
3. Seleziona la voce **Domini** dalle tab di navigazione in alto.

![](/kb-assets/d5f5ea575a-image-20220908-103833.png)

## Attiva un Dominio

Per attivare un Dominio è sufficiente seguire questi passaggi:

1. Premi il bottone **Nuovo Dominio** posto in basso a destra nella pagina.
2. Inserisci il **Dominio** che vuoi attivare sul servizio, una eventuale **Descrizione** nella finestra di dialogo che ti compare e premi sul bottone **Inserisci.**
3. Visualizzerai nuovamente la pagina Domini con il nuovo Dominio in stato **Da verificare**.
4. A questo punto dovrai verificare di essere il proprietario del Dominio inserito.

![](/kb-assets/b242a696ae-image-20220906-115628.png)

## Verifica del Dominio

:::info
La verifica del Dominio è un’operazione di sicurezza volta a dimostrare che il Dominio inserito sia realmente di tua proprietà. Una volta completata questa operazione potrai procedere alla creazione di Caselle email e Liste di distribuzione.
:::

Per verificare un Dominio è sufficiente seguire questi passaggi:

1. Accedi alla sezione **domini.**
2. Premi l’azione **Verifica** posto in corrispondenza del dominio appena aggiunto.  
![](/kb-assets/c786fb0855-image-20220906-115959.png)
3. Segui le istruzioni per [verificare il Dominio tramite inserimento di un record DNS](https://cloudfireit.atlassian.net/wiki/spaces/~478399111/pages/1776746531/Gestione+dei+Domini+-+Email#Verificare-un-Dominio-tramite-inserimento-record-DNS) all’interno della finestra di dialogo.
4. Premi il bottone **Verifica** in basso a destra nella finestra di dialogo![](/kb-assets/ba7e6a29d1-email-domini-5.png)
5. Al termine del processo questo passerà in stato **Attivo** ed il Dominio risulterà utilizzabile per la configurazione del servizio

:::info
La propagazione del record DNS può durare da pochi minuti ad alcune ore, in base al registrar del dominio. Se il record è stato correttamente propagato ma non risulta comunque possibile completare la verifica del dominio ti invitiamo ad aprire un [**Case**](../../../account-manager/supporto/case.md) al nostro supporto.

[!NOTE]
Se è stato inserito un dominio errato o risulta impossibile procedere alla sua verifica è possibile eliminare il dominio premendo sul bottone **Elimina**. Visualizzerai nuovamente la pagina **Overview**.
:::

### Verificare un Dominio tramite inserimento record DNS

Per inserire il record bisogna disporre di una zona DNS dedicata al domino, poi procedere con i seguenti passaggi:

1. Aggiungere un Nuovo Record
2. Compilare il puntatore al dominio (ES. “[nuovodominio.it](http://nuovodominio.it)” oppure “@” se il gestore DNS è automatico)
3. Impostare **TTL** del nuovo record a **3600**
4. Impostare **tipologia** di record **TXT**
5. Inserire il contenuto (**Target**) del nuovo record con il codice univoco mostrato nella finestra: CF-xxxxxxxx
6. Salvare la modifica importata
7. Attendere la propagazione del record

## Effettua la configurazione tecnica del Dominio

:::warning
Procedere con questa operazione solo dopo aver verificato il Dominio.
:::

Per il corretto funzionamento e una maggiore sicurezza del Dominio è necessario inserire all’interno della zona DNS dedicata ulteriori record.  
Per visualizzare questi valori basta seguire questi passaggi:

1. Accedi alla sezione **domini.**
2. Premi il bottone **Configurazioni tecniche** in corrispondenza del dominio che vuoi implementare.
3. Segui le istruzioni per [verificare il Dominio tramite inserimento di un record DNS](https://cloudfireit.atlassian.net/wiki/spaces/~478399111/pages/1776746531/Gestione+dei+Domini+-+Email#Verificare-un-Dominio-tramite-inserimento-record-DNS) utilizzando i parametri visibili nella finestra di dialogo.![](/kb-assets/b4674f5449-email-domini-17.png)

:::warning
Verificare con il proprio register la piena compatibilità dei valori, ad esempio la corretta gestione di chiavi a 2048 bit per il DKIM.

[!INFO]
L’inserimento di questi record nella configurazione DNS è necessario per gestire in modo corretto l’indirizzamento ai nomi host, al mail exchanger e ad altre informazioni fondamentali per la presenza del dominio sulla rete internet.
:::

## Modifica un Dominio

:::warning
Una volta creato e verificato un Dominio non è possibile modificarne il **Nome** ma solo la **Descrizione**. Procedere dunque con l’eliminazione del Dominio attivato oppure con l’aggiunta del Dominio corretto ripercorrendo la fase di creazione.
:::

Per procedere alla modifica di un Dominio è sufficiente seguire questi passaggi:

1. Accedi alla sezione **domini.**
2. Premi il bottone **Modifica** in corrispondenza del dominio che vuoi modificare.
3. Premi il bottone **Modifica** dopo aver inserito o modificato la **Descrizione** del Dominio.

## Elimina un Dominio

Per eliminare un Dominio è sufficiente seguire questi passaggi:

1. Accedi alla sezione **domini.**
2. Premi il bottone **Elimina** in corrispondenza del dominio che vuoi eliminare.
3. Premi il bottone **Conferma** nella finestra di dialogo per eliminare il dominio, visualizzerai nuovamente la pagina Domini senza più il Dominio eliminato.

:::info
Nel caso in cui non è possibile procedere con l’eliminazione del Dominio assicurarsi che non siano presenti elementi, come ad esempio Caselle email o Alias di dominio, ad esso relativi. Eliminarli prima di eliminare il Dominio.

[!CAUTION]
L’eliminazione di un Dominio comporta l’eliminazione di **TUTTI** i dati ad esso relativi. **L’operazione non può essere annullata**.
:::

# Alias di dominio

L' alias di dominio è una impostazione che permette di avere più domini che puntano ad uno stesso sito web condividendone i contenuti ed il pannello di controllo, ad esempio se il dominio [*miodominio1.com*](http://miodominio1.com) è alias del dominio [*miodominio2.it*](http://miodominio2.it) visitando [*miodominio1.com/index.html*](http://miodominio1.com/index.html) e [*miodominio2.com/index.html*](http://miodominio2.com/index.html) vedrai la stessa pagina.

## Accedi alla sezione Alias di dominio

Per accedere al sezione Domini puoi seguire i seguenti passaggi:

1. Accedi al servizio **Email** dalle voci di menù laterale. Non sai come fare? Segui la nostra [**guida**](index.md#Accedi-al-servizio-Email).
2. Seleziona la voce **Domini** dalle voci di menù laterale
3. Seleziona la voce **Alias di dominio** dalle tab di navigazione in alto.

![](/kb-assets/a028ccfb04-image-20220906-120327.png)

## Crea un Alias di Dominio

Dopo aver verificato lo stato del Dominio, puoi accedere alla sezione riservata per la creazione degli **Alias di dominio**. Questi consentono di utilizzare un altro indirizzo per lo stesso dominio.

Per creare un Alias di dominio è sufficiente seguire questi passaggi:

1. Accedi al Progetto nel quale vuoi creare l’Alias di Dominio, seleziona la voce **Email** dal menu di navigazione e poi la voce **Domini**.
2. Seleziona la voce **Alias domini** dalla barra di navigazione orizzontale presente nella Dashboard.
3. Premi il bottone **Nuovo alias di dominio** posto in basso a destra nella pagina.
4. Seleziona il **Dominio**, inserisci il nome dell’**Alias di Dominio** che vuoi creare, una eventuale **Descrizione** e premi sul bottone **Crea alias**.
5. Visualizzerai nuovamente la pagina Alias Domini con il nuovo Alias di Dominio in stato **Da verificare**.

![](/kb-assets/16124e076a-image-20220906-120452.png)

## Verifica Alias di Dominio

:::info
La verifica dell’Alias di Dominio è un’operazione di sicurezza volta a dimostrare che il Dominio inserito sia realmente di tua proprietà. Una volta completata questa operazione potrai procedere alla creazione di Caselle email e Liste di distribuzione utilizzando l’Alias.
:::

Per verificare un Alias di Dominio è sufficiente seguire questi passaggi:

1. Premi il bottone **Verifica** posto in basso a destra nella pagina.
2. Segui le istruzioni per [verificare il Dominio tramite inserimento di un record DNS](https://cloudfireit.atlassian.net/wiki/spaces/~478399111/pages/1776746531/Gestione+dei+Domini+-+Email#Verificare-un-Dominio-tramite-inserimento-record-DNS) all’interno della finestra di dialogo.
3. Premi il bottone **Verifica** in basso a destra nella finestra di dialogo.![](/kb-assets/89a720f1b6-email-domini-10.png)
4. Al termine del processo questo passerà in stato **Attivo** e l’Alias di Dominio risulterà utilizzabile per la creazione di Caselle email e Alias di caselle email.![](/kb-assets/5e2eaea495-email-domini-11.png)

:::info
La propagazione del record DNS può durare da pochi minuti ad alcune ore, in base al registrar del dominio. Se il record è stato correttamente propagato ma non risulta comunque possibile completare la verifica del dominio ti invitiamo ad aprire un [**Case**](../../../account-manager/supporto/case.md) al nostro supporto.

[!NOTE]
Se è stato inserito un Alias di Dominio errato o risulta impossibile procedere alla sua verifica è possibile eliminarlo premendo sul bottone **Elimina**.
:::

## Elimina Alias di dominio

Per eliminare un Alias di dominio è sufficiente seguire questi passaggi:

1. Accedi al Progetto nel quale vuoi eliminare un Alias di dominio, seleziona la voce **Email** nel menu di navigazione e poi la voce **Domini**.
2. Seleziona la voce **Alias domini** dalla barra di navigazione orizzontale presente nella Dashboard.
3. Premi il bottone **Elimina** in corrispondenza dell’alias di dominio che vuoi eliminare.
4. Premi il bottone **Conferma** nella finestra di dialogo per eliminare l’Alias di dominio, visualizzerai nuovamente la pagina Alias domini senza più l’Alias di dominio eliminato.

:::info
Nel caso in cui non è possibile procedere con l’eliminazione dell’Alias di dominio assicurarsi che non siano presenti elementi, come ad esempio Caselle email o Alias di caselle email, ad esso relativi. Eliminarli prima di eliminare l’Alias di dominio.

[!CAUTION]
L’eliminazione di un Alias di dominio comporta l’eliminazione di **TUTTI** i dati ad esso relativi. **L’operazione non può essere annullata**.
:::

**Sommario**

- [Prerequisiti di attivazione](#prerequisiti-di-attivazione)
- [Domini](#domini)
-   [Accedi alla sezione Domini](#accedi-alla-sezione-domini)
-   [Attiva un Dominio](#attiva-un-dominio)
-   [Verifica del Dominio](#verifica-del-dominio)
  
  -   [Verificare un Dominio tramite inserimento record DNS](#verificare-un-dominio-tramite-inserimento-record-dns)
-   [Effettua la configurazione tecnica del Dominio](#effettua-la-configurazione-tecnica-del-dominio)
-   [Modifica un Dominio](#modifica-un-dominio)
-   [Elimina un Dominio](#elimina-un-dominio)
- [Alias di dominio](#alias-di-dominio)
-   [Accedi alla sezione Alias di dominio](#accedi-alla-sezione-alias-di-dominio)
-   [Crea un Alias di Dominio](#crea-un-alias-di-dominio)
-   [Verifica Alias di Dominio](#verifica-alias-di-dominio)
-   [Elimina Alias di dominio](#elimina-alias-di-dominio)