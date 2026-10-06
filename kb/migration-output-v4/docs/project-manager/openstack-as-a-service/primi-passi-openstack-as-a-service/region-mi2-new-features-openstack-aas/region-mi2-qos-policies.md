---
title: "Region MI2 - QoS Policies"
---

Per la parte di networking è stata introdotta la possibilità di creazione di **policy di Quality of Service**, per limitare l’utilizzo di banda.  
Per fare ciò è sufficiente creare una nuova regola di limite di banda ed assegnarla al Floating IP su cui si vuole agire.

![image-20250716-105752.png](/kb-assets/6d9993463a-image-20250716-105752.png)

![image-20250716-105829.png](/kb-assets/9ca58f7cad-image-20250716-105829.png)

:::info
La banda di default è di 1Gb simmetrico, perciò le regole di QoS si possono configurare al ribasso entro questi limiti.
:::