---
title: "Veeam - Reconfigure"
---

## Modificare le credenziali d’accesso {#modificare-le-credenziali-d-accesso}

1. Accedere a Cortex e recarsi sulla pagina del servizio Veeam Cloud Platform
2. Selezionare “Reimposta password” dal riquadro Veeam Cloud Connect e configurare una nuova password (consigliamo una password complessa: minimo 10 caratteri, maiuscole, minuscole, cifre e caratteri speciali)

![](/kb-assets/24e5790282-immagine-20221118-171503.png)

3\. Nel riquadro Veeam Cloud Connect sono inoltre presenti il nuovo gateway URL ([vcg.cloudfire.it](http://vcg.cloudfire.it)) e il nuovo username (… \_1), che serviranno nei passaggi successivi

## Modificare il Service Provider {#modificare-il-service-provider}

1. Collegarsi alla console Veeam Backup and Replication
2. Sezione **Backup Infrastructure** → **Add Provider**![](/kb-assets/51783f637c-image-20221118-163339.png)
3. Configurare DNS name [**vcg.cloudfire.it**](http://vcg.cloudfire.it)  
![](/kb-assets/ad4bb496d2-1.png)
  
![](/kb-assets/49e227a265-image-20221118-163458.png)

4\. Creare / Selezionare le nuove credenziali ( **username nuovo finisce con \_1** )  

![](/kb-assets/dd1cdd332c-2.png)

![](/kb-assets/a9d5012c96-3.png)

5\. Verificare che il Repository sia **Veeam Cloud Platform - Mi1**  

![](/kb-assets/24b88f1196-image-20221118-163713.png)

![](/kb-assets/7fab4ca100-image-20221118-163826.png)

![](/kb-assets/fe1f1ec502-image-20221118-163856.png)

![](/kb-assets/fd801f3994-4.png)

## Modificare Job di Backup Copy {#modificare-job-di-backup-copy}

1. Sezione **Home** → **Jobs** → **Backup Copy**  
![](/kb-assets/a2cd6a0a9e-image-20221118-164036.png)
2. Selezionare un job per volta quindi **Disable**![](/kb-assets/6b6c880792-image-20221118-164539.png)
3. Clonare il primo job **Selezionando il job** → **Clone**![](/kb-assets/7f7281f12a-image-20221118-164622.png)
4. Editare il job **CLONATO** cliccando **Tasto DESTRO** → **Edit** : Portarsi alla voce **Target** quindi modificare dal menu a tendina il **Backup repository** da CloudFireMIrepo1 a **Veeam Cloud Platform - Mi1**  
![](/kb-assets/9e68d96355-image-20221118-164418.png)
5. Selezionare **Next** fino al termine della procedura selezionando **Enable the job when I click Finish**  
![](/kb-assets/4d9b48ad74-image-20221118-164831.png)

:::caution
Per gli altri tipi di job è necessario procedere con la modifica del **Backup Repository** nella sezione **Target**
:::