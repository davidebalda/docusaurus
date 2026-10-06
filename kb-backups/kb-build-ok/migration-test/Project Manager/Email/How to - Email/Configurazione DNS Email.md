Record da impostare presso il proprio domain register.

Variabili: 

- $DOM = nome del vostro dominio
- $SELECTOR = stringa fornita da Cloudfire, relativa al dominio in seguito alla registrazione
- $KEY = chiave RSA fornita da Cloudfire, relativa al dominio in seguito alla registrazione

|     |     |     |     |
| --- | --- | --- | --- |
| ### Record | ### TTL | ### Tipo | ### Target |
| **Autodiscover.$DOM.** | 0   | CNAME | [autoconfig.cloudfire.it](http://autoconfig.cloudfire.it). |
| **$SELECTOR.\_domainkey.$DOM.** | 0   | DKIM<br><br>  <br><br>(o TXT se non si dispone del record DKIM) | v=DKIM1; k=rsa; p=$KEY |
| **$DOM.** | 0   | MX  | 0 [mtx-mail.cloudfire.it](http://mtx-mail.cloudfire.it). |
| **$DOM.** | 600 | SPF | "v=spf1 a mx -all" |

Per maggiore sicurezza i consiglia la creazione del record DMARC:

|     |     |     |     |
| --- | --- | --- | --- |
| ### Dominio | ### TTL | ### Tipo | ### Target |
| **\_dmarc.$DOM.** | 0   | DMARC | v=DMARC1; p=quarantine; |

> [!WARNING]
> Verificare con il proprio register la piena compatibilità dei valori, ad esempio la corretta gestione di chiavi a 2048 bit per il DKIM.