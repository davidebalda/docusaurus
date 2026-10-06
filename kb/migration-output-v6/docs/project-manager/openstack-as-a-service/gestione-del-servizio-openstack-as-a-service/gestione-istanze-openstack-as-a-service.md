---
title: "Gestione Istanze - Openstack as a Service"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina spiega come attivare e gestire istanze in Openstack as a Service.

Le istanze sono virtual machine (VM) ospitate nel cloud, con determinate caratteristiche computazionali (Flavor), che possono essere create a partire da un’immagine pubblica o privata.

## Attiva funzionalità Gestione Istanze {#attiva-funzionalita-gestione-istanze}

Per attivare la Gestione istanze puoi seguire i seguenti passaggi:

1. Accedi al servizio **Openstack as a Service** nel menu di navigazione. Non sai come fare? Segui la nostra [**guida**](index.md)**.**
2. Seleziona la voce **Gestione Istanze** nel tab in alto;
3. Premi sul bottone **Attiva gestione istanze** al centro della pagina;
4. Seleziona la **Region** sul quale vuoi attivare il servizio dal selettore in alto a destra.
5. **Imposta (e salva in luogo riservato) una password sicura** per attivare l'accesso al portale di gestione delle istanze Openstack as a Service, lo username verrà generato automaticamente;
6. Seleziona se attivare o meno un router. Questo ti permette di far navigare su internet le tue istanze o renderle raggiungibili tramite la rete. Seleziona l’opzione “*no router*” se intendi personalizzare la rete o utilizzare un tuo firewall in sostituzione a quello fornito di default;
7. Premi sul bottone **Attiva gestione istanze** per confermare l’attivazione.

:::info
La procedura di attivazione può impiegare fino a **10 minuti** per completare le operazioni. Se trascorso questo tempo la pagina non risulta ancora in stato **Attivo** ti invitiamo ad aprire un [**Case**](../../../account-manager/supporto/case.md) al nostro supporto.

[!WARNING]
Al fine di mantenere i requisiti di sicurezza e allinearci alle normative attuali, non siamo tenuti a conservare le password degli utenti in Openstack as a Service. La password di accesso infatti viene **automaticamente resettata** alle **23:59** dell'**ultimo giorno** di **ogni mese**.

[!NOTE]
Ad oggi sono disponibili due region di Openstack as a Service con caratteristiche differenti tra di loro.
Qui trovi i dettagli di ciascuna Region:
- [Milano MI1](https://cloudfire-salesforce.s3.eu-south-1.amazonaws.com/Datasheet/OpenstackAsAServiceMI1Datasheet.pdf)
- [Milano MI2](https://cloudfire-salesforce.s3.eu-south-1.amazonaws.com/Datasheet/OpenstackAsAServiceMI2Datasheet.pdf)
:::

Puoi ora utilizzare le credenziali presenti nella pagina per effettuare l’accesso al portale di gestione delle istanze Openstack as a Service.

## Accedi alla funzionalità Gestione Istanze {#accedi-alla-funzionalita-gestione-istanze}

Per accedere alla Gestione istanze puoi seguire i seguenti passaggi:

1. Accedi al servizio **Openstack as a Service** nel menu di navigazione. Non sai come fare? Segui la nostra [**guida**](index.md)**.**
2. Seleziona la voce **Gestione Istanze** nel tab in alto.

![Screenshot 2024-04-24 at 15.55.52.png](/kb-assets/de10e7661b-screenshot-2024-04-24-at-15-55-52.png)

## Accedi alla dashboard di servizio Openstack as a Service {#accedi-alla-dashboard-di-servizio-openstack-as-a-service}

Per accedere alla dashboard di servizio del Openstack as a Service puoi seguire i seguenti passaggi:

1. Accedi alla voce **Gestione Istanze** nel tab in alto;
2. Premi sul bottone **Accedi**;
3. Premi sul bottone **Login with Cortex** nella pagina **Login MFA** aperta;
4. Effettua il login con le tue **credenziali Cortex**;
5. Inserisci le **credenziali di accesso** alla **dashboard Openstack as a Service**:
1.   Copia lo username dalla pagina gestione istanze;
2.   Inserisci la password salvata al momento della creazione delle istanze.

:::warning
L’accesso alla Region MI2 è possibile attraverso due interfacce, una **new (v2)** e una **legacy**.
Indipendentemente dall’interfaccia scelta, controlla il progetto a cui accedi. In MI2 infatti riesci a visualizzare e ad accedere a tutti i progetti creati direttamente dall’interfaccia.
:::

## Reimposta password del servizio Openstack as a Service {#reimposta-password-del-servizio-openstack-as-a-service}

Al fine di mantenere i requisiti di sicurezza e allinearci alle normative attuali, non siamo tenuti a conservare le password degli utenti in Openstack as a Service. Per questo motivo qualora non avessi più a disposizione la password di accesso è necessario resettare la password e reimpostarne una nuova. Seguendo questi passaggi, la precedente password viene invalidata e sostituita con la password mostrata al momento della creazione.

Per reimpostare la password utile ad accedere alla dashboard di Openstack as a Service puoi seguire i seguenti passaggi:

1. Accedi alla voce **Gestione Istanze** nel tab in alto;
2. Premi sul bottone **Reimposta Password;**
3. Utilizza il bottone **copia** e salvala in luogo sicuro e non accessibile.

:::warning
Per motivi di sicurezza ogni volta che viene richiesta una password di accesso al Openstack as a Service ne viene generata una nuova. Dopo la chiusura della finestra di credenziali Openstack as a Service, non sarà più possibile visualizzare la password, ti consigliamo di copiarla e salvarla in un luogo sicuro.
:::

![](/kb-assets/55e54560a7-image-20230710-130214.png)

## Elimina funzionalità Gestione istanze {#elimina-funzionalita-gestione-istanze}

:::warning
**Prerequisiti di eliminazione**  
Per eliminare la funzionalità Gestione Istanze di quel tenant dovrai prima cancellare all’interno di Openstack:
- tutte le istanze;
- tutti i volumi;
- tutti gli snapshot (sia Volume, sia Image);
- tutti i router e i Floating IP;
- tutte le subnet private.
:::

Per eliminare la Gestione istanze puoi seguire i seguenti passaggi:

1. Accedi al servizio **Openstack as a Service** nel menu di navigazione. Non sai come fare? Segui la nostra [**guida**](index.md)**.**
2. Accedi alla voce **Gestione Istanze** nel tab in alto;
3. Premi sul bottone **Elimina** presente in alto a destra nella pagina;
4. Inserisci il testo **conferma-eliminazione** per confermare l’operazione;
5. Premi sul bottone **Elimina** per avviare l’eliminazione della funzionalità.

![](/kb-assets/9568718cdf-image-20230710-124246.png)

:::caution
**Questa operazione non è reversibile e non può essere annullata né interrotta.**

[!INFO]
La procedura di eliminazione può impiegare fino a **10 minuti** per completare le operazioni. Se trascorso questo tempo la funzionalità non risulta **Disattiva** ti invitiamo ad aprire un [**Case**](../../../account-manager/supporto/case.md) al nostro supporto.
:::