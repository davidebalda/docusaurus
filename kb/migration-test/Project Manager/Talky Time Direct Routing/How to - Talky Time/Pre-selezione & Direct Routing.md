Questa pagina definisce i requisiti i processi per configurare **Microsoft Teams,** per utilizzare la **preselezione** impostata nel PBX on-premise che si sta integrando con Talky Time.

## Prerequisiti

- **Utente con privilegi di Teams Admin** per il dominio che si vuole configurare
- Il **codice della preselezione** da configurare

## Configurazione della Preselezione su Microsoft Teams

1. Accedi al pannello di gestione [**Microsoft Teams**](https://admin.teams.microsoft.com)
2. Nel menù a sinistra clicca su ***Voice → Dial Plan***
3. Seleziona il ***Dial Plan Global (Org-wide default)***  
![](./attachments/Screenshot%202022-01-14%20at%2012.34.23.png)
4. Compila il campo ***External dialing prefix*** (es. 0) e abilitalo spostando il cursore su ***ON***  
![](./attachments/Screenshot%202022-01-14%20at%2012.19.38.png)

Da questo momento sarà possibile utilizzare l' integrazione Talky Time con il proprio PBX configurato con la preselezione.