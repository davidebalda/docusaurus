---
title: "Criteri di sicurezza e gestione degli accessi su Cortex"
---

Al fine di offrire un accesso sicuro per ogni utente e per i propri dati, in linea con le linee guida e [certificazioni ISO](https://www.cloudfire.it/competency-security/certifications-qualifications) ottenute da CloudFire, su Cortex sono implementati i seguenti criteri di sicurezza.

## Password Policy

Per rendere le password (degli utenti?) più robuste e difficili da decifrare, sono stati implementati i seguenti requisiti di complessità:

- Lunghezza minima 8 caratteri
- Utilizzo di almeno 1 carattere speciale
- Utilizzo di almeno 1 lettera maiuscola
- Utilizzo di almeno 1 lettera minuscola
- Utilizzo di almeno 1 numero

## MFA Obbligatorio

Oltre all’utilizzo della password, abbiamo reso obbligatoria l’attivazione del MFA.

Segui la nostra [guida](https://cloudfireit.atlassian.net/wiki/x/YgCJdQ) per la prima configurazione.

:::tip
La combinazione di una password complessa e l’utilizzo del MFA garantiscono una sicurezza completa per il tuo Account.
:::

## Password Rotation

Per rafforzare la sicurezza nel tempo, la password di accesso a Cortex ha **validità 90 giorni**.

Al raggiungimento del termine sarà necessario aggiornare la propria password, creandone una diversa dalle 24 precedenti impostate. Un controllo durante il reset ti informerà se la password scelta è già stata utilizzata in passato, prevenendo il rischio di riutilizzare password vulnerabili

## Protezione Brute Force

Per prevenire l’accesso agli account attraverso attacchi *brute force*, il sistema **limita** automaticamente i **tentativi di accesso falliti** consecutivi a **5 per medesimo indirizzo IP di origine**.

Superato questo limite il tuo account verrà bloccato temporaneamente e riceverai una notifica via email dall’indirizzo [hello@mycortex.io](mailto:hello@mycortex.io) con le relative istruzioni per sbloccare l’utente stesso.

## Limitazione IP sospetti

Per prevenire attacchi automatizzati ad alta velocità, che prendono di mira più account contemporaneamente (*credential stuffing*), il sistema **monitora il traffico in entrata** e **blocca automaticamente** gli i**ndirizzi IP che tentano troppi accessi o iscrizioni a Cortex in un breve lasso di tempo**.

## Rilevamento password violate

Per tutelare i tuoi dati in caso di violazioni di altri siti web o servizi, il sistema di autenticazione di Cortex è in grado di rilevare se le tue credenziali sono state compromesse e sono presenti in database di password rubate. In questo caso, il tuo accesso a Cortex verrà disabilitato e riceverai una notifica via email con istruzioni per reimpostare la tua password e ripristinare la protezione del tuo account.

:::info
In caso di problemi o dubbi, ti invitiamo ad aprire un [**Case**](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/1966244909) al nostro supporto.
:::