#!/usr/bin/env python3
import time
import re
import csv
import datetime
import json
import os
import github_release
import requests
import docker



#MADE WITH LOVE BY THE L3 MIAGE 2020-2021



f=list(open('envfile'))
VOD_USER=(f[0].split('\n'))[0]
VOD_PASSWORD=(f[1].split('\n'))[0]
credentials=[VOD_USER,VOD_PASSWORD]


client=docker.from_env()


while (True):
    time.sleep(15)
    
    response_get=requests.get("http://127.0.0.1:8080/api/pendingtasks")
    
    
    if (response_get.status_code!=200):
        print("Aucune Tâche à accomplir")
        continue
    
    response=response_get.json()
    print(response_get)
    print(response)
    
    
    text=''
    id=response['id']
    loop=response['loop']
    robot=response['robot']['label']
    print("Tâche numéro "+str(int(id)))
    
    if (robot=="thumbnails"):
        while(loop!=0):
            loop-=1
            container=client.containers.run("wallseven/thumbnails",detach=True,environment=credentials,name="container-thumbnails",remove=True)
            for line in container.logs(stream=True):
                text+=str(line)
                
    elif (robot=="watcher"):
        while(loop!=0):
            loop-=1
            container=client.containers.run("wallseven/watcher",detach=True,environment=credentials,name="container-thumbnails",remove=True)
            for line in container.logs(stream=True):
                text+=str(line)
                
    elif (robot=="direct"):
        while(loop!=0):
            loop-=1
            container=client.containers.run("wallseven/direct",detach=True,environment=credentials,name="container-thumbnails",remove=True)
            for line in container.logs(stream=True):
                text+=str(line)
                
    elif (robot=="netflixid"):
        while(loop!=0):
            loop-=1
            container=client.containers.run("wallseven/netfixid",detach=True,environment=credentials,name="container-thumbnails",remove=True)
            for line in container.logs(stream=True):
                text+=str(line)
                
                
                
    
    data={
        "log":text,
        "task": int(id)
        }
    
    
    response2=requests.post("http://127.0.0.1:8080/api/data",json=data)
    
    print(response2)
    print(response2.json())
        
        





