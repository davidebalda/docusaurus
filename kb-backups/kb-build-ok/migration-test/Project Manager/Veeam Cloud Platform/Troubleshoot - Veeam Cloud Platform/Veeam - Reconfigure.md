## Modificare le credenziali d’accesso

1. Accedere a Cortex e recarsi sulla pagina del servizio Veeam Cloud Platform
2. Selezionare “Reimposta password” dal riquadro Veeam Cloud Connect e configurare una nuova password (consigliamo una password complessa: minimo 10 caratteri, maiuscole, minuscole, cifre e caratteri speciali)

![](./attachments/immagine-20221118-171503.png)

3\. Nel riquadro Veeam Cloud Connect sono inoltre presenti il nuovo gateway URL ([vcg.cloudfire.it](http://vcg.cloudfire.it)) e il nuovo username (… \_1), che serviranno nei passaggi successivi

## Modificare il Service Provider

1. Collegarsi alla console Veeam Backup and Replication
2. Sezione **Backup Infrastructure** → **Add Provider**![](./attachments/image-20221118-163339.png)
3. Configurare DNS name [**vcg.cloudfire.it**](http://vcg.cloudfire.it)  
![](./attachments/1.png)
  
![](./attachments/image-20221118-163458.png)

4\. Creare / Selezionare le nuove credenziali ( **username nuovo finisce con \_1** )  

![](./attachments/2.png)

![](./attachments/3.png)

5\. Verificare che il Repository sia **Veeam Cloud Platform - Mi1**  

![](./attachments/image-20221118-163713.png)

![](./attachments/image-20221118-163826.png)

![](./attachments/image-20221118-163856.png)

![](./attachments/4.png)

## Modificare Job di Backup Copy

1. Sezione **Home** → **Jobs** → **Backup Copy**  
![](./attachments/image-20221118-164036.png)
2. Selezionare un job per volta quindi **Disable**![](./attachments/image-20221118-164539.png)
3. Clonare il primo job **Selezionando il job** → **Clone**![](./attachments/image-20221118-164622.png)
4. Editare il job **CLONATO** cliccando **Tasto DESTRO** → **Edit** : Portarsi alla voce **Target** quindi modificare dal menu a tendina il **Backup repository** da CloudFireMIrepo1 a **Veeam Cloud Platform - Mi1**  
![](./attachments/image-20221118-164418.png)
5. Selezionare **Next** fino al termine della procedura selezionando **Enable the job when I click Finish**  
![](./attachments/image-20221118-164831.png)

> [!CAUTION]
> Per gli altri tipi di job è necessario procedere con la modifica del **Backup Repository** nella sezione **Target**