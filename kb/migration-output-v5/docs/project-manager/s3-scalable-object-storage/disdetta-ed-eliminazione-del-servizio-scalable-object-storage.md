---
title: "Disdetta ed eliminazione del servizio - Scalable Object Storage"
---

:::note
Stiamo aggiornando la tua esperienza utente in Cortex. In questo periodo di transizione, è possibile che alcune guide non siano completamente allineate con le novità sul portale.
:::

Questa pagina spiega come **disattivare** ed **eliminare** buckets in Openstack as a Service.

I **buckets** sono contenitori di dati archiviati mediante protocollo S3. Per ciascuno di questi esiste un utente proprietario che può accedervi e gestirne le funzionalità.

## Disattiva un Bucket {#disattiva-un-bucket}

Per disattivare un bucket in Scalable Object Storage puoi seguire i seguenti passaggi:

1. Accedi al servizio **Scalable Object Storage** nella categoria Infrastructure as a Service. Non sai come fare? Segui la nostra [**guida**](gestione-del-servizio-scalable-object-storage/index.md);
2. Premi sul **Nome del bucket** del quale vuoi disattivare al dettaglio.![](/kb-assets/7f52afa352-image-20230619-111419.png)
3. Premi sul bottone **Disattiva bucket** in alto a destra;
4. Premi sul bottone **Disattiva** per confermare l’operazione.

![](/kb-assets/158a09beb4-image-20230619-111243.png)

:::warning
Disattivando il bucket non potrai più sfogliarlo utilizzando le credenziali S3 dell’utente proprietario e tutti i sub-users verranno eliminati.
Tutti i dati e le impostazioni configurate non verranno modificati.
:::

## Elimina bucket {#elimina-bucket}

:::info
**Puoi eliminare un bucket solo se prima lo hai disattivato.**
:::

Per eliminare un bucket in Scalable Object Storage puoi seguire i seguenti passaggi:

1. Accedi al servizio **Scalable Object Storage** nella categoria Infrastructure as a Service. Non sai come fare? Segui la nostra [**guida**](gestione-del-servizio-scalable-object-storage/index.md);
2. Premi sul **Nome del bucket** del quale vuoi eliminare al dettaglio.![](/kb-assets/7f52afa352-image-20230619-111419.png)

![](/kb-assets/42bee71b85-image-20230619-111315.png)

Per eliminare il bucket puoi seguire i seguenti passaggi:

1. Premi sul bottone **Elimina bucket** in alto a destra;
2. Inserisci il testo **conferma-eliminazione** per confermare l’operazione;
3. Premi sul bottone **Elimina** per confermare l’operazione.

:::caution
**Questa operazione non può essere annullata né interrotta.**

[!INFO]
La procedura di eliminazione può impiegare fino a **15 minuti** per completare le operazioni. Se trascorso questo tempo il bucket non risulta **Eliminato** ti invitiamo ad aprire un [**Case**](../../account-manager/supporto/case.md) al nostro supporto.
:::