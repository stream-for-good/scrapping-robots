#!/usr/bin/env python3
import time
import re
import csv
import datetime
import json
import os
import github_release
import requests
from secrets import randbelow
from pyvirtualdisplay import Display
from s4gpy.s4gpy import S4GAPI


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


#UTILISER UN COMPTE AVEC MINIMUM 4 PROFILS POUR QUE LE SCRIPT FONCTIONNE


vod_user=os.getenv('VOD_USER')
vod_password=os.getenv('VOD_PASSWORD')
# Retreive login/pwd from API


api=S4GAPI(vod_user,vod_password)
login, password = api.get_credentials_api().get_credentials("netflix")


print ('Starting ...')

#DOWNLOAD .crx
result2=github_release.gh_asset_download("discoverability/discoverability","5.2.11")


#Set a Display
#display = Display(visible=0, size=(1280, 720))
#display.start()
print ('Display Activated')


#Options for the ChromeDriver

opt = webdriver.ChromeOptions()
caps = webdriver.DesiredCapabilities.CHROME.copy()

opt.add_argument("--no-sandbox")
opt.add_argument("--disable-gpu")
opt.add_argument("--allow-running-insecure-content")
opt.add_argument("--ignore-ssl-errors=yes")
opt.add_argument("--window-size=1280,720")
opt.add_argument("--ignore-certificate-errors")
opt.add_argument("--disable-dev-shm-usage")
opt.add_extension("./Prime-Space-Sorbonne-5.2.11-prod.crx")
caps['goog:loggingPrefs'] = { 'browser':'ALL' }



#Load the driver
driver = webdriver.Chrome(options=opt,desired_capabilities=caps)
print ('webdriver loaded')


#check extension situation
driver.get("chrome://extensions/?id=blkbcjgilnfbdbnfdacpffhjbeigkmgj")
driver.refresh()
time.sleep(1)
print ('extension PRIME-SPACE loaded')



driver.get("https://dashboard.vod-prime.space")
time.sleep(5)
driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys(vod_user)
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys(vod_password)
driver.find_element(By.ID, "kc-login").click()
time.sleep(5)




# Navigate to target website
driver.get('https://www.netflix.com/login')
time.sleep(10)
print ('Netflix Reached')

#Netflix Login
element=driver.find_element(By.ID, "id_userLoginId")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "id_userLoginId").send_keys(login)
driver.find_element(By.ID, "id_password").click()
driver.find_element(By.ID, "id_password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, ".login-button").click()
time.sleep(15)
print ('Netflix credentials work!')


#Select Profile
roundsecret=randbelow(5)
while (roundsecret==0):
    roundsecret=randbelow(5)
round_secret=str(roundsecret)
driver.find_element(By.CSS_SELECTOR, ".profile:nth-child("+round_secret+") .profile-icon").click()
time.sleep(20)
netflix_url=driver.current_url
print ('Profile selected')



#Scraping 



for i in range (1,40,1):
    print(i)
    row="#row-"+str(i)+" .handle"
    time.sleep(3)
    isPresent=len(driver.find_elements(By.CSS_SELECTOR, row))>0
    if isPresent==False: 
        continue
    driver.find_element(By.CSS_SELECTOR, row).click()
    time.sleep(3)
    row="#row-"+str(i)+" .handleNext"
    driver.find_element(By.CSS_SELECTOR, row).click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, row).click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, row).click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, row).click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, row).click()
    time.sleep(3)


now=datetime.datetime.now()
log=driver.get_log('browser')
print("Voici les données récupérées par le robot watcher" +str(now))
iter=0
for e in log:
    if (iter<2):
        iter+=1
        continue 
    data = re.findall(r'SPACE\](.*?)"', str(e))
    if (len(data)>0):
        timestamp = re.findall(r'console-api\'\,(.*?)\}',str(e))
        if(len(timestamp)>0):
            print(data[0]+timestamp[0])



print("you just added ~5000 thumbnails to database !")
time.sleep(2)
actions.send_keys(Keys.ESCAPE)

#Close Session
driver.close()
print ('Done')




