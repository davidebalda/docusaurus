---
title: "Tool IS/LSR installazione Linux"
---

Requisito necessario: Linux 64bit RPM-based. Come per esempio openSUSE o Fedora.

Scaricare l'archivio [Requirements](https://kb.acronis.com/system/files/content/2018/06/56070/requirements132.zip), estrarre **requirements.txt** e **fes-0.1.3.tar.gz** e copiarli nella cartella corrente.

La distribuzione di Linux deve avere i seguenti pacchetti: python3.5, python3-colorama, python3-pyOpenSSL packages. Nel caso non li avesse bisognerà installare python3.5 manualmente e installare colorama e pyOpenSSL via pip3.

Assicurarsi che le componenti siano correttamente installate con il comando:

```
pip3 list
```

L'output dovrebbe essere il seguente:

```
localhost ~ $ pip3 list...
colorama (0.3.7)
colorlog (2.6.1)...
fes (0.1.1)...
pip (8.0.2)...
pyOpenSSL (0.15.1)...
```

In seguito scaricare il tool [IS/LSR tool](https://dl.acronis.com/u/kb/IS_LSR_Tool_Build3.1.132_Linux.zip) e estrarlo. Installare il tool utilizzando il distribution package manager, per esempio:

```
sudo zypper install InitialSeedingTool64.rpm
```

Per installare Pyton 3.5  su CentOS 7.x dovete eseguire qualche spet aggiuntivo:

- Copiare il seguente file in **/etc/yum.repos.d/acronis-ius.repo**
```
[acronis-ius]
name=IUS repository mirror
baseurl=https://eu-repo.acronis.com/public/ius/
gpgcheck=0
enabled=1 
[vstorage]
name=Acronis Storage - $basearch
mirrorlist=http://storage-repo.acronis.com/vstorage/mirrorlists/2.0/releases-os.mirrorlist
#baseurl=http://storage-repo.acronis.com/vstorage/releases/2.0/x86_64/os/
enabled=1
gpgcheck=0
priority=50 
[vstorage-updates]
name=Acronis Storage Updates
mirrorlist=http://storage-repo.acronis.com/vstorage/mirrorlists/2.0/updates-os.mirrorlist
#baseurl=http://storage-repo.acronis.com/vstorage/updates/2.0/x86_64/os/
enabled=1
gpgcheck=0
priority=50
```
- Di seguito eseguire il seguente comando: 
```
yum install libffi-devel gcc openssl-devel python35u-devel python35u-pip archive3
pip3.5 install -r requirements.txt
rpm --install --nodeps InitialSeedingTool64.rpm
```