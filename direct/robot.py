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

browser.get('https://www.netflix.com/direct/schedule')

time.sleep(5)

now = datetime.datetime.now()
payload = []
for row in browser.find_elements_by_css_selector("div.row"):
    browser.execute_script("arguments[0].scrollIntoView();", row)
    start_time = row.find_element_by_css_selector("div.start-time").text
    print("content start time:"+start_time)
    parsed_date = dateparser.parse(start_time)
   
    if row.find_element_by_css_selector("div.direct-label").text == "":
        if parsed_date < now:
            parsed_date = parsed_date + datetime.timedelta(days=1)

    row.click()
    row_data = {
        "airing_time": parsed_date.timestamp(),
        "video_id": browser.current_url.split("jbv=")[1]
    }
    payload.append(row_data)
    resp = session.post('https://conso-api.vod-prime.space/direct', json=[row_data])
    time.sleep(2)
    
    actions.send_keys(Keys.ESCAPE)
    actions.perform()

    time.sleep(1)

