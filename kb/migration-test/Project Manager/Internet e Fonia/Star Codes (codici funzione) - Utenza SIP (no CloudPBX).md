- [Introduzione](#introduzione)
- [Inoltro/Deviazione](#inoltrodeviazione)
-   [Deviazione incondizionata](#deviazione-incondizionata)
-   [Deviazione in caso di non risposta](#deviazione-in-caso-di-non-risposta)
-   [Deviazione in caso di occupato](#deviazione-in-caso-di-occupato)
-   [Deviazione in caso di utente non registrato](#deviazione-in-caso-di-utente-non-registrato)
-   [Call Forking / Follow me](#call-forking-follow-me)
-   [Verificare o cancellare i vari inoltri / deviazioni](#verificare-o-cancellare-i-vari-inoltri-deviazioni)
- [Rifiutare le chiamate](#rifiutare-le-chiamate)
-   [Do not Disturb DND](#do-not-disturb-dnd)
-   [Rifiutare le chiamate anonime](#rifiutare-le-chiamate-anonime)

## Introduzione

Di seguito i codici funzioni utilizzabili dal tastierino telefonico per poter applicare deviazioni, pickup e conference.

## Inoltro/Deviazione

### Deviazione incondizionata

|     |     |     |
| --- | --- | --- |
| Azione | Codice | Note |
| Attivazione | ```<br>*21(*)<numero di telefono><br>``` | il numero di telefono deve essere inserito senza il "39" iniziale se si tratta di un numero nazionale. |
| Deviazione verso VoiceMail Box | ```<br>*28<br>``` |     |
| Disattivazione | ```<br>*021<br>``` |     |
| Verifica Status del servizio | ```<br>**21<br>``` |     |

  

### Deviazione in caso di non risposta

questa feature si attiva se l'utente non risponde alla chiamata dopo 14 secondi (circa 3 squilli)

|     |     |     |
| --- | --- | --- |
| Azione | Codice | Note |
| Attivazione | ```<br>*61(*)<numero di telefono><br>``` | il numero di telefono deve essere inserito senza il "39" iniziale se si tratta di un numero nazionale. |
| Deviazione verso VoiceMail Box | ```<br>*68<br>``` |     |
| Disattivazione | ```<br>*061<br>``` |     |
| Verifica Status del servizio | ```<br>**61<br>``` |     |

  

### Deviazione in caso di occupato

|     |     |     |
| --- | --- | --- |
| Azione | Codice | Note |
| Attivazione | ```<br>*67(*)<numero di telefono><br>``` | il numero di telefono deve essere inserito senza il "39" iniziale se si tratta di un numero nazionale. |
| Deviazione verso VoiceMail Box | ```<br>*691<br>``` |     |
| Disattivazione | ```<br>*067<br>``` |     |
| Verifica Status del servizio | ```<br>**67<br>``` |     |

  

### Deviazione in caso di utente non registrato

|     |     |     |
| --- | --- | --- |
| Azione | Codice | Note |
| Attivazione | ```<br>*22(*)<numero di telefono><br>``` | il numero di telefono deve essere inserito senza il "39" iniziale se si tratta di un numero nazionale. |
| Deviazione verso VoiceMail Box | ```<br>*692<br>``` |     |
| Disattivazione | ```<br>*022<br>``` |     |
| Verifica Status del servizio | ```<br>**22<br>``` |     |

### Call Forking / Follow me

|     |     |     |
| --- | --- | --- |
| Azione | Codice | Note |
| Attivazione | ```<br>*481(*)<numero di telefono><br>``` | il numero di telefono deve essere inserito senza il "39" iniziale se si tratta di un numero nazionale. |
| Disattivazione | ```<br>*0481<br>``` |     |
| Verifica Status del servizio | ```<br>**481<br>``` |     |

### Verificare o cancellare i vari inoltri / deviazioni

|     |     |     |
| --- | --- | --- |
| Azione | Codice | Note |
| Cancella tutto | ```<br>*00<br>``` | questo comando elimina tutti gli inoltri/deviazioni attivati con "#\*". |
| Verifica di quante<br><br>deviazioni / inoltri sono attivi | ```<br>**481<br>``` |     |

## Rifiutare le chiamate

### Do not Disturb DND

Se attivato, il chiamante sentirà un messaggio vocale che la persona contattata al momento non vuole essere disturbata.

|     |     |     |
| --- | --- | --- |
| Azione | Codice | Note |
| Attivazione | ```<br>*26<br>``` |     |
| Disattivazione | ```<br>*026<br>``` |     |
| Verifica Status del servizio | ```<br>**26<br>``` |     |

### Rifiutare le chiamate anonime

Se attivato e il chiamante si presenta con numerazione anonima, la chiamata verrà rifiutata e il chiamante sentirà un messaggio vocale che la persona chiamata non accetta chiamate provenienti da numerazione anonima.

|     |     |     |
| --- | --- | --- |
| Azione | Codice | Note |
| Attivazione | ```<br>*99<br>``` |     |
| Disattivazione | ```<br>*099<br>``` |     |
| Verifica Status del servizio | ```<br>**99<br>``` |     |