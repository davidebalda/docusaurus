## Introduzione

Questa procedura è rivolta ai service provider/partner che vogliono attivare il servizio per se o per i propri clienti.

Di seguito i semplici passaggi di attivazione del servizio VPN su Public Cloud

## Prerequisiti

Per realizzare la VPN occorre avere accesso al Firewall Cisco ASA in modalità "Privileged EXEC"

## Guida passo-passo

![](./attachments/VPN%202.png)

![](./attachments/VPN%201.png)

![](./attachments/VPN%204.1.png)

![](./attachments/VPN%203.png)

![](./attachments/VPN%205.png)

![](./attachments/VPN%204.2.png)

### Configurazione Cisco ASA

```
ciscoasa> ena
Password: **********
ciscoasa#

ciscoasa# conf t
ciscoasa(config)#

! Inserire la Configurazione !
```

#### Configurazione

```
object network NET_LOCAL
subnet  $Local Subnet es: 192.168.52.0 255.255.255.0

object-group network NET_CLOUD
network-object $Remote Subnet es: 192.168.168.0 255.255.255.0



access-list VPN-CLOUD extended permit ip object NET_LOCAL object-group NET_CLOUD

nat (inside,Outside) source static NET_LOCAL NET_LOCAL destination static NET_CLOUD NET_CLOUD no-proxy-arp route-lookup

crypto ipsec ikev1 transform-set esp-aes256-sha esp-aes-256 esp-sha-hmac
crypto ipsec security-association pmtu-aging infinite
crypto ipsec df-bit clear-df Outside



crypto map CLOUD_MAP 10 match address VPN-CLOUD
crypto map CLOUD_MAP 10 set pfs
crypto map CLOUD_MAP 10 set peer $SERVICE_IP IPv4 
crypto map CLOUD_MAP 10 set ikev1 transform-set esp-aes256-sha
crypto map CLOUD_MAP 10 set security-association lifetime seconds 86400
crypto map CLOUD_MAP interface Outside

crypto isakmp identity address
crypto ikev1 enable Outside

crypto ikev1 policy 10
authentication pre-share
encryption aes-256
hash sha
group 2
lifetime 86400
```

```
tunnel-group $SERVICE_IP type ipsec-l2l
tunnel-group $SERVICE_IP ipsec-attributes
 ikev1 pre-shared-key $PRE_SHARED
```

> [!INFO]
> NOTE:
> $Local Subnet = rete/i locale/i
> $Remote Subnet = rete/i remota/e
> $PRE\_SHARED = pre-shared key
> $SERVICE\_IP = ip vpn service public cloud
> Configurazione testata con Cisco Adaptive Security Appliance Software Version 9.1(4)

  

  

  

> [!NOTE]
> **Sommario**
> 
> 
> 
> - [Introduzione](#introduzione)
> - [Prerequisiti](#prerequisiti)
> - [Guida passo-passo](#guida-passo-passo)
> -   [Configurazione Cisco ASA](#configurazione-cisco-asa)
>   
>   -   [Configurazione](#configurazione)
>     
>   
>     -   Filter by label
> * * *
> **Articoli collegati**
> 
> 
> ##### Filter by label
> 
> There are no items with the selected labels at this time.