#!/bin/python3
import os

config = '''
{
    "registry-mirrors":[
        "http://hub-mirror.c.163.com",
        "https://registry.docker-cn.com"
    ],
    "data-root":"/var/lib/docker"
}
'''

os.system('sudo apt-get update')
os.system('sudo apt install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common')
os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
os.system('sudo apt-key fingerprint 0EBFCD88')
os.system('sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"')
os.system('sudo apt-get update')
os.system('sudo apt-get install docker-ce docker-ce-cli containerd.io')

os.system("sudo echo '{}' > /etc/docker/daemon.json".format(config))

os.system('sudo groupadd docker')
os.system('sudo usermod -aG docker yangyixuan')