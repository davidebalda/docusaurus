---
title: "3CX - Aggiornamento alla v20"
---

#### Prerequisiti {#prerequisiti}

- Assicurarsi di avere almeno un utente con ruolo “Proprietario di sistema”;
- Assicurarsi di avere il profilo dell’App adatto;
- Assicurarsi di avere una licenza valida.

:::warning
**Prima di procedere con l’aggiornamento, assicurarsi di avere un backup completo del centralino.**

[!INFO]
Con la v20 3CX **ha** **dismesso** il supporto delle registrazioni **STUN** dei telefoni.  
Pertanto, in caso di aggiornamento, consigliamo di verificare la presenza di un **SBC** o un **telefono router** nella propria infrastruttura per riuscire a registrare i dispositivi.
:::

#### Procedimento {#procedimento}

- Accedere a Cortex e sotto il servizio *Unified Communication* → *3CX* verificare di avere un profilo dell’app v20.  
**Nel caso fosse un profilo v18, bisognerà modificarlo scegliendone uno adatto v20.** [Qui la guida per l’accesso ai dettagli e la modifica](app-3cx.md#accedi-al-dettaglio-di-un-app-3cx).
- Effettuare quindi l’accesso al centralino e dalla voce “Aggiornamenti” in alto a destra selezionare “v20 - Debian 12”;
- Nella schermata che si aprirà, procedere con l’aggiornamento:

![image-20240514-093705.png](/kb-assets/3190fd5b12-image-20240514-093705.png)

3CX provvederà in autonomia a tutto il procedimento, inviando un’email al proprietario di sistema una volta conclusa l’operazione.

:::info
L’aggiornamento alla v20 comporta anche un aggiornamento del sistema operativo della macchina Linux a **Debian 12**.

[!INFO]
L’aggiornamento richiede un fermo e un riavvio dell’intero sistema, per un periodo variabile (dai 5 ai 20 minuti).
:::