#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time
import dateparser
import datetime
import json
import os
from s4gpy.s4gpy import S4GAPI

vod_user=os.environ["VOD_USER"]
vod_password=os.environ["VOD_PASSWORD"]
# Retreive login/pwd from API

session = requests.Session()
payload = {"client_id": "dashboard-vuejs", "grant_type": "password", "scope": "dashboard-vuejs", "username": vod_user,
           "password": vod_password}
resp = session.post('https://auth.vod-prime.space/auth/realms/discoverability/protocol/openid-connect/token',
                    data=payload)
access_token = resp.json()["access_token"]

headers = {"Authorization": f"Bearer {access_token}"}
credentials = session.get("https://credentials.vod-prime.space/providers/netflix", headers=headers).json()
single_credentials_link = credentials["links"][0]["href"]

single_credentials = session.get(single_credentials_link, headers=headers).json()
login = single_credentials["credentials"]["login"]
password = single_credentials["credentials"]["password"]

known_netflix_id_conso_api = session.get("https://api.vod-prime.space/api/thumbnails/latest?since=01/01/1970&limit=-1", headers=headers).json()
netflix_id_conso_api=set([conso_pi["video_id"] for conso_pi in known_netflix_id_conso_api])
known_netflix_id_platform = session.get("https://platform-api.vod-prime.space/api/emns/provider/4/identifiers", headers=headers).json()
netflix_id_platform_api=set([v["identifierId"] for v in known_netflix_id_platform["data"]["identifiers"]])

unknown_video_ids=[id for id in netflix_id_conso_api if id not in netflix_id_platform_api]

#for unknown_video_id in unknown_video_ids:
#    print(f"netflix id {unknown_video_id} is unknown" )

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(options=options)
actions = ActionChains(browser)
browser.get('https://www.netflix.com/login')

elem = browser.find_element_by_id('id_userLoginId')
elem.send_keys(login + Keys.RETURN)

time.sleep(5)

elem = browser.find_element_by_id('id_password')
elem.send_keys(password + Keys.RETURN)

time.sleep(5)

elem = browser.find_element_by_class_name('profile-icon')
elem.click()

time.sleep(5)


for unknown_video_id in unknown_video_ids:

    browser.get(f'https://www.netflix.com/title/{unknown_video_id}')

    time.sleep(2)

    
    title_element=browser.find_element_by_css_selector("p.previewModal--section-header strong")
    print(f"{unknown_video_id} is {title_element.text} ")
    