#!/usr/bin/env python3
import logging
import sys
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


logging.basicConfig(stream=sys.stderr, level=logging.INFO)

logging.info('Jackdaws love my big sphinx of quartz.')

logging.info ('Starting ...')

#Set a Display
display = Display(visible=0, size=(1280, 720))
display.start()
logging.info ('Display Activated')


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
opt.add_extension("./extension_1_35_2_0.crx")
caps['goog:loggingPrefs'] = { 'browser':'ALL' }


#Load the driver
driver = webdriver.Chrome(options=opt,desired_capabilities=caps)

# Navigate to target website
driver.get(f"https://www.youtube.com/watch?v={os.environ['VIDEO_ID']}")
time.sleep(2)

actions = ActionChains(driver)
actions.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()


time.sleep(5)
#Netflix Login
element=driver.find_elements(By.CSS_SELECTOR, "#info button[aria-label='More actions']")[0]
element.click()
time.sleep(2)


element=driver.find_elements(By.CSS_SELECTOR, ".ytd-menu-popup-renderer > ytd-menu-service-item-renderer")[0]
time.sleep(2)
element.click()
time.sleep(5)
caption= "".join([e.get_attribute('innerHTML') for e in driver.find_elements(By.CSS_SELECTOR, "div.cue-group > div > div")])


driver.close()
print(caption)




