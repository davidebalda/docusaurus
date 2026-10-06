---
title: "Deploy PBX Yeastar PSE su Openstack"
---

### Procedimento {#procedimento}

Effettuare il deploy di un’istanza Ubuntu 20.04 definendo:

- le seguenti **istruzioni cloud-init** in fase di deploy della VM, per l’installazione del software Yeastar

```
#cloud-config
runcmd:
- [ wget, "https://update-ys2015-alicloud.oss-cn-hongkong.aliyuncs.com/YeastarSupport/pseinstallscripts/unyc_ubuntu.sh", -O, /root/unyc_ubuntu.sh ]
- [ chmod, +x, "/root/unyc_ubuntu.sh" ]
- [ sh, "/root/unyc_ubuntu.sh" ]
```

:::info
Lo script può impiegare fino a 60 minuti per eseguire tutta l'installazione.
:::

- un indirizzo **IP pubblico** della rete transparent, tramite il quale raggiungere il centralino.

Una volta effettuato il deploy del server, la console di gestione del PBX sarà accessibile via web tramite l’IP assegnato e la porta 8088 in https.  
Assicurarsi dunque di aver aperto tale porta per l’accesso remoto tramite i [Security Groups](../primi-passi-openstack-as-a-service/gestione-reti-porte-ip-pubblici-router-e-security-group.md#definizione-security-groups).