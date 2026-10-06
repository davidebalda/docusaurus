*La seguente guida presuppone dimestichezza con le funzionalità e features di Public Cloud.*

***Attenzione! al termine della guida la macchina perderà le configurazioni di mac address, indirizzi ip, uuid e quant’altro.***  
*Se e solo se si è sicuri che non si creeranno problematiche nella riconfigurazione della vm procedere con la guida. In caso di incertezza NON effettuare nessun passaggio e consultare il team CloudFire a* [*help@cloudfire.it*](mailto:help@cloudfire.it)  
  
**Presa nota di quanto scritto sopra, procedere con la lettura**

1. Spegnere la macchina arrestando tutti i servizi in maniera corretta.
2. Creare lo snapshot

![](./attachments/image-20211210-112458.png)

3\. Recarsi sotto la voce Volumes e creare un nuovo volume SSD (della stessa dimensione del disco originale)

![](./attachments/image-20211210-113944.png)

4\. Ora modificare il volume da standard a ssd

![](./attachments/image-20211210-114300.png)

![](./attachments/image-20211210-114400.png)

5\. Ora fare il Launch Instance dal disco nuovo SSD.

![](./attachments/image-20211210-114642.png)

6\. Fine