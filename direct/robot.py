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

api=S4GAPI(vod_user,vod_password)
login, password = api.get_credentials_api().get_credentials("netflix")


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
for row in browser.find_elements_by_css_selector("div.row"):
    browser.execute_script("arguments[0].scrollIntoView();", row)
    start_time = row.find_element_by_css_selector("div.start-time").text
    print("content start time:"+start_time)
    parsed_date = dateparser.parse(start_time)
   
    if row.find_element_by_css_selector("div.direct-label").text == "":
        if parsed_date < now:
            parsed_date = parsed_date + datetime.timedelta(days=1)

    row.click()
    resp = api.get_conso_api().create_direct_schedule(parsed_date.timestamp(),browser.current_url.split("jbv=")[1])
    time.sleep(2)
    
    actions.send_keys(Keys.ESCAPE)
    actions.perform()

    time.sleep(1)

