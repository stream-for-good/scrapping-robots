#!/usr/bin/env python3

from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display


import requests
import time
import github_release
import json
import os
display=Display(visible=0,size=(800,600))
display.start()



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

#DOWNLOAD .crx
result2=github_release.gh_asset_download("discoverability/discoverability","5.2.10")




options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument("--allow-running-insecure-content")
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-gpu")
options.add_argument('--disable-dev-shm-usage')
options.add_extension("./Prime-Space-Sorbonne-5.2.10-prod.crx")
browser = webdriver.Chrome(options=options)
actions = ActionChains(browser)



browser.get("chrome://extensions/?id=blkbcjgilnfbdbnfdacpffhjbeigkmgj")
time.sleep(2)
browser.save_screenshot('SHOT1.png')
time.sleep(2)
browser.refresh()
print("extension prime-space Loaded!")


browser.get("https://dashboard.vod-prime.space")
time.sleep(10)
browser.save_screenshot('SeleniumChromiumTest0.png')

browser.find_element(By.ID, "username").click()
browser.find_element(By.ID, "username").send_keys(vod_user)
browser.find_element(By.ID, "password").click()
browser.find_element(By.ID, "password").send_keys(vod_password)
browser.find_element(By.ID, "kc-login").click()
time.sleep(5)

print("vod-prime.space logged")


browser.get('https://www.netflix.com/login')
elem = browser.find_element_by_id('id_userLoginId')
elem.send_keys(login + Keys.RETURN)
time.sleep(5)
elem = browser.find_element_by_id('id_password')
elem.send_keys(password + Keys.RETURN)
time.sleep(10)
elem=browser.find_element(By.CSS_SELECTOR, ".profile:nth-child(1) .profile-icon")
elem.click()
time.sleep(5)
print("Netflix Reached and credentials worked")

for i in range (1,30,1):
    print(i)
    row="#row-"+str(i)+" .handle"
    time.sleep(1)
    isPresent=len(browser.find_elements(By.CSS_SELECTOR, row))>0
    if isPresent==False: 
        continue
    browser.find_element(By.CSS_SELECTOR, row).click()
    time.sleep(3)
    row="#row-"+str(i)+" .handleNext"
    browser.find_element(By.CSS_SELECTOR, row).click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, row).click()
    time.sleep(2)



print("you just added ~750 thumbnails to database !")
time.sleep(2)
actions.send_keys(Keys.ESCAPE)
actions.perform()

time.sleep(1)

