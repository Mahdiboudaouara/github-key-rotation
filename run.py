#!/usr/bin/env python3
import subprocess, os, requests, shutil
from pathlib import Path
from mail import send_email


user_profile = os.environ.get('USERPROFILE')
ssh_folder = Path(f"{user_profile}\\.ssh")
keyPath = Path(f"{ssh_folder}//id_rsa")
url = "https://api.github.com/user/keys"

#backing up old ssh 
if keyPath.exists():
    shutil.copy(keyPath, Path(f"{ssh_folder}\\id_rsa_old"))

with open('./github_pat.txt', 'r') as file:
    github_pat = file.read()




try:
    subprocess.run(f'echo y | ssh-keygen -t rsa -b 4096 -f {keyPath} -N ""', check=True, shell=True)
    print("Key Generated successfully")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")


with open(f'{user_profile}\\.ssh\\id_rsa.pub', 'r') as file:
    my_ssh_key = file.read()


headers = {
    "Accept": "application/vnd.github+json",
    "Authorization":  f"token {github_pat}",
}

data = {
    "title": "ssh-rsa-besbes",  
    "key": my_ssh_key
}

getResponse = requests.get(url,headers=headers)

if getResponse.status_code == 200:
    keys = getResponse.json()
    
    matching_ids = [key["id"] for key in keys if key["title"] == data["title"]]

    for id in matching_ids:
        deleteResponse = requests.delete(f"{url}/{id}",headers=headers)

postResponse = requests.post(url, headers=headers, json=data)

if postResponse.status_code == 201:
    postResponse=postResponse.json()
    send_email(postResponse["id"])
