Altra funzionalità a livello di rete che è stata implementata è la possibilità di creare un **Load Balancer** nativo all’interno di Openstack.

Per procedere con il deploy bisogna seguire il wizard d’installazione e definire le varie configurazioni del Listener e del Pool su cui dirottare il traffico.

- Si parte definendo le configurazioni di base, come la rete e l’IP di riferimento:

![image-20250716-125726.png](./attachments/image-20250716-125726.png)

- Si procede con le impostazioni del Listener, scegliendo il protocollo desiderato:

![image-20250716-125858.png](./attachments/image-20250716-125858.png)

- Successivamente si sceglie l’algoritmo del Pool, per la tipologia di instradamento delle connessioni, e il protocollo:

![image-20250716-130114.png](./attachments/image-20250716-130114.png)

- Definire quindi i membri:

![image-20250716-130254.png](./attachments/image-20250716-130254.png)

- E scegliere infine se attivare l’Health Monitor:

![image-20250716-130512.png](./attachments/image-20250716-130512.png)

> [!WARNING]
> Il Load Balancer **genera consumo** a livello di fatturazione, in base al profilo scelto.