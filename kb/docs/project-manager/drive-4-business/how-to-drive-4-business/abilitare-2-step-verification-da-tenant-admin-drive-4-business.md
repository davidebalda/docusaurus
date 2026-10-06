---
title: "Abilitare 2-Step Verification da Tenant Admin - Drive 4 Business"
---

:::info
La modifica apportata da utenza Admin Tenant interessa solo gli utenti che appartengono al tenant.
:::

## Abilitare 2-Step Verification da Tenant Admin {#abilitare-2-step-verification-da-tenant-admin}

Per abilitare il 2-Step Verification è sufficiente seguire i seguenti passaggi:

1. Effettua il **Login** come **Admin Tenant** al portale web di Drive4Business ( [www.d4b.cloudfire.it](http://www.d4b.cloudfire.it) )  
![](/kb-assets/75110012ec-d4b-login-1.png)
2. Naviga nel menù **Group Policy > Account & Login > User Account > 2-Step Verification**  
![](/kb-assets/7afdc4d92a-d4b-2fa-1.png)
3. Abilita le voci che vuoi abilitare per l’attivazione dell’autenticazione a due fattori.

## Ruolo {#ruolo}

  
Il **Ruolo** è una funzione per tutti gli utenti ai quali si vuole applicare a un ruolo specifico.

###    {#section}
Assegna un Ruolo

Per assegnare un ruolo ad un utente è sufficiente seguire i seguenti passaggi:

1. Effettua il **Login** come **Admin Tenant** al portale web di Drive4Business ( [www.d4b.cloudfire.it](http://www.d4b.cloudfire.it) )  
![](/kb-assets/75110012ec-d4b-login-1.png)
2. Naviga nel menù **User Account > Role Manager > Create new Role > Policies tab** e spunta la voce **Enforce 2-Step Verification on users**  
![](/kb-assets/741eb48e33-d4b-2fa-2.png)
3. Premi su **Apply** per applicare le modifiche apportate.

### Come utilizzare il 2-Step Verification {#come-utilizzare-il-2-step-verification}

Se il 2-Step Verification è stato **abilitato, ma non forzato** per l’utente, una volta che questo effettua l’accesso può abilitarlo.

Per abilitarlo basta seguire i seguenti passaggi:

1. Effettua il **Login** come **User** al portale web di Drive4Business ( [www.d4b.cloudfire.it](http://www.d4b.cloudfire.it) )
2. Vai al menù utente posto in alto a destra nella pagina e premi la voce **2-Step Verification**  
![](/kb-assets/c80c2ad3f6-d4b-2fa-3.png)
3. Abilita la voce **Enable Two-Step Verification** e poi premi su **Apply**  
![](/kb-assets/c4ca4a2ca2-d4b-2fa-4.png)

### Passaggi da seguire una volta attivato {#passaggi-da-seguire-una-volta-attivato}

Una volta abilitato, segui questi passaggi:

1. **Dall’app Authenticator**. Scannerizza il QRCode o utilizza la chiave segreta
2. **Verifica il Codice di Sicurezza**. Inserisci il codice di sicurezza ricevuto dall’authenticator
3. **Email di Backup**. Specifica una casella email che verrà usata quando l’authenticator non è disponibile o non funziona.
4. Facoltativo. Abilita i Client Desktop o le Mobile App del Two-Step Verification

:::note
Quando il 2-Step Verification è **Abilitato dall’Utente**, dopo che l’utente inserisce la password per autenticarsi, il sistema richiederà un Codice di Sicurezza.

[!NOTE]
Quando il 2-Step Verification è **Forzato dall’Amministratore Tenant**, e l’utente non l’ha configurato dal suo portale, la configurazione verrà richiesta non appena l’utente esegue l’accesso sul portale web ( [www.d4b.cloudfire.it](http://www.d4b.cloudfire.it) )
:::