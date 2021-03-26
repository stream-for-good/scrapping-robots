#!/usr/bin/env python3
import time
import re
import csv
import datetime
import json
import os
import requests



#NETFLIX QUERY
robots_collection=["watcher","thumbnails","direct","netflixid"]
for i in range (len(robots_collection)):
    print(robots_collection[i])
    data={
        "label":robots_collection[i],
        "category": "netflix"
        }
 
    response=requests.post("http://127.0.0.1:8080/api/setRobot",json=data)
    print(response)
    time.sleep(2)
