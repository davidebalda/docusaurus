## Guida passo per passo

1. Run the following command to find out the kernel version and the required GCC version: 
```
cat /proc/version
```
ES: Linux version 4.4.0-104-generic (buildd@lgw01-amd64-022) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.5)
2. Run the following command to check whether the Make tool and the GCC compiler are installed:
```
make -v
gcc -vFor gcc, ensure that the version returned by the command is the same as in the gcc version in step 1. For make, just ensure that the command runs.
```
3. ```
Check whether the appropriate version of the packages for building kernel modules is installed:
```
4. 
1.   In Red Hat Enterprise Linux, CentOS, and Fedora, run the following command:
  ```
  yum list installed | grep kernel-devel
  ```
2.   In Ubuntu, run the following commands
  ```
  dpkg --get-selections | grep linux-headers
  dpkg --get-selections | grep linux-image
  ```
  In either case, ensure that the package versions are the same as in Linux version in step 1.  
5. Run the following command to check whether the Perl interpreter is installed:
```
perl --version
```
  
If you see the information about the Perl version, the interpreter is installed.

In case of Incongruence continue on

[https://dl.managed-protection.com/u/baas/help/7.5/user/en-US/index.html#22619.html](https://dl.managed-protection.com/u/baas/help/7.5/user/en-US/index.html#22619.html)

The following table lists how to install the required packages in various Linux distributions.

|     |     |     |
| --- | --- | --- |
| Linux distribution | Package names | How to install |
| Red Hat Enterprise Linux | kernel-devel  <br>gcc  <br>make | The setup program will download and install the packages automatically by using your Red Hat subscription. |
| perl | Run the following command:<br><br>```<br>yum install perl<br>``` |
| CentOS<br><br>Fedora | kernel-devel  <br>gcc  <br>make | The setup program will download and install the packages automatically. |
| perl | Run the following command:<br><br>```<br>yum install perl<br>``` |
| Ubuntu | linux-headers  <br>linux-image  <br>gcc  <br>make  <br>perl | Run the following commands:<br><br>```<br>sudo apt-get update<br><br>sudo apt-get install linux-headers-`uname -r`<br><br>sudo apt-get install linux-image-`uname -r`<br><br>sudo apt-get install gcc-<package version><br><br>sudo apt-get install make<br><br>sudo apt-get install perl<br>``` |

 In Ubuntu's case, after gcc-version package install check again

```
gcc -v
```

if not present you have to additionally install gcc package runn

```
sudo apt-get install gcc
```

  
Download or upload the agent on machine.

Give execution permissions:

```
chmod +x agent.bin
```

Verify to have RPM utility installed (needed for installation).

```
chmod +x agent.bin
```

Linux Agent installation prerequisites

Make sure that the RPM Package Manager (RPM) is installed in your system. Before installing the product on a Linux distribution that does not use RPM, such as Ubuntu, you need to install RPM manually; for example, by running the following command:

```
sudo yum install rpm (Red Hat based distributions)
sudo apt-get install rpm (Debian based distributions); in case of an Ubuntu distro.
sudo zypper install rpm (Suse based distributions)
sudo yast install rpm (Suse based distributions)”
```

Install: 

```
sudo ./agent.bin
```

  
Specify the credentials of the account to which the machine should be assigned.

Select the check boxes for the agents that you want to install (if asked). The following agents are available:

             Agent for Linux (not Virtuozzo)

In case of server without graphical interface, select "Show Registration Details", copy and paste code in Acronis "Add" section using "Registration via Code" or using the following link:

- URL - Region Acronis-Eu2 - Francoforte, Germania: [http://eu2.backup.cloudfire.it/bc/reg](http://eu2.backup.cloudfire.it/bc/reg)
- URL - Region Acronis-Eu8 - Francoforte, Germania: [http://eu8.backup.cloudfire.it/bc/reg](http://eu8.backup.cloudfire.it/bc/reg)

- URL - Region Acronis-It01 - Roma, Italia: [http://it01.backup.cloudfire.it/bc/reg](http://it01.backup.cloudfire.it/bc/reg) ( in sostituzione a URL: [https://backup.cloudfire.it/bc/reg](https://backup.cloudfire.it/bc/reg))

If you have to uninstall the agent run:

```
sudo /usr/lib/Acronis/BackupAndRecovery/uninstall/uninstall
```

  
and eventually remove the machine from Acronis console.