---
title: "Security"
---

## Introduzione {#introduzione}

Questo sotto-menù permette la gestione delle restrizioni relative a numeri di telefono, Reti IP oppure utenti.

## Descrizione delle sezioni {#descrizione-delle-sezioni}

### Access Restriction {#access-restriction}

In questa sezione è possibile gestire le ACL per negare un accesso o una registrazione SIP proveniente da altre reti.

Cliccando su ![](/kb-assets/95d85bd0be-image2019-4-4-14-47-53.png)

è possibile creare una nuova regola,  

![](/kb-assets/74d67bd488-image2019-4-4-14-46-33.png)

- **IP:**  Indirizzo IP della rete o dell'Host da negare.
- **Mask Bit:** indicare la subnet della rete (in caso di singolo host mantenere il valore 32).
- **Description:** breve descrizione della regola.
- **Restriction Type:** indicare se la restrizione è da applicare all'accesso web, alla registrazione oppure ad entrambi.
- **Restriction Status:** Abilita o disabilita la regola.

### Blacklist Number {#blacklist-number}

In questa sezione è possibile indicare i numeri verso cui le chiamate in uscita sono inibite oppure vengono rifiutate in caso di chiamate in entrata. Cliccando su ![](/kb-assets/d29ef73777-image2019-4-10-15-18-29.png)

 vi si apre il form da compilare.

![](/kb-assets/5d8ad3dfb7-image2019-4-10-15-20-57.png)

- **Number:** Inserire numerazione telefonica, se la numerazione è italiana inserirla **SENZA** il prefisso internazionale. 
- **IN:** scegliere IN se volete bloccare la numerazione in ingresso, OUT se la volete bloccare in uscita, BOTH se la volete bloccare in entrambe le direzioni
- **Reason:** spazio in cui inserire una breve descrizione della regola.

### Whitelist Number {#whitelist-number}

Vedi Blacklist Number per la configurazione, serve a indicare i numeri da aggiungere alla whitelist. In caso di conflitto prevarrà la whitelist.

### Locked User {#locked-user}

Mostra le extension bloccate a causa dell’ infrazione delle regole di registrazione. Previene la possibilità che un client compromesso generi traffico fraudolento.

  

  

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Descrizione delle sezioni](#descrizione-delle-sezioni)
-   [Access Restriction](#access-restriction)
-   [Blacklist Number](#blacklist-number)
-   [Whitelist Number](#whitelist-number)
-   [Locked User](#locked-user)
* * *
**Articoli collegati**


- Page:
[Fax to Mail & Mail to Fax](../../../internet-e-fonia/fax-to-mail-and-mail-to-fax.md)
- Page:
[Portale Extension - Opzioni e Funzionalità](https://cloudfireit.atlassian.net/wiki/spaces/KB/pages/1966256717/Portale+Extension+-+Opzioni+e+Funzionalit)
- Page:
[Dashboard](dashboard.md)
- Page:
[Security](security.md)
- Page:
[Outgoing Rules](call-routing/outgoing-rules.md)
:::