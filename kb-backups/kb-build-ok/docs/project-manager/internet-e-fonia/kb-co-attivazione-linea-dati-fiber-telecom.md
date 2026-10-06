---
title: "KB ΓÇô Attivazione linea dati Fiber Telecom"
---

## **1\. Recupero dei dati dal portale Fiber Telecom**

1. Collegarsi al sito Fiber Telecom:
-   [https://www.fibertelecom.it/store/](https://www.fibertelecom.it/store/)
2. Espandere la sezione **Ordine → Consegnato**.
3. Recuperare i seguenti parametri tecnici:
-   **Service VLAN**
-   **Customer VLAN**

Annotare i valori, saranno necessari durante la configurazione sul router.

* * *

## **2\. Configurazione del router di accesso**

1. Accedere via **SSH** al router della region corrispondente.
2. Creare l'interfaccia sub‑if per la doppia VLAN (QinQ):
-   La nomenclatura dell'interfaccia deve seguire il formato:  
  **0/1/0.XXXXYYYY**Dove:
-   **XXXX** = Service VLAN
-   **YYYY** = Customer VLAN

### **Esempio di configurazione**

Supponendo:

- Service VLAN: `3546`
- Customer VLAN: `3999`

Configurazione:

```
interface TenGigabitEthernet0/1/0.35463999
 description CLOUDFIRESRL20250709155648 Roberto Bondavalli - Casa
 encapsulation dot1Q 3546 second-dot1q 3999
 pppoe enable group global

```

> Nota: verificare sempre che il gruppo PPPoE corretto sia **global**, salvo esigenze specifiche della region.

* * *

## **3Creazione utente RADIUS**

1. Accedere al server RADIUS:
-   [**radius01.radius.mi1.prod.cloudfire.it**](http://radius01.radius.mi1.prod.cloudfire.it)
-   Autenticarsi con le **credenziali 1 PASS**.
2. Navigare nel menu: **MANAGEMENT → USER → New User**
3. Compilare il nuovo utente:
-   Gruppo: **DEFAULT**
-   Username nel formato: **IDLINEA\_NOME**  
  *(Esempio: 20250709155648\_RBONDAVALLI)*
4. Accedere alla tab **Attributes**.
5. Selezionare **Insert Custom Attribute**.
6. Inserire il seguente attributo RADIUS:
-   **Framed-IP-Address :=**   
  *(l’IP statico deve essere recuperato dall’IPAM)*

## **4\. . Creazione utente RADIUS**

1. Accedere al server RADIUS:
-   [**radius01.radius.mi1.prod.cloudfire.it**](http://radius01.radius.mi1.prod.cloudfire.it)
-   Autenticarsi con le **credenziali 1 PASS**.
2. Navigare nel menu: **MANAGEMENT → USER → New User**
3. Compilare il nuovo utente:
-   Gruppo: **DEFAULT**
-   Username nel formato: **IDLINEA\_NOME**  
  *(Esempio: 20250709155648\_RBONDAVALLI)*
4. Accedere al**5**a tab **Attributes**.
5. Selezionare **Insert Custom Attribute**.
6. Inserire il seguente attributo RADIUS:
-   **Framed-IP-Address :=**   
  *(l’IP statico deve essere recuperato dall’IPAM)*

## **4\. Verificeazione**

1. Verificare che l'interfaccia sia **UP**:
```
show interface TenGigabitEthernet0/1/0.XXXXYYYY
```
2. Controllare la sessione PPPoE:
```
show pppoe sessions
```
3. In caso di problemi, verificare:
-   Tag VLAN corretti
-   Inserimento corretto di Service VLAN e Customer VLAN
-   Presenza della configurazione PPPoE

* * *

## **5\. Note aggiuntive**

file con vlan condiviso

[https://docs.google.com/spreadsheets/d/1gCsgpQ2YS4HxvNjc5esN6PxICtdrpQCeXtQBGZ\_F8bo/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1gCsgpQ2YS4HxvNjc5esN6PxICtdrpQCeXtQBGZ_F8bo/edit?gid=0#gid=0)

- Alcune attivazioni possono richiedere qualche minuto prima che la sessione PPPoE salga.
- Assicurarsi che non esistano altre interfacce con la stessa coppia di VLAN.