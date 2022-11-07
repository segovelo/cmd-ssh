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
1.2 In terminal type cd ../../../../home/segovelo\
1.3 Type segovelo@HP-Z2-G4:~$ code.\
1.4 Visual Studio code will open and then click ".bashrc" or ".bash_aliases"

Method 2:\
2.1 From any terminal type "wsl"\
2.2 Type cd .. as many times to get the prompt "segovelo@HP-Z2-G4:/$"\
2.3 Type cd home/segovelo\
2.4 Type segovelo@HP-Z2-G4:~$ code.\
2.5 Visual Studio code will open and then click ".bashrc" or ".bash_aliases"

Add the following in this ".bashrc" or ".bash_aliases" file and save it:

`#` alias to execute bash script to create a new git repository
alias scriptrepo="bash /mnt/c/Users/<Your/Path/To/Folder/ChangeIt>/scriptrepo.sh"

To run scriptrepo script from WSL 2\
Create a folder script-test in folder of your choice\
From WSL 2 command line\
cd ../../<Your/Path/To/Folder/ChangeIt>

From Ubuntu-20.04\
cd ../../mnt/c/<Your/Path/To/Folder/ChangeIt>

Then run\
segovelo@HP-Z2-G4:/mnt/c/<Your/Path/To/Folder/ChangeIt>$scriptrepo repo-test

---

# Run scriptrepo.sh from Windows command line using python script and batch file

python script to run scriptrepo.sh command in WSL-2

Include your local repo directory path to your system environment variable PATH
Do not forget to modify mkrepo.bat file with your local repo directory path, that way/
you will able torun mkrepo <repo_name> from any folder./

Upgrade from WSL to WSL-2 in Windows 10
https://winaero.com/update-from-wsl-to-wsl-2-in-windows-10/

C:\Users\some_user\desktop>wsl --set-version Ubuntu-20.04 2
C:\Users\some_user\desktop>wsl -l -v

OpenSSH server setup in WSL-2
https://www.youtube.com/watch?v=TJ1buhbhgDQ
segovelo@LAPTOP-T0H2E05J:~$sudo ssh-keygen -A
segovelo@LAPTOP-T0H2E05J:~$sudo apt install net-tools
segovelo@LAPTOP-T0H2E05J:~$ sudo service ssh start
segovelo@LAPTOP-T0H2E05J:~$sudo ufw allow ssh
segovelo@LAPTOP-T0H2E05J:~$ifconfig
segovelo@LAPTOP-T0H2E05J:~$ sudo service ssh stop

Automated ssh comands in python
https://www.youtube.com/watch?v=DYYxLSrJdW8&list=RDCMUC8wZnXYK_CGKlBcZp-GxYPA&index=8

Create a .env file with your ssh credentials
SSH_PASSPHRASE=<YOUR_SSH_PASSPHRASE>
SSH_PASSWORD=<YOUR_SSH_PASSWORD>

Dependecies:
pip install fabric
pip install python-dotenv
