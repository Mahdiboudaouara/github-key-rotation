import subprocess, os, requests

user_profile = os.environ.get('USERPROFILE')
with open('./github_pat.txt', 'r') as file:
    github_pat = file.read()


url = "https://api.github.com/user/keys"


try:
    subprocess.run(f'echo y | ssh-keygen -t rsa -b 4096 -f {user_profile}\\.ssh\\my_ssh_key -N ""', check=True, shell=True)
    print("Key Generated successfully")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")



with open(f'{user_profile}\\.ssh\\my_ssh_key.pub', 'r') as file:
    my_ssh_key = file.read()


headers = {
    "Accept": "application/vnd.github+json",
    "Authorization":  f"token {github_pat}",
}

data = {
    "title": "ssh-rsa-besbes",  
    "key": my_ssh_key
}

response = requests.post(url, headers=headers, json=data)

print(response.json())


