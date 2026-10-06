---
title: "Tool IS/LSR installazione Windows"
---

Requisito necessario: Windows 64bit

1. Scaricare [python3.5 installer](https://www.python.org/downloads/release/python-353/). Per semplicità, selezionare l'opzione **Install launcher for all users** e **Add Python 3.5 to PATH:**  
![](/kb-assets/37d8d234f1-image2018-10-11-15-14-34.png)
2. Assicurarsi di installare il pip tool:  
![](/kb-assets/d09dcda37b-image2018-10-11-15-16-21.png)
3. Dopo aver completato l'installazione aprire il prompt dei comandi come amministratore.
4. Scaricare l'archivio [Requirements](https://kb.acronis.com/system/files/content/2018/06/56070/requirements132.zip), estrarre **requirements.txt** e **fes-0.1.3.tar.gz** e copiarli nella cartella corrente.
5. Nel prompt dei comandi eseguire i seguenti comandi:
```
python -m pip install --upgrade pip
pip3 install -r requirements.txt 
pip install --upgrade pyOpenSSL
```
![](/kb-assets/908a4bc3ab-image2018-10-11-15-22-42.png)
6. Scaricare [IS/LSR tool](https://dl.acronis.com/u/kb/IS_LSR_Tool_Build3.1.132_Windows.zip) e spacchettarlo.
7. Installare il tool ed eseguire l'msi package.