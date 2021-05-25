#!/usr/bin/env python3
import argparse
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

#CLI parsing
parser = argparse.ArgumentParser(description='Launch the youtube scrapping robot')
parser.add_argument('configuration', metavar='C', type=str, help='a string containing the json configuration')
args = parser.parse_args()


logging.basicConfig(stream=sys.stderr, level=logging.INFO)


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
caps['goog:loggingPrefs'] = { 'browser':'ALL' }


#Load the driver
driver = webdriver.Chrome(options=opt,desired_capabilities=caps)
print(f"****{args.configuration}")
response=requests.post("https://scriptgenyoutube.miage.dev/generate",json=json.loads(args.configuration))
response_text=json.dumps(response.json())
logging.info(response_text)
print(response_text) # return stuff to stdout for logging purposed through rabbitmq
