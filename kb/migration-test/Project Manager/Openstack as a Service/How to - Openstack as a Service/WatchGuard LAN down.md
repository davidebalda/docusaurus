Nel caso in cui la LAN del vostro WatchGuard su Openstack as a Service risulti down, controllare le seguenti cose:

- che la licenza sia attiva (controllare la data di scadenza delle features del WatchGuard dentro il portale);
- assicurarsi che LAN abbia MTU 1450 (valore della private di Openstack).

Per farlo, entrare in console da OpenStack:

- Login sul firewall (admin/readwrite è il default)
- config->interface fasteth 1
- mtu 1450

> [!INFO]
> Vale anche per Sophos e probabilmente altri firewall con discriminante sul MTU della LAN.