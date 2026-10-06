---
title: "Disinstallazione dell'agente Acronis su macchina Windows"
---

## **Introduzione** {#introduzione}

È possibile disinstallare qualsiasi prodotto di backup di Acronis selezionandolo dalla lista dei programmi installati di Windows o, in alternativa, facendo partire l’eseguibile di installazione. Può capitare però che in certi casi la disinstallazione fallisca. Di seguito verranno elencati tutti gli step per disintallare o rimuovere l’agente.

## **Soluzione** {#soluzione}

Per disinstallare qualsiasi software di Acronis da una macchina Windows, seguire in ordine i seguenti passaggi:

1. Andare su *Pannello di controllo* → *Programmi e funzionalità* → selzionare il software *Acronis…* che si vuole rimuovere → *Disinstalla*.
2. Nel caso la soluzione sopra indicata non andasse a buon fine, avviare il file eseguibile di installazione dell’agente e scegliere l’opzione per rimuovere il prodotto.
3. Se i passaggi precedenti non portano alla rimozione completa del prodotto, utilizzare lo [strumento Microsoft Fixit](https://download.microsoft.com/download/7/E/9/7E9188C0-2511-4B01-8B4E-0A641EC2F600/MicrosoftProgram_Install_and_Uninstall.meta.diagcab). Una volta scaricato, eseguire il software e seguire i passaggi indicati, selezionando il software che si desidera rimuovere.
4. Se Microsoft Fixit non è in grado di risolvere il problema, utilizzare l’Acronis Cleanup Utility.

### **Acronis Cleanup Utility** {#acronis-cleanup-utility}

Cleanup Utility deve essere utilizzato solo nel caso in cui il prodotto non venga disinstallato tramite gli step elencati in precedenza.

**Come misura precauzionale, prima di utilizzare Cleanup Utility, è vivamente consigliato eseguire un backup del sistema.**

L’esecuzione dell’Utility potrebbe chiudere tutte le finestre di Esplora risorse.

Si consiglia di disattivare temporaneamente *Startup Recovery Manager* (se attivato), prima di utilizzare il tool.

1. Scaricare il Cleanup Utility, [x64](https://dl2.acronis.com/u/kb/cleanup_tool.exe) oppure [x32](https://dl2.acronis.com/u/kb/cleanup_tool_x32.exe)
2. Aprire il *Prompt dei comandi* di Windows come amministratore.
3. Usando il comando *cd*, spostarsi nella cartella in cui avete effettuato il download del tool.
4. Eseguire l’utility tramite uno dei seguenti comandi:  
![](/kb-assets/41ad6f4b7b-immagine-20221202-092213.png)
1.   Per eseguire il tool con i parametri predefiniti:  
  **cleanup\_tool.exe**  
  Verrà chiesta conferma per la rimozione del software e i suoi componenti. Verrà richiesto anche un riavvio della macchina, se necessario (sconsigliato subito dopo l’esecuzione del comando, leggere sotto).  
2.   Per eseguire il tool senza l’interazione dell’utente:  
  **cleanup\_tool.exe --quiet**  
  Con il parametro *\--quiet* il software e suoi componenti verranno rimossi senza alcuna richiesta di conferma. La macchina NON verrà riavviata.  
  
  1.   Per eseguire il tool ed eliminare l’Acronis Secure Zone:  
    **cleanup\_tool.exe --quiet --delete-asz**  
  
  2.   Per permettere il riavvio automatico del PC (sconsigliato, leggere sotto):  
    **cleanup\_tool.exe --quiet --allow-reboot**

5\. Dopo aver eseguito il comando, l’utility rimuoverà tutti i componenti del software che rileva sulla macchina.  
  
**Dopo aver utilizzato Cleanup Utility, si consiglia vivamente di non riavviare la macchina**. Aprire il regedit e verificare che non ci siano stringhe *snapman\**, *tdrpman\**, *fltsrv,* *timounter, tib\_mounter* negli UpperFilters e LowerFilters delle seguenti chiavi di registro:

- HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E967-E325-11CE-BFC1-08002BE10318}
- HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{71A27CDD-812A-11D0-BEC7-08002BE2092F} 

Se ce ne sono, rimuovere le stringhe dagli UpperFilters e LowerFilters delle chiavi menzionate sopra.  
**Non cancellare le chiavi!**

Riavviare infine la macchina.