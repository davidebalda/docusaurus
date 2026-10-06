## Introduzione

L’infrastruttura Scalable Storage che trovate sulla piattaforma offre più Tier con performance differenti e due modalità di accesso.

La modalità **Scalable Block Storage** è pensata per essere utilizzate come disco a blocchi per qualsiasi istanza Public Cloud. I Tier attualmente disponibili sono i seguenti:

- SSD - Ad oggi il profilo più veloce con le ultime tecnologie SSD e replica dati in 3 Availability Zone ( [Più informazioni](../primi-passi-openstack-as-a-service/flavor-e-storage-disponibili-in-openstack-as-a-service-v2.md) )
- Standard- Scalable Standard General Purpose Storage -
- LTS - Scalable Long Term Storage - Throughtput Optimized - HDD Based

La modalità **Scalable Object Storage** è pensata per offrire la possibilità di salvare i file in un ambiente cloud sicuro, scalabile ad accessibile attraverso un unico endpoint con protocollo S3.

# Scalable Block Storage Benchmark

## Storage Standard Benchmark

|     |     |
| --- | --- |
| **Size \[GB\]** | **STD \[iops\]** |
| **fino a 99** | 1000 |
| **da 100 a 149** | 1500 |
| **da 150 a 199** | 2000 |
| **da 200 a 249** | 2500 |
| **da 250 a 299** | 3000 |
| **da 300 a 349** | 3500 |
| **da 350 a 399** | 4000 |
| **da 400 a 449** | 4500 |
| **da 450 a 499** | 5000 |
| **da 500 a 749** | 5500 |
| **da 750 a 999** | 8000 |
| **\>1000** | 10000 |

###### I Benchmark sono sono stati eseguiti tramite [Fio Tool](https://fio.readthedocs.io/en/latest/fio_doc.html) con un una base **block size** di **4kB** e **iodepth** **128**.  
La voce **iops** indica il numero massimo di operazioni simultanee.

## Storage SSD Benchmark

|     |     |
| --- | --- |
| **Size \[GB\]** | **SSD \[iops\]** |
| **fino a 99** | 1950 |
| **da 100 a 149** | 2700 |
| **da 150 a 199** | 3450 |
| **da 200 a 249** | 4200 |
| **da 250 a 299** | 4950 |
| **da 300 a 349** | 5700 |
| **da 350 a 399** | 6450 |
| **da 400 a 449** | 7200 |
| **da 450 a 499** | 7950 |
| **da 500 a 749** | 8700 |
| **da 750 a 999** | 12450 |
| **\>1000** | 15000 |

###### I Benchmark sono sono stati eseguiti tramite [Fio Tool](https://fio.readthedocs.io/en/latest/fio_doc.html) con un una base **block size** di **4kB** e **iodepth** **128**.  
La voce **iops** indica il numero massimo di operazioni simultanee.

## Storage LTS Benchmark

Lo storage **LTS** parte da un throughput di **60MB/s** e aumenta questo performance counter in modo statico "a fasce" all'aumentare dello spazio.

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| **Type** | **50GB \[MB/s\]** | **100GB \[MB/s\]** | **500GB \[MB/s\]** | **1TB \[MB/s\]** | **2TB \[MB/s\]** | **5TB \[MB/s\]** |
| **LTS** | 60  | 60  | 60  | 60  | 100 | 250 |

# Scalable Object Storage Benchmark

### Bucket S3 Storage

Per questa modalità al momento è disponibile un unico tier senza alcun limite di banda, con possibilità della funzionalità Object Locking ( [Più informazioni](https://www.cloudfire.it/solutions/object-storage) )

Il numero di operazioni massime per Indirizzo IP client sono le seguenti:

|     |     |
| --- | --- |
| **Operations** | **Max 10 secondi** |
| **PUT/COPY/POST** | 5000 |
| GET | 50000 |
| DELETE | 500 |

Al raggiungimento o superamento del limite comparirà l’errore “*Error 429 - Too Many Request*”.  
Basterà attendere un breve periodo per riprendere le operazioni.