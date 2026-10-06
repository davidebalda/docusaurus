---
title: "Disdetta ed eliminazione Openstack as a Service"
---

# Elimina funzionalità Gestione istanze in Openstack as Service

:::warning
**Prerequisiti di eliminazione**  
Per eliminare la funzionalità Gestione Istanze di quel tenant dovrai prima cancellare all’interno di Openstack:
- tutte le istanze;
- tutti i volumi;
- tutti gli snapshot (sia Volume, sia Image con stato settato “Private”);
- tutti i router e i Floating IP;
- tutte le subnet private.
:::

Per eliminare la Gestione istanze puoi seguire i seguenti passaggi:

1. Accedi al servizio **Openstack as a Service** nel menu di navigazione. Non sai come fare? Segui la nostra [**guida**](gestione-del-servizio-openstack-as-a-service/index.md)**.**
2. Accedi alla voce **Gestione Istanze** nel tab in alto;
3. Premi sul bottone **Elimina** presente in alto a destra nella pagina;
4. Inserisci il testo **conferma-eliminazione** per confermare l’operazione;
5. Premi sul bottone **Elimina** per avviare l’eliminazione della funzionalità.

![](/kb-assets/a76ca21f46-image-20230710-124246.png)

:::caution
**Questa operazione non è reversibile e non può essere annullata né interrotta.**

[!INFO]
La procedura di eliminazione può impiegare fino a **10 minuti** per completare le operazioni. Se trascorso questo tempo la funzionalità non risulta **Disattiva** ti invitiamo ad aprire un [**Case**](../../account-manager/supporto/case.md) al nostro supporto.
:::