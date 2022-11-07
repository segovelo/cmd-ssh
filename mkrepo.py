#!/usr/bin/env python3
import getpass
from fabric import Connection, Config
from dotenv import load_dotenv
import os, sys

load_dotenv()
pass_phrase = os.getenv("SSH_PASSPHRASE")
password = getpass.getpass("Enter your root password")
#password = os.getenv("SSH_PASSWORD")
config = Config(overrides={
    "sudo": {
        "password": password
        },
    "connect_kwargs": {
                "passphrase": pass_phrase  
    }
    })
    

connect_kwargs = {
    "passphrase": pass_phrase  
    }

conn = Connection("<YOUR.IP.CHANGE.IT>", user="<YOUR_USER>", config=config)

print("sys.arg[0]: ", sys.argv[0])
name = sys.argv[1]
print("sys.argv[1]: ",name)
calling_from_dir = os.getcwd().replace("C:\\","/mnt/c/").replace("\\","/")
print("os.getcwd(): ", calling_from_dir)
conn.run("pwd") 
with conn.cd(calling_from_dir):
    conn.run("pwd")
    conn.run(f"bash /mnt/c/users/<YOUR_USER>/<Your/Path/To/Folder/ChangeIt>/scriptrepo.sh {name}")    

