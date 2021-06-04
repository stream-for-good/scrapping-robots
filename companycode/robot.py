from s4gpy.s4gpy import S4GAPI
from s4gpy.api.companyapi import CompanyAPI
from s4gpy.s4gsession import S4GSession
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import requests
import json
import time
import urllib
import re
import config

api=S4GAPI(config.user,config.password)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(options=options)

# i = j =0
ttcode_list=[]
colist_api = [company.company_id for company in api.get_company_api().get_companies()]

#Get all ttcode form the API
with urllib.request.urlopen("https://platform-api.vod-prime.space/api/emns/provider/4/identifiers") as url:
    json_data = json.loads(url.read().decode())
for i in range(len(json_data['data']['identifiers'])) :
    ttcode_list.append((json_data['data']['identifiers'][i]['imdbId']))

time.sleep(2)

#Exclude content already registered in db
for content in api.get_company_api().get_contents():
    if content.content_id in ttcode_list :
        print("In DB: "+ content.content_id)
        ttcode_list.remove(content.content_id)

for i in range(len(json_data['data']['identifiers'])) : 
    company_name_for_content=[]
    try :
        browser.get("https://www.imdb.com/title/"+ ttcode_list[i] +"/companycredits")
        search = browser.find_element_by_xpath("//h4[@id='production']/following-sibling::ul").text
        print(search)
        search = re.sub("[\(\[].*?[\)\]]", "", search).split("\n")
        print(search)
        for j in range(len(search)):
            continue_company_link = browser.find_element_by_partial_link_text(search[j].rstrip()).get_attribute('href')
            if continue_company_link == "https://www.imdb.com/title/"+ttcode_list[i]+"/?ref_=ttco_co_tt" :
                continue_company_link = browser.find_elements_by_partial_link_text(search[j].rstrip())[1].get_attribute('href')
               
            company_link_regex = re.search("company\/([a-z0-9\-]+)\&?",continue_company_link, 2)
            print(company_link_regex[1]+ " " +search[j].rstrip())

            if company_link_regex[1] not in colist_api :
                api.get_company_api().push_company(company_link_regex[1],name=search[j].rstrip(),link=continue_company_link)
                company_name_for_content.append(search[j].rstrip())
                colist_api.append(company_link_regex[1])

        api.get_company_api().push_content(ttcode_list[i],company_name_for_content)

    except NoSuchElementException :
        print("No company credits for "+ ttcode_list[i] )

#Check
for company in api.get_company_api().get_companies():
    print(f"company code {company.company_id} is {company.company().name}")
for content in api.get_company_api().get_contents():
    for company in content.content().companies():
        print(f"content {content.content_id} is produced by {company.company_id}")

browser.quit()