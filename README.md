# cmd-ssh repo

# scriptrepo.sh

Bash script to create README.md file, initialize a .git repository, commit, create remote repo and push to https://www.github.com

Tutorial from https://www.freecodecamp.org/news/command-line-for-beginners/?fbclid=IwAR1TUE4XrL58zYg3khtt0QlRPM0EEVskPDsp4BhagPnZIkfoQ88XxXACf_I

Execute from command line by passing the repo name as a parameter.\
**You will need an external git_credentials.sh file containing your github username and access token. Change them**

https://developpaper.com/three-ways-for-shell-script-to-call-another-script

# To create a new git repository run scriptrepo.sh script from any folder you are

### To store GitHub credentials in git_credentials.sh and call them from anywhere

If you do not have a GitHub access token to include in git_credentials.sh go to Settings > Developer settings > Personal access tokens > Generate new token

![image](https://user-images.githubusercontent.com/44499182/192099446-fd4625c7-8abb-467f-9444-c84403bdaaf1.png)

To source a external shell script from any directory with git credentials

https://unix.stackexchange.com/questions/216910/bash-command-to-source-a-file-in-a-different-directory

# I will show how to create an alias to execute bash script.

https://code.visualstudio.com/docs/remote/wsl

To open VS Code from WSL:Ubuntu-20.04 and land into /home/segovelo/.bashrc file

Method 1:\
1.1 Type wsl in "search" task bar to open Ubunto-20.04 terminal\
1.2 In terminal type segovelo@LAPTOP-T0H2E05J:/mnt/c/windows/system32$ cd ~
1.3 Type segovelo@LAPTOP-T0H2E05J:~$ code.\
1.4 Visual Studio code will open and then click ".bashrc" or ".bash_aliases"

Method 2:\
2.1 From any terminal type "wsl"\
2.2 Type cd .. as many times to get the prompt "segovelo@LAPTOP-T0H2E05J:/$"\
2.3 Type cd home/segovelo\
2.4 Type segovelo@LAPTOP-T0H2E05J:~$ code.\
2.5 Visual Studio code will open and then click ".bashrc" or ".bash_aliases"

Add the following in this ".bashrc" or ".bash_aliases" file and save it:

`#` alias to execute bash script to create a new git repository\
alias scriptrepo="bash /mnt/c/Users/<Your/Path/To/Folder/ChangeIt>/scriptrepo.sh"

To run scriptrepo script from WSL 2\
Create a folder script-test in folder of your choice\
From WSL 2 command line\
cd ../../<Your/Path/To/Folder/ChangeIt>

From Ubuntu-20.04\
cd ../../mnt/c/<Your/Path/To/Folder/ChangeIt>

Then run\
segovelo@LAPTOP-T0H2E05J:/mnt/c/<Your/Path/To/Folder/ChangeIt>$scriptrepo repo-test

---

# Run scriptrepo.sh from Windows command line using python script and batch file

python script mkrepo.py to run scriptrepo.sh from windows command line.

Include your local repo directory path inside your system environment variable PATH\
Do not forget to modify mkrepo.bat file with your local repo directory path, that way\
you will able to run\
C:\users\segovelo\desktop>mkrepo <repo_name>\
from any folder.

Create a .env file with your ssh credentials\
SSH_PASSPHRASE=<YOUR_SSH_PASSPHRASE>\
SSH_PASSWORD=<YOUR_SSH_PASSWORD>

Dependecies:\
pip install fabric\
pip install python-dotenv

# Initialize ssh server

Upgrade from WSL to WSL-2 in Windows 10\
https://winaero.com/update-from-wsl-to-wsl-2-in-windows-10

C:\Users\some_user\desktop>wsl --set-version Ubuntu-20.04 2\
C:\Users\some_user\desktop>wsl -l -v\

OpenSSH server setup in WSL-2\
https://www.youtube.com/watch?v=TJ1buhbhgDQ\
segovelo@LAPTOP-T0H2E05J:~$sudo apt install openssh-server\
segovelo@LAPTOP-T0H2E05J:~$sudo ssh-keygen -A\
segovelo@LAPTOP-T0H2E05J:~$sudo apt install net-tools\
segovelo@LAPTOP-T0H2E05J:~$ sudo service ssh start\
segovelo@LAPTOP-T0H2E05J:~$sudo ufw allow ssh\
segovelo@LAPTOP-T0H2E05J:~$ifconfig

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500\
&nbsp;&nbsp;&nbsp;inet 172.21.148.67 netmask 255.255.240.0 broadcast 172.21.159.255

Copy the IP address you get after "inet", in the example above would be\
"172.21.148.67" and paste it in mkrepo.py file in line 25.

Go back to Windows command line a create a ssh key:\
C:\Users\some_user\desktop>ssh-keygen -t rsa\
.\
.\
.\
C:\Users\some_user\desktop>cd .ssh\
C:\Users\some_user\desktop\.ssh>dir\
02/11/2022 21:34 <DIR> .\
02/11/2022 21:34 <DIR> ..\
02/11/2022 21:23 2,655 id_rsa\
02/11/2022 21:23 573 id_rsa.pub\
07/11/2022 18:33 353 known_hosts

C:\Users\some_user\desktop\.ssh>copy id_rsa.pub C:\Users\some_user\desktop>\
&nbsp;&nbsp;1 file(s) copied.

Go back to Ubuntu-20.04 terminal\
segovelo@LAPTOP-T0H2E05J:/mnt/c/users/some_user/desktop$ cp id_rsa.pub ~/.ssh/authorized_keys\
segovelo@LAPTOP-T0H2E05J:/mnt/c/users/some_user/desktop$ cd ~/.ssh\
segovelo@LAPTOP-T0H2E05J:~/.ssh$ ls\
&nbsp;&nbsp;authorized_keys\
segovelo@LAPTOP-T0H2E05J:~/.ssh$ cat authorized_keys\
segovelo@LAPTOP-T0H2E05J:~/.ssh$ ifconfig

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500\
&nbsp;&nbsp;&nbsp;inet 172.21.148.67 netmask 255.255.240.0 broadcast 172.21.159.255

Copy the IP address you get after "inet", in the example above would be\
"172.21.148.67" and go back to Windows command line.

C:\Users\some_user\desktop>ssh <YOUR_USER>@172.21.148.67\
Enter passphrase for key 'C:\Users\Sebastian/.ssh/id_rsa':\
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.72-microsoft-standard-WSL2 x86_64)

- Documentation: https://help.ubuntu.com\
- Management: https://landscape.canonical.com\
- Support: https://ubuntu.com/advantage\

System information as of Mon Nov 7 20:36:26 GMT 2022

&nbsp;&nbsp;System load: 0.0 Processes: 10\
&nbsp;&nbsp;Usage of /: 0.8% of 250.98GB Users logged in: 0\
&nbsp;&nbsp;Memory usage: 0% IPv4 address for eth0: 172.21.148.67\
&nbsp;&nbsp;Swap usage: 0%

179 updates can be installed immediately.\
75 of these updates are security updates.\
To see these additional updates run: apt list --upgradable\

New release '22.04.1 LTS' available.\
Run 'do-release-upgrade' to upgrade to it.

Last login: Mon Nov 7 18:46:45 2022 from 172.21.144.1
segovelo@LAPTOP-T0H2E05J:~$

**You got connected to WSL from Windows command line**

To exit WSL command line back to Windows just type exit:\
segovelo@LAPTOP-T0H2E05J:~$ exit\
logout\
Connection to 172.21.148.67 closed.\
C:\Users\some_user\desktop>

Go back to Windows command line.\
You are now ready to execute mkrepo.bat from Windows command line which then\
run mkrepo.py and this executebash /mnt/c/Users/<Your/Path/To/Folder/ChangeIt>/scriptrepo.sh\
C:\Users\some_user\desktop>mkrepo repo-name

When you finish and before closing terminal stop ssh server\
segovelo@LAPTOP-T0H2E05J:~$ sudo service ssh stop

Automated ssh comands in python\
https://www.youtube.com/watch?v=DYYxLSrJdW8&list=RDCMUC8wZnXYK_CGKlBcZp-GxYPA&index=8
