---
title: "Flavor e Storage Disponibili in Openstack as a Service - V2"
---

La presente guida ha il compito di evidenziare quali sono i Flavor disponibili in Openstack as a Service.

Le principali tipologie di Flavor disponibili sono due:  

![](/kb-assets/00dc4edf9b-general-purposes-icon-1.png)

**General Purpose v2: Architettura Intel Xeon Gold Scalable su hardware Dell PowerEdge per applicazioni Enterprise**

Flavor ideato appositamente per applicazioni Enterprise come applicazioni Business, servizi Web, centralini VoIP, cluster di container Kubernetes ed una vastissima gamma di servizi cloud-native. Rappresenta un buon bilanciamento tra costi e prestazioni per un altissimo range di applicazioni cloud.

![](/kb-assets/07c9d4d78d-cpu-optimized-icon-1.png)

**CPU Optimized v2 : Architettura Intel Xeon Gold Scalable su hardware Dell PowerEdge per applicazioni mission-critical**

Flavor potente, ideato per ottenere il massimo delle prestazioni computazionali per applicazioni specifiche quali Database server, HPC, Machine learning ed analisi dei dati. Risulta perfetto per eseguire applicazioni mission-critical sensibili alle latenze, con il massimo delle performance e con CPU di ultima generazione.

## Nuova Tipologia di Storage

Per **entrambe** due le **tipologie di Flavor** è possibile avere a disposizione un Direct Attached Storage estremamente performante a costi contenuti.  

Ecco le differenze:  

![](/kb-assets/d3d0c73219-das.png)

- Storage ad alte prestazioni connessi direttamente alle risorse compute;
- Tecnologia SSD per i flavor General Purpose mentre tecnologia NVME per i flavor CPU Optimized;
- Migliori performance garantite, la replica avviene su un singolo sito azzerando le latenze di accesso;
- Resilienza del dato limitata alla singola Availability Zone.
- Dimensione del volume fissa, non è possibile estendere o ridurre il volume.

![](/kb-assets/9c870c5202-scalable-storage.png)

- Flavor in cui non è integrata la componente Storage, garantita un’alta resilienza del dato grazie alla maggior ridondanza dello stesso;
- Multi tier in base alle esigenze: LTS, Standard e SSD;
- Performance di livello enterprise basate sulla dimensione dei volumi;
- 3x Replica in più availability zone per garantire un’integrità del dato senza compromessi;
- Dati sempre disponibili per le applicazioni senza la necessità di implementare algoritmi di alta affidabilità.

  
Di seguito la tabella dei Flavor disponibili per le istanze Openstack as a Service:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **SKU Flavor** | **vCPUs** | **RAM** | **Prodotto** | **Descrizione** |
| **General Purpose Direct Attached Storage DAS** |     |     |     |     |
| PC-MI1-G211 | 1   | 1   | Openstack as a Service - Region MI1 - Flavor G2-11 | General purpose \| 1 vCPU - 1GB Ram \| 2,1 Ghz per vCPU \| 30 GB SSD \| Gigabit Interfaces |
| PC-MI1-G212 | 1   | 2   | Openstack as a Service - Region MI1 - Flavor G2-12 | General purpose \| 1 vCPU - 2GB Ram \| 2,1 Ghz per vCPU \| 60 GB SSD  \| Gigabit Interfaces |
| PC-MI1-G224 | 2   | 4   | Openstack as a Service - Region MI1 - Flavor G2-24 | General purpose \| 2 vCPU - 4GB Ram \| 2,1 Ghz per vCPU \| 120GB SSD  \| Gigabit Interfaces |
| PC-MI1-G228 | 2   | 8   | Openstack as a Service - Region MI1 - Flavor G2-28 | General purpose \| 2 vCPU - 8GB Ram \| 2,1 Ghz per vCPU \| 240GB SSD  \| Gigabit Interfaces |
| PC-MI1-G248 | 4   | 8   | Openstack as a Service - Region MI1 - Flavor G2-48 | General purpose \| 4 vCPU - 8GB Ram \| 2,1 Ghz per vCPU \| 240GB SSD  \| Gigabit Interfaces |
| PC-MI1-G246 | 4   | 16  | Openstack as a Service - Region MI1 - Flavor G2-416 | General purpose \| 4 vCPU - 16GB Ram \| 2,1 Ghz per vCPU \| 480 SSD \| Gigabit Interfaces |
| PC-MI1-G256 | 6   | 16  | Openstack as a Service - Region MI1 - Flavor G2-616 | General purpose \| 6 vCPU - 16GB Ram \| 2,1 Ghz per vCPU \| 480 SSD \| Gigabit Interfaces |
| PC-MI1-G226 | 4   | 32  | Openstack as a Service - Region MI1 - Flavor G2-432 | General purpose \| 4 vCPU - 32GB Ram \| 2,1 Ghz per vCPU \| 960 SSD \| Gigabit Interfaces |
| PC-MI1-G262 | 8   | 32  | Openstack as a Service - Region MI1 - Flavor G2-832 | General purpose \| 8 vCPU - 32GB Ram \| 2,1 Ghz per vCPU \| 960 SSD \| Gigabit Interfaces |
| PC-MI1-G232 | 16  | 32  | Openstack as a Service - Region MI1 - Flavor G2-1632 | General purpose \| 16 vCPU - 32GB Ram \| 2,1 Ghz per vCPU \| 960 SSD \| Gigabit Interfaces |
| PC-MI1-G264 | 16  | 64  | Openstack as a Service - Region MI1 - Flavor G2-1664 | General purpose \| 16 vCPU - 64GB Ram \| 2,1 Ghz per vCPU \| 1920 SSD \| Gigabit Interfaces |
| PC-MI1-G296 | 20  | 96  | Openstack as a Service - Region MI1 - Flavor G2-2096 | General purpose \| 20 vCPU - 96GB Ram \| 2,1 Ghz per vCPU \| 2880 SSD \| Gigabit Interfaces |
| PC-MI1-G228 | 24  | 128 | Openstack as a Service - Region MI1 - Flavor G2-24128 | General purpose \| 24 vCPU - 128GB Ram \| 2,1 Ghz per vCPU \| 3840 SSD \| Gigabit Interfaces |
| PC-MI1-G292 | 32  | 192 | Openstack as a Service - Region MI1 - Flavor G2-32192 | General purpose \| 32 vCPU - 192GB Ram \| 2,1 Ghz per vCPU \| 5760 SSD \| Gigabit Interfaces |
| **General Purpose - Scalable Storage** |     |     |     |     |
| PC-MI1-G2S1 | 1   | 1   | Openstack as a Service - Region MI1 - Flavor G2S-11 | General purpose \| 1 vCPU - 1GB Ram \| 2,6 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-G2S2 | 1   | 2   | Openstack as a Service - Region MI1 - Flavor G2S-12 | General purpose \| 1 vCPU - 2GB Ram \| 2,6 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-G2S3 | 2   | 4   | Openstack as a Service - Region MI1 - Flavor G2S-24 | General purpose \| 2 vCPU - 4GB Ram \| 2,6 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-G2SB | 2   | 8   | Openstack as a Service - Region MI1 - Flavor G2S-28 | General purpose \| 2 vCPU - 8GB Ram \| 2,6 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-G2S4 | 4   | 8   | Openstack as a Service - Region MI1 - Flavor G2S-48 | General purpose \| 4 vCPU - 8GB Ram \| 2,6 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-G2SC | 4   | 16  | Openstack as a Service - Region MI1 - Flavor G2S-416 | General purpose \| 4 vCPU - 16GB Ram \| 2,6 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-G2S5 | 6   | 16  | Openstack as a Service - Region MI1 - Flavor G2S-616 | General purpose \| 6 vCPU - 16GB Ram \| 2,6 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-G2SD | 4   | 32  | Openstack as a Service - Region MI1 - Flavor G2S-432 | General purpose \| 4 vCPU - 32GB Ram \| Xeon Gold 2,1 Ghz per vCPU \| Only Scalable Storage \| Gigabit Interfaces |
| PC-MI1-G2S6 | 8   | 32  | Openstack as a Service - Region MI1 - Flavor G2S-832 | General purpose \| 8 vCPU - 32GB Ram \| 2,6 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-G2SB | 16  | 32  | Openstack as a Service - Region MI1 - Flavor G2S-1632 | General purpose \| 16 vCPU - 32GB Ram \| Xeon Gold 2,1 Ghz per vCPU \| Only Scalable Storage \| Gigabit Interfaces |
| PC-MI1-G2S7 | 16  | 64  | Openstack as a Service - Region MI1 - Flavor G2S-1664 | General purpose \| 16 vCPU - 64GB Ram \| 2,6 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-G2S8 | 20  | 96  | Openstack as a Service - Region MI1 - Flavor G2S-2096 | General purpose \| 20 vCPU - 96GB Ram \| 2,6 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-G2S9 | 24  | 128 | Openstack as a Service - Region MI1 - Flavor G2S-24128 | General purpose \| 24 vCPU - 128GB Ram \| 2,6 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-G2SA | 32  | 192 | Openstack as a Service - Region MI1 - Flavor G2S-32192 | General purpose \| 32 vCPU - 192GB Ram \| 2,6 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| **CPU Optimized - Direct Attached Storage DAS** |     |     |     |     |
| PC-MI1-C201 | 2   | 4   | Openstack as a Service - Region MI1 - Flavor C2-24 | CPU Optimized \| 2 vCPU - 4GB Ram \|  3,00 Ghz per vCPU \| 80 GB NVME \| Gigabit Interfaces |
| PC-MI1-C202 | 4   | 8   | Openstack as a Service - Region MI1 - Flavor C2-48 | CPU Optimized \| 4 vCPU - 8GB Ram \|  3,00 Ghz per vCPU \| 160 GB NVME \| Gigabit Interfaces |
| PC-MI1-C203 | 8   | 16  | Openstack as a Service - Region MI1 - Flavor C2-816 | CPU Optimized \| 8 vCPU - 16GB Ram \|  3,00 Ghz per vCPU \| 320 GB NVME \| Gigabit Interfaces |
| PC-MI1-C204 | 16  | 32  | Openstack as a Service - Region MI1 - Flavor C2-1632 | CPU Optimized \| 16 vCPU - 32GB Ram \|  3,00 Ghz per vCPU \| 640 GB NVME \| Gigabit Interfaces |
| PC-MI1-C205 | 32  | 64  | Openstack as a Service - Region MI1 - Flavor C2-3264 | CPU Optimized \| 32 vCPU - 64GB Ram \|  3,00 Ghz per vCPU \| 1280 GB NVME \| Gigabit Interfaces |
| PC-MI1-C206 | 48  | 96  | Openstack as a Service - Region MI1 - Flavor C2-4896 | CPU Optimized \| 48 vCPU - 96GB Ram \|  3,00 Ghz per vCPU \| 1920 GB NVME \| Gigabit Interfaces |
| PC-MI1-C207 | 50  | 128 | Openstack as a Service - Region MI1 - Flavor C2-50128 | CPU Optimized \| 50 vCPU - 128GB Ram \|  3,00 Ghz per vCPU \| 2560 GB NVME \| Gigabit Interfaces |
| PC-MI1-C208 | 56  | 256 | Openstack as a Service - Region MI1 - Flavor C2-56256 | CPU Optimized \| 56 vCPU - 256GB Ram \|  3,00 Ghz per vCPU \| 5120 GB NVME \| Gigabit Interfaces |
| PC-MI1-C209 | 64  | 384 | Openstack as a Service - Region MI1 - Flavor C2-64384 | CPU Optimized \| 64 vCPU - 384GB Ram \|  3,00 Ghz per vCPU \| 7680 GB NVME \| Gigabit Interfaces |
| **CPU optimized - Scalable storage** |     |     |     |     |
| PC-MI1-C2S1 | 2   | 4   | Openstack as a Service - Region MI1 - Flavor C2S-24 | CPU Optimized \| 2 vCPU - 4GB Ram \|  3,00 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-C2S2 | 4   | 8   | Openstack as a Service - Region MI1 - Flavor C2S-48 | CPU Optimized \| 4 vCPU - 8GB Ram \|  3,00 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-C2S3 | 8   | 16  | Openstack as a Service - Region MI1 - Flavor C2S-816 | CPU Optimized \| 8 vCPU - 16GB Ram \|  3,00 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-C2S4 | 16  | 32  | Openstack as a Service - Region MI1 - Flavor C2S-1632 | CPU Optimized \| 16 vCPU - 32GB Ram \|  3,00 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-C2S5 | 32  | 64  | Openstack as a Service - Region MI1 - Flavor C2S-3264 | CPU Optimized \| 32 vCPU - 64GB Ram \|  3,00 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-C2S6 | 48  | 96  | Openstack as a Service - Region MI1 - Flavor C2S-4896 | CPU Optimized \| 48 vCPU - 96GB Ram \|  3,00 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-C2S7 | 50  | 128 | Openstack as a Service - Region MI1 - Flavor C2S-50128 | CPU Optimized \| 50 vCPU - 128GB Ram \|  3,00 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-C2S8 | 56  | 256 | Openstack as a Service - Region MI1 - Flavor C2S-56256 | CPU Optimized \| 56 vCPU - 256GB Ram \|  3,00 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |
| PC-MI1-C2S9 | 64  | 384 | Openstack as a Service - Region MI1 - Flavor C2S-64384 | CPU Optimized \| 64 vCPU - 384GB Ram \|  3,00 Ghz per vCPU \| Only Scalable Storage  \| Gigabit Interfaces |

Sono tuttavia ancora disponibili i seguenti Flavor, non previsti con la nuova infrastruttura

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **SKU Flavor** | **vCPUs** | **RAM** | **Prodotto** | **Descrizione** |
| PC-FVR-G111 | 1   | 1   | VM G1-11 | General purpose \| 1 vCPU - 1GB Ram \| 2,6 Ghz per vCPU |
| PC-FVR-G112 | 1   | 2   | VM G1-12 | General purpose \| 1 vCPU - 2GB Ram \| 2,6 Ghz per vCPU |
| PC-FVR-G163 | 16  | 32  | VM G1-1632 | General purpose \| 16 vCPU - 32GB Ram \| 2,6 Ghz per vCPU |
| PC-FVR-G124 | 2   | 4   | VM G1-24 | General purpose \| 2 vCPU - 4GB Ram \| 2,6 Ghz per vCPU |
| PC-FVR-G148 | 4   | 8   | VM G1-48 | General purpose \| 4 vCPU - 8GB Ram \| 2,6 Ghz per vCPU |
| PC-FVR-G181 | 8   | 16  | VM G1-816 | General purpose \| 8 vCPU - 16GB Ram \| 2,6 Ghz per vCPU |
| PC-FVR-R128 | 24  | 128 | VM R1-128 | RAM Optimized \| 24 vCPU - 128GB Ram \| 2,6 Ghz per vCPU |
| PC-FVR-R116 | 4   | 16  | VM R1-16 | RAM Optimized \| 4 vCPU - 16GB Ram \| 2,6 Ghz per vCPU |
| PC-FVR-R132 | 8   | 32  | VM R1-32 | RAM Optimized \| 8 vCPU - 32GB Ram \| 2,6 Ghz per vCPU |
| PC-FVR-R154 | 16  | 64  | VM R1-64 | RAM Optimized \| 16 vCPU - 64GB Ram \| 2,6 Ghz per vCPU |
| PC-FVR-R108 | 2   | 8   | VM R1-8 | RAM Optimized \| 2 vCPU - 8GB Ram \| 2,6 Ghz per vCPU |

Verranno invece dismessi

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| PC-FVR-C116 | 16  | 32  | VM C1-16 | CPU Optimized \| 16 vCPU - 32GB Ram \| 3,2 Ghz per vCPU |
| PC-FVR-C136 | 36  | 72  | VM C1-36 | CPU Optimized \| 36 vCPU - 72GB Ram \|  3,2 Ghz per vCPU |
| PC-FVR-C104 | 4   | 8   | VM C1-4 | CPU Optimized \| 4 vCPU - 8GB Ram \|  3,2 Ghz per vCPU |
| PC-FVR-C148 | 48  | 96  | VM C1-48 | CPU Optimized \| 48 vCPU - 96GB Ram \|  3,2 Ghz per vCPU |
| PC-FVR-C108 | 8   | 16  | VM C1-8 | CPU Optimized \| 8 vCPU - 16GB Ram \| 3,2 Ghz per vCPU |
| PC-FVR-E111 | 1   | 1   | VM E1-11 | Economy \| 1 vCPU - 1GB Ram \| 2,1 Ghz per vCPU |
| PC-FVR-E112 | 1   | 2   | VM E1-12 | Economy\| 1 vCPU - 2GB Ram \| 2,1 Ghz per vCPU |
| PC-FVR-E124 | 2   | 4   | VM E1-24 | Economy \| 2 vCPU - 4GB Ram \| 2,1 Ghz per vCPU |
| PC-FVR-E148 | 4   | 8   | VM E1-48 | Economy \| 4 vCPU - 8GB Ram \| 2,1 Ghz per vCPU |
| PC-FVR-N111 | 1   | 1   | VM N1-11 | Network Appliance \| 1 vCPU - 1GB Ram \| 2,6 Ghz per vCPU \| No min 50GB |
| PC-FVR-N112 | 1   | 2   | VM N1-12 | Network Appliance \| 1 vCPU - 2GB Ram \| 2,6 Ghz per vCPU \| No min 50GB |
| PC-FVR-N124 | 2   | 4   | VM N1-24 | Network Appliance  \| 2 vCPU - 4GB Ram \| 2,6 Ghz per vCPU \| No min 50GB |
| PC-FVR-N12C | 2   | 4   | VM N1-2C | Network Appliance \| 2 vCPU - 4GB Ram \| 3,2 Ghz per vCPU CPU INTENSIVE \| No min 50GB |
| PC-FVR-N148 | 4   | 8   | VM N1-48 | Network Appliance  \| 4 vCPU - 8GB Ram \| 2,6 Ghz per vCPU \| No min 50GB |
| PC-FVR-N116 | 8   | 16  | VM N1-816 | Network Appliance \| 8 vCPU - 16GB Ram \| 2,6 Ghz per vCPU \| No min 50GB |
| PC-FVR-S128 | 16  | 128 | VM S1-128 | SAP CPU OPTIMIZED \| 16 vCPU -128GB Ram \| Xeon Platinum 3,2 Ghz per vCPU |
| PC-FVR-S432 | 4   | 32  | VM S1-32 | SAP CPU OPTIMIZED\| 4 vCPU - 32GB Ram \| Xeon Platinum 3,2 Ghz per vCPU |
| PC-FVR-S864 | 8   | 64  | VM S1-64 | SAP CPU OPTIMIZED \| 8 vCPU - 64GB Ram \| Xeon Platinum 3,2 Ghz per vCPU |

Di seguito la tabella dei profili di storage disponibili per le istanze Openstack as a Service:

|     |     |     |
| --- | --- | --- |
| **SKU prodotto** | **Short Description** | **Descrizione** |
| PC-MI1-OBJE | Openstack as a Service - Region MI1 - Scalable Object Storage - 1TB | Scalable Object Storage con protocollo Amazon S3/ Openstack Swift. |
| PC-MI1-LNTS | Openstack as a Service - Region MI1 - Scalable Block Storage - LTS - 1GB | Scalable Long Term Storage - Throughtput Optimized - HDD Based |
| PC-MI1-SPRM | Openstack as a Service - Region MI1 - Scalable Block Storage - SSD - 1GB | Scalable SSD Storage - More IOPS - SSD Based |
| PC-MI1-SSTD | Openstack as a Service - Region MI1 - Scalable Block Storage - Standard - 1GB | Scalable General Purpose  Storage - SSD Based |
| PC-MI1-SSNP | Openstack as a Service - Region MI1 - GB Snapshot / Immagini | External Storage for Snapshot / Immagini custom |