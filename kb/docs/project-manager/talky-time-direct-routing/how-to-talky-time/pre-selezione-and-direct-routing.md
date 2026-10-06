---
title: "Pre-selezione & Direct Routing"
---

Questa pagina definisce i requisiti i processi per configurare **Microsoft Teams,** per utilizzare la **preselezione** impostata nel PBX on-premise che si sta integrando con Talky Time.

## Prerequisiti {#prerequisiti}

- **Utente con privilegi di Teams Admin** per il dominio che si vuole configurare
- Il **codice della preselezione** da configurare

## Configurazione della Preselezione su Microsoft Teams {#configurazione-della-preselezione-su-microsoft-teams}

1. Accedi al pannello di gestione [**Microsoft Teams**](https://admin.teams.microsoft.com)
2. Nel menù a sinistra clicca su ***Voice → Dial Plan***
3. Seleziona il ***Dial Plan Global (Org-wide default)***  
![](/kb-assets/3f1bf7219f-screenshot-2022-01-14-at-12-34-23.png)
4. Compila il campo ***External dialing prefix*** (es. 0) e abilitalo spostando il cursore su ***ON***  
![](/kb-assets/1483b7587c-screenshot-2022-01-14-at-12-19-38.png)

Da questo momento sarà possibile utilizzare l' integrazione Talky Time con il proprio PBX configurato con la preselezione.