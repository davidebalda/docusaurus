---
title: "Autenticazione multifattore (MFA)"
---

:::warning
Dal **31/03/2024** è obbligatoria l’attivazione dell’autenticazione multifattore per tutti gli utenti Cortex.
:::

Questa pagina spiega come abilitare la MFA o Autenticazione a più fattori.

## Reimpostare autenticazione multifattore (MFA)

:::note
L'autenticazione a multifattore (MFA) ti consente di aumentare il livello di sicurezza del tuo utente, richiedendo l'inserimento di un codice per effettuare l'accesso al portale. In questa sezione puoi gestire la configurazione del MFA.
:::

Per abilitare l’autenticazione multifattore puoi seguire i seguenti passaggi:

1. Effettua il **login** su Cortex, verrai indirizzato su **Account Manager**
2. Seleziona la voce **Utenti** dal menu di navigazione laterale
3. Naviga fino alla sezione **Autenticazione Multifattore (MFA)**
4. Premi il bottone **Reimposta MFA** posto in basso a destra nella card;
5. Si aprirà una finestra di dialogo che chiederà di confermare la scelta, premi **Reimposta**

![Screenshot 2024-03-29 at 16.09.35.png](/kb-assets/b65827e083-screenshot-2024-03-29-at-16-09-35.png)

:::info
Reimpostando l’autenticazione multifattore, al login successivo all’abilitazione, all’utente verrà richiesto di completare la configurazione per l'invio del codice di accesso.
:::

## Configura l’autenticazione multifattore - Notifiche OTP

La prima volta che effettui il login al portale ti verrà richiesto di configurare l’autenticazione tramite notifiche OTP.

Per configurare le notifiche OTP per l’autenticazione a più fattori puoi seguire i seguenti passaggi:

1. Seleziona la voce **OTP** come modalità di MFA

Per utilizzare le password monouso (OTP) come fattore di autenticazione, dovrai utilizzare un'app Authenticator come:

- Authy ([Google Play](https://play.google.com/store/apps/details?id=com.authy.authy)/[App Store](https://itunes.apple.com/us/app/authy/id494168017)).
- Autenticatore Google ([Google Play](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2)/[App Store](https://itunes.apple.com/us/app/google-authenticator/id388497605)).
- Auth0 Guardiano ([Google Play](https://play.google.com/store/apps/details?id=com.auth0.guardian)/[App Store](https://itunes.apple.com/us/app/auth0-guardian/id1093447833)).
- Autenticatore Microsoft ([Google Play](https://play.google.com/store/apps/details?id=com.azure.authenticator)/[App Store](https://itunes.apple.com/us/app/microsoft-authenticator/id983156458))

Dovrai infatti avere un' app OTP Authenticator installata sul tuo o più dispositivi mobili.

![](/kb-assets/d757770930-image-20220923-134615.png)

Al momento della registrazione, possono scansionare un codice e configurare l'app, sulla quale inizierà a generare codici monouso. Successivamente, quando accede all'app, l'utente può semplicemente controllare l'app di autenticazione per il codice monouso corrente:

![](/kb-assets/139b737041-image-20220923-134703.png)

Dovrai quindi inserire il codice alla richiesta:

![](/kb-assets/d718de2ecd-image-20220923-134727.png)