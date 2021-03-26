
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




vod_user=os.getenv('VOD_USER')
vod_password=os.getenv('VOD_PASSWORD')
# Retreive login/pwd from API


api=S4GAPI(vod_user,vod_password)
login, password = api.get_credentials_api().get_credentials("netflix")



print ('Starting ...')

#DOWNLOAD .crx
result2=github_release.gh_asset_download("discoverability/discoverability","5.2.11")


#Set a Display
display = Display(visible=0, size=(1280, 720))
display.start()
print ('Display Activated')


#Options for the ChromeDriver

opt = webdriver.ChromeOptions()
caps = webdriver.DesiredCapabilities.CHROME.copy()

opt.binary_location ="/lib/chromium-browser/chromium-browser"
opt.add_argument("--no-sandbox")
opt.add_argument("--disable-gpu")
opt.add_argument("--allow-running-insecure-content")
opt.add_argument("--ignore-ssl-errors=yes")
opt.add_argument("--window-size=1280,720")
opt.add_argument("--ignore-certificate-errors")
opt.add_argument("--disable-dev-shm-usage")
opt.add_extension("./Prime-Space-Sorbonne-5.2.11-prod.crx")
opt.add_argument("--user-agent=Mozilla/5.0 (X11; CrOS armv7l 12371.89.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
caps['goog:loggingPrefs'] = { 'browser':'ALL' }



#Load the driver
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',options=opt,desired_capabilities=caps)
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
time.sleep(10)
netflix_url=driver.current_url
print ('Profile selected')



#Scraping 

round=True
watched=1
while(round):
    roundsecret=randbelow(4)
    round_secret=str(roundsecret)

    ### ICI ON SE DEPLACE GENERIQUEMENT À LA LIGNE "NOTRE SELECTION POUR [NAME_PROFILE] "
    wozx=len(driver.find_elements(By.XPATH,"//div[@data-list-context='topTen']"))>0
    while (wozx==False):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        wozx=len(driver.find_elements(By.XPATH,"//div[@data-list-context='topTen']"))>0
    #######################################################

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(5)
    element=(driver.find_element(By.XPATH,"//div[@data-list-context='topTen']/div[@class='rowContainer rowContainer_title_card']/div[@class='ptrack-container']/div[@class='rowContent slider-hover-trigger-layer']/div[@class='slider']/div[@class='sliderMask showPeek']/div[@class='sliderContent row-with-x-columns']/div[@class='slider-item slider-item-"+round_secret+"']/div[@class='title-card-container ltr-0']"))
    actions=ActionChains(driver)
    actions.click(element).perform()
    time.sleep(10)
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    element = driver.find_element(By.CSS_SELECTOR, ".primary-button > .color-primary")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".primary-button > .color-primary").click()
    time.sleep(45)
    currentUrl=driver.current_url
    newUrl=driver.current_url
    now=datetime.datetime.now()
    after_2_30_hour=now+datetime.timedelta(hours=2)
    after_2_30_hour=after_2_30_hour+datetime.timedelta(minutes=30)
    print("you are watching:")
    print(currentUrl)
    log=driver.get_log('browser')
    with open('data'+str(watched)+'.csv', 'w',encoding="utf-8", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Voici les données récupérées par le robot watcher" +str(now) ])
                    writer.writerow([""])
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
    
    while(newUrl==currentUrl and now<after_2_30_hour):
        newUrl=driver.current_url
        now=datetime.datetime.now()
        time.sleep(60)
    
    driver.get(netflix_url)
    time.sleep(10)
    print ("Scraping "+str(watched)+": OK")
    round=False
    

#Close Session
driver.close()
print ('Done')

