from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import requests
import json
import time
import urllib
import re

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(options=options)
i=j=0
ttcode_list=[]
ttcode_company={}
ttcode_company_bis={}
regex = re.compile(".*?\((.*?)\)")

#Get all ttcode form the API
with urllib.request.urlopen("https://platform-api.vod-prime.space/api/emns/provider/4/identifiers") as url:
    json_data = json.loads(url.read().decode())

for i in range(len(json_data['data']['identifiers'])) :
    ttcode_list.append((json_data['data']['identifiers'][i]['imdbId']))

time.sleep(2)

# for i in range(len(json_data['data']['identifiers'])) :
for i in range(3) : # Analyse 3 - Uncoment uppon for total list
    try :
        browser.get("https://www.imdb.com/title/"+ ttcode_list[i] +"/companycredits")
        search = browser.find_element_by_xpath("//h4[@id='production']/following-sibling::ul").text
        search = re.sub("[\(\[].*?[\)\]]", "", search).split("\n")
        for j in range(len(search)):
            search[j] = search[j].rstrip()
            
        ttcode_company[i] = {'imdb_id' : ttcode_list[i], 'companies' : search }

    except NoSuchElementException :
        print("No company credits for "+ ttcode_list[i] )
    


json_out = json.dumps(ttcode_company, indent=4)
print(json_out)







browser.quit()