---
title: "VPNaaS - Watchguard Firewall"
---

## Introduzione

Configurazione Watchguard presso cliente per attivazione tunnel con servizio VPNaaS Cloudfire.

## Guida passo-passo

### Definizione Gateway: VPN → Branch Office Gateways

![](/kb-assets/46119da734-image2019-8-12-13-0-51.png)

![](/kb-assets/a86e632599-image2019-8-12-13-3-29.png)

![](/kb-assets/ae69efeaf1-image2019-8-12-12-52-3.png)

### Definizione Tunnel: VPN → Branch Office Tunnels

![](/kb-assets/3d754da631-image2019-8-12-12-52-33.png)

![](/kb-assets/dc859f954e-image2019-8-12-12-52-44.png)

:::warning
Personalizzare i "Phase 2 Settings" poichè la configurazione di default non è corretta:
:::

![](/kb-assets/dd7557886c-image2019-8-12-12-54-38.png)

![](/kb-assets/23c1ba8164-image2019-8-12-12-54-20.png)

Al termine della configurazione vengono create 2 regole che consentono tutto il traffice Da e Verso il tunnel Cloudfire (N.B. di default non è attivo il logging)

![](/kb-assets/aa90481b0c-image2019-8-12-12-55-34.png)

![](/kb-assets/4e82518547-image2019-8-12-12-55-54.png)

  

  

  

:::note
**Sommario**



- [Introduzione](#introduzione)
- [Guida passo-passo](#guida-passo-passo)
-   [Definizione Gateway: VPN → Branch Office Gateways](#definizione-gateway-vpn-branch-office-gateways)
-   [Definizione Tunnel: VPN → Branch Office Tunnels](#definizione-tunnel-vpn-branch-office-tunnels)
  
  -   Filter by label
* * *
**Articoli collegati**


##### Filter by label

There are no items with the selected labels at this time.
:::