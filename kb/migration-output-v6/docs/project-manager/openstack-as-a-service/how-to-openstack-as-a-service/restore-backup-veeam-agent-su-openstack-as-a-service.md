---
title: "Restore backup Veeam Agent su Openstack as a Service"
---

## Premessa: {#premessa}

:::note
Questa guida si applica in caso di ripristino di server fisici e/o istanze virtuali il cui backup è stato eseguito con Veeam Windows agent, sia in modalità *managed* che *stand-alone*.
:::

La procedura è suddivisa in 3 fasi:

- [1\. Creazione dell’istanza temporanea](#1-creazione-dell-istanza-temporanea)
- [2\. Restore](#2-restore)
- [3\. Creazione della macchina definitiva](#3-creazione-della-macchina-definitiva)

### 1\. Creazione dell’istanza temporanea {#1-creazione-dell-istanza-temporanea}

:::note
Su Openstack non è possibile creare direttamente la macchina definitiva in quanto il tool di Recovery di Veeam è una ISO che non è progettata per lavorare come immagine, occorre quindi creare una VM effimera che renda avviabile l'ISO.
:::

1. Accedi ad Openstack e cerca l’immagine “**Veeam Recovery Media**”
2. Clicca su **Launch**

![1.png](/kb-assets/9dbc003335-1.png)

1. Imposta un **nome** per l’istanza

![2-20250527-093057.png](/kb-assets/4afb222dd0-2-20250527-093057.png)

1. Lascia l’impostazione **default** per non creare nuovo volume

![3-20250527-093117.png](/kb-assets/33d7d511d6-3-20250527-093117.png)

1. Utilizza obbligatoriamente un **Flavor G2-XX** e non G2S-XX

![4-20250527-093530.png](/kb-assets/1a356738f6-4-20250527-093530.png)

1. Seleziona una rete che consenta la navigazione della macchina e avvia l’istanza.

![5-20250527-093321.png](/kb-assets/49db8d7cfd-5-20250527-093321.png)

### 2\. Restore {#2-restore}

1. Crea un nuovo volume che diventerà il disco **definitivo** dell’istanza

![4.1.png](/kb-assets/5bdce2e255-4-1.png)

1. Collega il nuovo volume alla istanza temporanea

![5.1.png](/kb-assets/d292025eed-5-1.png)

1. Nella console dell’istanza fare click su **Tools**

![1.1.png](/kb-assets/5003cdb798-1-1.png)

1. Clicca su **Load Driver**

![2.1.png](/kb-assets/37295daf1d-2-1.png)

1. Installa i driver **ethernet**

![3.1.png](/kb-assets/f883f52be6-3-1.png)

1. Installa i driver **SCSI**

![6.1.png](/kb-assets/caac6a2765-6-1.png)

1. Torna indietro ed avvia il ripristino

![7.1.png](/kb-assets/a7cbcb0cbc-7-1.png)

1. Seleziona il network storage

![8.1.png](/kb-assets/3ce134c3de-8-1.png)

1. Inserisci il FQDN Cloud Connect

![10.1.png](/kb-assets/eb5facdea3-10-1.png)

1. Seleziona il backup desiderato

![11.1.png](/kb-assets/930c380f49-11-1.png)

1. Seleziona il restore point

![12.1.png](/kb-assets/36bab5fc0b-12-1.png)

1. Seleziona **entire computer** e clicca su **finish**

![13.1.png](/kb-assets/985b9f9c8c-13-1.png)

1. Clicca no al reboot e **spegni** la macchina

![14.1.png](/kb-assets/4ffa88abeb-14-1.png)

### 3\. Creazione della macchina definitiva {#3-creazione-della-macchina-definitiva}

:::note
Da questo momento è possibile distruggere l’istanza temporanea.
:::

1. Modifica il volume definitivo e rendilo “bootable”

![1.2.png](/kb-assets/7d88d5ead9-1-2.png)

1. Lancia l’istanza definitiva dal volume

![2.2.png](/kb-assets/b2ec6c037b-2-2.png)

1. Seleziona ora un Flavour **G2S-XX**

![3.2.png](/kb-assets/ea36ab6bc7-3-2.png)

1. Seleziona la rete definitiva e avviare l’istanza

![4.2.png](/kb-assets/5eddfd38fb-4-2.png)