---
title: "Attach Folder di una cartella di rete"
---

Se si tenta di fare un "attach folder" di una cartella di rete su D4B è possibile che non vengano sincronizzati i file. Questo probabilmente è dovuto al fatto che D4B non riconosce i path di rete. Per ovviare a questa problematica si può aggirare il problema eseguendo questi step:

- Per ovviare al problema del percorso di rete bisogna fare in modo che la cartella che si vuole sincronizzare venga vista da D4B come una cartella locale. Per fare questo bisogna creare una cartella in locale ed applicargli un link simbolico alla cartella di rete. Per fare questo seguire questi step:
-   eseguire il prompt dei comandi come amministratore
-   digitare i seguenti comandi:
  ```
  C:\WINDOWS\system32>net use y: \\SRV-XXX\Utenti\Mario_Rossi * /user:XXX\mario.rossi /persistent:yes
  Digitare la password per \\SRV-XXX\Utenti\Mario_Rossi:
  Esecuzione comando riuscita.
  C:\Windows\System32>mklink /d C:\test2 \\SRV-XXX\Utenti\Mario_Rossi
  collegamento simbolico creato per C:\test2 <<===>> \\SRV-XXX\Utenti\Mario_Rossi
  ```
  La prima riga fa in modo che venga mappata un unità di rete corrispondente alla cartella di rete interessata.La seconda invece applica un link simbolico tra l'unità mappata precedentemente e una nuova cartella generata dal comando stesso.

- Una volta fatto questo è sufficiente cliccare con il destro sulla cartella appena creata e selezionare "Attach this folder su D4B".
- Verificare che effettivamente la sincronizzazione dei file stia procedendo correttamente.