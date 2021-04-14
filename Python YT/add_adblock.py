from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

PATH = "C:\chromedriver\chromedriver.exe"
#driver = webdriver.Chrome(PATH)
"""
capabilities = {
  'browserName': 'chrome',
  'chromeOptions':  {
    'useAutomationExtension': False,
    'forceDevToolsScreenshot': True,
    'args': ['--start-maximized', '--disable-infobars']
  }
}
driver = webdriver.Chrome(desired_capabilities=capabilities, executable_path=PATH)
"""

options = webdriver.ChromeOptions()
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=PATH)


def add_block():
    driver.get(r"https://chrome.google.com/webstore/detail/adblock-plus-free-ad-bloc/cfhdojbkjhnklbpkdaibdccddilifddb")
    time.sleep(2)
    driver.find_element_by_xpath('//html/body/div[@class="F-ia-k S-ph S-Rc-qa"]/div[@class="h-F-f-k F-f-k"]/div/div/div[@class="e-f-o"]/div[@class="h-e-f-Ra-c e-f-oh-Md-zb-k"]/div[@class="dd-Va g-c-wb g-eg-ua-Uc-c-za g-c-Oc-td-jb-oa g-c"]').click()
    time.sleep(2)
    alert = Alert(driver)
    print(alert.text)

def Google_login(email, password):
    driver.find_element_by_css_selector('#gb > div > div.gb_Ue > a').click()
    driver.find_element_by_css_selector("#identifierId").send_keys(email)
    driver.find_element_by_css_selector("#identifierNext > div > button > div.VfPpkd-RLmnJb").click()
    driver.find_element_by_css_selector("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input").send_keys(password)
    driver.find_element_by_css_selector("#passwordNext > div > button > div.VfPpkd-RLmnJb").click()
    
    
    
    
    
    
    
    
    