---
title: "Estendere volume Guest OS (Linux) senza riavviare"
---

## Linux

:::caution
**Si consiglia di eseguire un backup dell' istanza prima di procedere**
:::

Per estendere il volume di root di un' istanza con sistema Operativo Linux, a seguito dell' estensione a caldo del disco svolta dal supporto Cloudfire, occorre procedere come segue:

### Debian | Ubuntu

1. Collegarsi all' istanza tramite ssh o direttamente in console
2. Individuare il disco da estendere con il comando:
```
sudo fdisk -l
```
```
Disk /dev/loop0: 61.98 MiB, 64966656 bytes, 126888 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk /dev/loop1: 67.83 MiB, 71106560 bytes, 138880 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk /dev/loop2: 46.98 MiB, 49242112 bytes, 96176 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
GPT PMBR size mismatch (104857599 != 209715199) will be corrected by write.
The backup GPT table is not on the end of the device. This problem will be corrected by write.
Disk /dev/vda: 100 GiB, 107374182400 bytes, 209715200 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 8D44F517-DC04-4D7C-8A16-1CDC75907C62
Device      Start       End   Sectors  Size Type
/dev/vda1  227328 104857566 104630239 49.9G Linux filesystem
/dev/vda14   2048     10239      8192    4M BIOS boot
/dev/vda15  10240    227327    217088  106M EFI System
Partition table entries are not in disk order.
```
Oppure usando il comando:
```
sudo lsblk
```
```
NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0     7:0    0   62M  1 loop /snap/core20/1611
loop1     7:1    0 67.8M  1 loop /snap/lxd/22753
loop2     7:2    0   47M  1 loop /snap/snapd/16292
vda     252:0    0  100G  0 disk
├─vda1  252:1    0 49.9G  0 part /
├─vda14 252:14   0    4M  0 part
└─vda15 252:15   0  106M  0 part /boot/efi
```

:::info
In questo caso il disco da estendere è ***vda1*** che passa da 50GB a 100GB
:::

3\. Installare i cloud-utils in cui è compreso **growpart**

```
sudo apt install -y cloud-utils
```

4\. Per estendere **vda1** eseguire il comando:

```
sudo growpart /dev/vda 1
```

:::warning
/dev/vda 1 è diverso da /dev/vda1 ed è volutamente scritto in questo modo perché growpart estende, del disco /dev/vda, la partizione numero 1
:::

5\. Estendere filesystem:

```
resize2fs /dev/vda1
```