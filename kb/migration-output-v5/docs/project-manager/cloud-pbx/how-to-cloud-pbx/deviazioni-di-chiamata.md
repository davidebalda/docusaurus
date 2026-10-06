---
title: "Deviazioni di chiamata"
---

## Introduzione {#introduzione}

In questa guida vi illustreremo come effettuare le deviazioni di chiamata, sia a livello di interno che di DID.

### Deviazione di chiamata destinata ad un'extension specifica {#deviazione-di-chiamata-destinata-ad-un-extension-specifica}

Il cloud PBX prevede diverse modalità di deviazione di chiamata per quanto riguarda gli interni, e di seguito vi esporremo tutte le varie casistiche.

#### Universal Forward {#universal-forward}

L'**Universal** **Forward** riguarda la deviazione di qualsiasi chiamata destinata ad un extension.

Per poter configurare questa opzione eseguite questi passaggi:

- Accedete al **[Portale Extension](/project-manager/cloud-pbx/how-to-cloud-pbx/portale-extension)** dell'extension desiderata.
- Spostatevi nel menù **Extension Settings.**
- Modificate il valore dal campo **Universal** **Forward Type**, selezionando la tipologia di destinazione voluta.

          ![](/kb-assets/ca91f0aa1e-image2019-8-22-12-41-58.png)

Modificate il valore **Universal** **Forward**, inserendo la numerazione verso cui effettuare la deviazione, compatibile con il tipo di destinazione selezionata nel menù precedente.

#### Shift Forward {#shift-forward}

Lo **S****hift Forward** riguarda la deviazione delle chiamate, destinate ad un extension, che arrivano al di fuori della finestra temporale impostata nello **Shift** (info maggiori → **[Shift (2) (2)](portale-tenant-cloud-pbx/timing/shift-2-2.md)**  e **[Extension (2) (2)](portale-tenant-cloud-pbx/service-2-2/extension-2-2.md)**).

Per poter configurare questa opzione eseguite questi passaggi:

- Accedete al **[Portale Extension](/project-manager/cloud-pbx/how-to-cloud-pbx/portale-extension)** dell'extension desiderata.
- Spostatevi nel menù **Extension Settings.**
- Modificate il valore dal campo **Shift Forward Type**, selezionando la tipologia di destinazione voluta.

          ![](/kb-assets/ca91f0aa1e-image2019-8-22-12-41-58.png)

- Modificate il valore **Shift Forward**, inserendo la numerazione verso cui effettuare la deviazione, compatibile con il tipo di destinazione selezionata nel menù precedente.

#### Busy / No Answer / Unavailable Forward {#busy-no-answer-unavailable-forward}

Valgono le stesse indicazioni dello **Shift Forward** anche per gli altri seguenti casi:

- **Busy Forward:** questa è la deviazione di chiamata nel caso in cui l'extension risulti occupata.
- **No Answer Forward:** questa è la deviazione di chiamata in caso in cui l'extension non risponda prima dello scadere del **Ring Timeout** (dettagli sul Ring Timeout: **[Extension](portale-tenant-cloud-pbx/service-2-2/extension-2-2.md)** o **[Extension Settings](portale-extension/portale-extension-extension-settings.md)**).
- **Unavailable Forward:** questa è la deviazione di chiamata nel caso in cui l'extension risulti non disponibile (generalmente quando il telefono non risulta registrato).

#### Selective Forward {#selective-forward}

Il **Selective Forward** è quella deviazione che viene eseguita in base al numero del chiamante, infatti è possibile fare in modo che tutte le chiamate provenienti da determinati numeri telefonici vengano deviate verso un'altra destinazione.

Per poter configurare questa opzione eseguite questi passaggi:

- Accedete al **[Portale Extension](/project-manager/cloud-pbx/how-to-cloud-pbx/portale-extension)** dell'extension desiderata.
- Spostatevi nel menù **Extension Settings.**
- Nel campo **Selective Forward** potete aggiungere una numerazione a vostro piacimento, che sia interna o esterna.  

- Modificate il valore dal campo **Selective Forwar** **Type**, selezionando la tipologia di destinazione voluta  
![](/kb-assets/ca91f0aa1e-image2019-8-22-12-41-58.png)

#### Time Based Forward {#time-based-forward}

Il **Time Based Forward** riguarda la deviazione delle chiamate, che arrivano in una particolare finestra temporale.

Per poter configurare questa opzione eseguite questi passaggi:

- Accedete al **[Portale Extension](/project-manager/cloud-pbx/how-to-cloud-pbx/portale-extension)** dell'extension desiderata.
- Spostatevi nel menù **Extension Settings.**
- Modificate il valore dal campo **Time Based** **Forward Type**, selezionando la tipologia di destinazione voluta.

          ![](/kb-assets/ca91f0aa1e-image2019-8-22-12-41-58.png)

- Modificate il valore **Time Based Forward**, inserendo la numerazione verso cui effettuare la deviazione, compatibile con il tipo di destinazione selezionata nel menù precedente.
- Nei campi **Time From** e **To** specificate la fascia oraria in cui volete che la deviazione sia attiva:

## Deviazioni di chiamata destinate ad un DID specifico {#deviazioni-di-chiamata-destinate-ad-un-did-specifico}

Se la vostra intenzione invece è quella di deviare tutte le chiamate destinate ad una vostra particolare **Numerazione Telefonica** dovete procedere come segue.

- Accedete al **Portale Tenant** e spostatevi nel sotto menù **Call Routing → DID Routing**  
![](/kb-assets/7b7d7c6b90-image2019-8-23-17-3-30.png)
- Entrate nella schermata di modifica delle impostazioni della numerazione desiderata cliccando sul pulsante **EDIT**
- A questo punto dovete verificare se sono state configurate delle **Inbound Rules** a questa numerazione.Se non ve ne sono, vedrete la tabella sottostante vuota come in questo caso:![](/kb-assets/800f781771-image2019-8-23-17-8-35.png)
Per applicare una deviazione a questa numerazione vi basterà modificare i campi come segue:
-   **Default Destination:** selezionate la tipologia di destinazione voluta.          ![](/kb-assets/4c87b29de1-image2019-8-23-17-10-11.png)
-   **Default Extension:** inserite la numerazione verso cui effettuare la deviazione, compatibile con il tipo di destinazione selezionata nel menù precedente.
-   **Header Type:** lasciate pure il valore su **To.  
  **
- Nel caso in cui invece la **Numerazine Telefonica** presentasse delle **Inbound Rules** (come nell'immagine sottostante)![](/kb-assets/5fcc74cf1a-image2019-8-23-17-31-7.png)
dovete procedere come segue:
1.   Spostatevi nel sotto menù **Timing → Time Condition**
2.   Cliccate su **ADD TIME CONDITION** e compilate i campi in modo da ottenere la finestra temporale desiderata per la deviazione di chiamata.
3.   Tornate al menù **Routing → DID Routing** ed rientrate nelle impostazioni della numerazione desiderata.
4.   Cliccate su **ADD INBOUND RULE** e aggiungete la regola appena creata specificando la destinazione della deviazione e cliccate su **CREATE**
5.   Tornando alla schermata precedente dovete trascinare la regola appena aggiunta in alto in tabella, così facendo, questa regola avrà priorità sulle altre, così facendo avrete impostato la deviazione.

## Deviazione in caso di No Line {#deviazione-in-caso-di-no-line}

Esiste infine, un ultima deviazione che si attiva nel caso di **No Line.** Per **No Line** viene inteso quel momento in cui nessun telefono è registrato per qualche tipo di problema sulla rete.

In questo caso nessuna delle extension risulta registrata e quindi il CloudPBX non saprebbe dove indirizzare le chiamate che gli arrivano, per cui è possibile configurare questa opzione per non perdere le varie chiamate.

Per configurare questa opzione spostarsi nel menù **Call Routing → No Line Forward Settings.**

Selezionare la destination voluta (ovviamente le destination sono solo **Extenal o Voice Mail,** in quanto nessun altra opzione sarebbe valida). 

Inserire la numerazione esterna in caso si abbia selezionato **External.**

Inserire l'extension desiderata in caso si desideri che le chiamate vengano deviate verso una particolare **Voicemail.**

:::note
**Sommario**



- [Introduzione](#introduzione)
-   [Deviazione di chiamata destinata ad un'extension specifica](#deviazione-di-chiamata-destinata-ad-un-extension-specifica)
  
  -   [Universal Forward](#universal-forward)
  
  -   [Shift Forward](#shift-forward)
  
  -   [Busy / No Answer / Unavailable Forward](#busy-no-answer-unavailable-forward)
  
  -   [Selective Forward](#selective-forward)
  
  -   [Time Based Forward](#time-based-forward)
- [Deviazioni di chiamata destinate ad un DID specifico](#deviazioni-di-chiamata-destinate-ad-un-did-specifico)
- [Deviazione in caso di No Line](#deviazione-in-caso-di-no-line)

* * *
**Articoli collegati**



- Page:
[Estendere volume Guest OS (Linux) senza riavviare](../../openstack-as-a-service/how-to-openstack-as-a-service/estendere-volume-guest-os-linux-senza-riavviare.md)
- Page:
[Chiamate esterne da Ring Group o IVR non funzionanti](../troubleshoot-cloud-pbx/chiamate-esterne-da-ring-group-o-ivr-non-funzionanti.md)
- Page:
[Impossibile chiamare o ricevere chiamate](../troubleshoot-cloud-pbx/impossibile-chiamare-o-ricevere-chiamate.md)
- Page:
[Portale Extension - Profile](portale-extension/portale-extension-profile.md)
- Page:
[Portale Extension - Voicemail](portale-extension/portale-extension-voicemail.md)
:::