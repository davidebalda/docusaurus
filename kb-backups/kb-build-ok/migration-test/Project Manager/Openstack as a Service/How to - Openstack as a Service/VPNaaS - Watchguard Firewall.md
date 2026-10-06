## Introduzione

Configurazione Watchguard presso cliente per attivazione tunnel con servizio VPNaaS Cloudfire.

## Guida passo-passo

### Definizione Gateway: VPN → Branch Office Gateways

![](./attachments/image2019-8-12_13-0-51.png)

![](./attachments/image2019-8-12_13-3-29.png)

![](./attachments/image2019-8-12_12-52-3.png)

### Definizione Tunnel: VPN → Branch Office Tunnels

![](./attachments/image2019-8-12_12-52-33.png)

![](./attachments/image2019-8-12_12-52-44.png)

> [!WARNING]
> Personalizzare i "Phase 2 Settings" poichè la configurazione di default non è corretta:

![](./attachments/image2019-8-12_12-54-38.png)

![](./attachments/image2019-8-12_12-54-20.png)

Al termine della configurazione vengono create 2 regole che consentono tutto il traffice Da e Verso il tunnel Cloudfire (N.B. di default non è attivo il logging)

![](./attachments/image2019-8-12_12-55-34.png)

![](./attachments/image2019-8-12_12-55-54.png)

  

  

  

> [!NOTE]
> **Sommario**
> 
> 
> 
> - [Introduzione](#introduzione)
> - [Guida passo-passo](#guida-passo-passo)
> -   [Definizione Gateway: VPN → Branch Office Gateways](#definizione-gateway-vpn-branch-office-gateways)
> -   [Definizione Tunnel: VPN → Branch Office Tunnels](#definizione-tunnel-vpn-branch-office-tunnels)
>   
>   -   Filter by label
> * * *
> **Articoli collegati**
> 
> 
> ##### Filter by label
> 
> There are no items with the selected labels at this time.