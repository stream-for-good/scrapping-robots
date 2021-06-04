from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from crement import Lever
from bs4 import BeautifulSoup
from s4gpy.s4gpy import S4GAPI
import time
import random
import undetected_chromedriver.v2 as uc
import json
import requests
import urllib.parse

PATH = r"C:\chromedriver\90\chromedriver.exe"
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
driver = uc.Chrome(PATH, options=opt, desired_capabilities=caps)
#driver = uc.Chrome()

def YouTube_Google_Log_In(thisLogin):
    try:
        email = 0
        password = 0
        isFound = True
        laccounts = get_Google_Accounts()
        if thisLogin != "":
            for x in laccounts:
                if thisLogin in x:
                    email = x[0]
                    password = x[1]
                    isFound = False
            if isFound:
                thisLogin == 0            
        elif thisLogin == 0:
            selectTupple = laccounts[random.randrange(len(laccounts))]
            email = selectTupple[0]
            password = selectTupple[1]
        driver.find_element_by_css_selector("#end > #buttons > ytd-button-renderer > a").click()
        emailInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#identifierId")))
        emailInput.send_keys(email)
        time.sleep(0.5)
        driver.find_element_by_css_selector("#identifierNext > div > button").click()
        passwordInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")))
        time.sleep(2)
        passwordInput.send_keys(password)
        time.sleep(2)
        driver.find_element_by_css_selector("#passwordNext > div > button").click()
        time.sleep(0.5)
        #driver.find_element_by_css_selector("#yDmH0d > c-wiz > div > div > div > div.L5MEH.Bokche.ypEC4c > div.lq3Znf > div.U26fgb.O0WRkf.oG5Srb.HQ8yf.C0oVfc.Zrq4w.WIL89.k97fxb.yu6jOd.M9Bg4d.j7nIZb > span > span").click()
        driver.find_element_by_css_selector("#yDmH0d > c-wiz.yip5uc.SSPGKf > c-wiz > div > div.p9lFnc > div > div > div > div.ZRg0lb.Kn8Efe > div:nth-child(3) > div > div.yKBrKe > div > span > span").click()
        return email
    except:
        print("Error in YouTube_Google_Log_In(email)")

def YouTube_Google_Log_Out():
    try:
        currPage = driver.current_url
        home_page()
        time.sleep(2)
        driver.get(driver.current_url + "logout/")
        time.sleep(2)
        driver.get(currPage)
    except:
        print("Error in YouTube_Google_Log_Out()")
        
def YouTube_Acces_Website():
    try:
        driver.get("https://www.youtube.com/")
    except:
        print("Error in YouTube_Acces_Website()")
        
def YouTube_Accept_Cookies():
    try:
        driver.find_element_by_css_selector("#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.qqtRac > form > div.lssxud > div > button").click()
    except:
        print("Error in YouTube_Accept_Cookies()")

def YouTube_Deny_Log_In():
    try:
        driver.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/tp-yt-paper-button/yt-formatted-string").click()
        time.sleep(1)
        driver.switch_to.default_content()
    except:
        pass

def YouTube_Toggle_AutoPlay(boolean):
    try:
        if boolean == 'True':
            #Regarder si l'auto play est false pour le mettre en true
            isPressed = driver.find_element_by_css_selector("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button:nth-child(1) > div > div")
            if isPressed.get_attribute("aria-checked") == "false":
                isPressed.click()
        else:
            #Regarder si l'auto play est true pour le mettre en false
            isPressed = driver.find_element_by_css_selector("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button:nth-child(1) > div > div")
            if isPressed.get_attribute("aria-checked") == "true":
                isPressed.click()
    except:
        print("Error in YouTube_Toggle_AutoPlay(boolean)")

def YouTube_Get_Video_Id_From_Url(url):
    try:
        if url == "https://www.youtube.com/":
            return ''
        return url.split("=")[1].split("&")[0]
    except:
        print("Error in YouTube_Get_Video_Id_From_Url(url)")
        return ''

def YouTube_Music_No_Thanks():
    try:
        driver.find_element_by_css_selector("ytd-button-renderer#dismiss-button > a > tp-yt-paper-button > yt-formatted-string").click()
        driver.switch_to.default_content()
    except:
        pass

def get_Google_Accounts():
    api = S4GAPI("pierre.rambert@hotmail.fr","Pj1101vC")
    return api.get_credentials_api().get_credentials_all("youtube")

def home_page():
    try:
        driver.find_element_by_css_selector("#logo > a > div > #logo-icon").click()
    except:
        print("Error in home_page()")

def scrollDown():
    try:
        driver.execute_script("window.scrollBy(0,1500);")
    except:
        print("Error in scrollDown()")

def find_caption():
    try:
        driver.find_element_by_xpath("//div[3]/div/ytd-menu-renderer/yt-icon-button/button/yt-icon").click()
        driver.find_elements_by_css_selector(".ytd-menu-popup-renderer > ytd-menu-service-item-renderer")[0].click()
        caption = "".join([e.get_attribute('innerHTML') for e in driver.find_elements_by_css_selector("div.cue-group > div > div")])
        return caption
    except:
        print("Error in find_caption()")
        return ''

def find_video():
    try:
        l = []
        #for x in driver.find_elements_by_css_selector("#thumbnail"):
        for x in driver.find_elements_by_css_selector("#dismissible > ytd-thumbnail > a#thumbnail"):
            url = x.get_attribute("href")
            if url == None:
                continue
            idVideo = YouTube_Get_Video_Id_From_Url(url)
            l.append(idVideo)
        return l
    except:
        print("Error in find_video")

def select_video(n=0):
    try:
        currUrl = driver.current_url
        driver.switch_to.default_content()
        if n > 15:
            scrollDown()
        if currUrl == "https://www.youtube.com/":
            # From homepage
    #            print("homepage")
            driver.find_elements_by_css_selector("#contents > ytd-rich-item-renderer")[n].click()
        elif "watch?v=" in currUrl:
            # From a watching video
    #            print("video")
            driver.find_elements_by_css_selector("#items > ytd-compact-video-renderer")[n].click()
        elif "results?search_query=" in currUrl:
            # From a search
    #            print("search")
            driver.find_elements_by_css_selector("#contents > ytd-video-renderer > #dismissible > ytd-thumbnail")[n].click()
        else:
            # From a video tab from a channel
    #            print("channel")
            driver.find_elements_by_css_selector("#items > ytd-grid-video-renderer")[n].click()
    except IndexError:
        m = int(n/2)
        select_video(m)


def find_video_length_in_seconds():
    try :
        strTime = driver.find_element_by_css_selector("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div.ytp-time-display.notranslate > span.ytp-time-duration").text
        listTime = strTime.split(":")[::-1]
        res = 0
        for i in range(len(listTime)):
            res += int(listTime[i]) * (60**i)
        return res
    except :
        print("Error in find_video_length_in_seconds()")

def watch_the_video_for(n=0):
    try:
        time.sleep(n)
    except:
        print("Error in watch_the_video_for()")

def dislike_video():
    try:
        driver.find_element_by_css_selector(".ytd-video-primary-info-renderer > #top-level-buttons > .style-scope:nth-child(2) #button > #button > .style-scope").click()
    except:
        print("Error in dislike_video()")

def like_video():
    try:
        driver.find_element_by_css_selector(".ytd-video-primary-info-renderer > #top-level-buttons > .style-scope:nth-child(1) #button > #button > .style-scope").click()
    except:
        print("Error in like_video()")

def go_to_channel():
    try:
        driver.find_element_by_css_selector("#top-row > ytd-video-owner-renderer > a").click()
        videoTab = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#tabsContent > tp-yt-paper-tab")))
        time.sleep(1)
        videoTab[1].click()
    except:
        print("Error in go_to_channel()")

def search_with_url(url):
    try:
        driver.get(url)
    except:
        print("Error in search_with_url()")

def search_bar(text):
    try:
        # Query
        driver.find_element_by_css_selector("#search-input > #search").clear()
        driver.find_element_by_css_selector("#search-input > #search").send_keys(text)
        driver.find_element_by_css_selector("#search-icon-legacy").click()
    except:
        print("Error in search_bar()")

def robot(file):
    urlForDB = "test.netops.fr"
    thisSession = str(int(time.time()))
    requests.post("https://"+ urlForDB + "/api/session/new",headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"id":thisSession})
    lets_toggle = False
    isLogedIn = False
    actionNumber = Lever()
    currentAction = 7
    time.sleep(2)
    listVideos = find_video()
    print("Where's the list of all the videos on this page (*~▽~) :")
    for x in listVideos:
        print("\t"+str(x))
    a = requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "videos":listVideos, "position":actionNumber.get()})
    actionNumber.incr()
    for x in file:
        YouTube_Deny_Log_In()
        YouTube_Music_No_Thanks()
        if x["action"] == 'settings':
            currentAction = 1
            print("Let's change some settings ⊂((・▽・))⊃")
            if "autoPlay" in x["options"]:
                print("Auto Play is set to : " + str(x["options"]["autoPlay"]) + " ヾ(*´∀｀*)ﾉ")
                requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "position":actionNumber.get()})
                actionNumber.incr()
                YouTube_Toggle_AutoPlay(x["options"]["autoPlay"])
            if "login" in x["options"]:
                print("We'll soon log in (=^▽^=)")
                logEmail = YouTube_Google_Log_In(x["options"]["login"])
                requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "email":logEmail, "position":actionNumber.get()})
                actionNumber.incr()
                
                isLogedIn = True
            if "logout" in x["options"]:
                print("We're login out ! °˖✧◝(^▿^)◜✧˖°")
                requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "email":"log out", "position":actionNumber.get()})
                actionNumber.incr()
                YouTube_Google_Log_Out()
                isLogedIn = False
        elif x["action"] == 'search':
            print("Let's search for : " + str(x["toSearch"]) + " ー( ´ ▽ ` )ﾉ")
            currentAction = 2
            searchedWords = str(x["toSearch"])
            search_bar(searchedWords)
            time.sleep(2)
            listVideos = find_video()
            print("Where's the list of all the videos on this page (*~▽~) :")
            for x in listVideos:
                print("\t"+str(x))
            requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "videos":listVideos, "key_word" : searchedWords, "position":actionNumber.get()})
            actionNumber.incr()
        elif x["action"] == 'watch':
            currentAction = 3
            index = -1
            videoLever = True
            if "url" in x:
                print("Let's watch a video from an URL o(^▽^)o")
                search_with_url(x["url"])
            elif "index" in x :
                print("Let's watch the video number : " + str(x["index"]) + " on this page ヾ(＾∇＾)")
                select_video(x["index"])
                index = x["index"]
            else:
                print("Let's watch the video number : 1 on this page ヾ(＾∇＾)")
                select_video()
                index = 1
            time.sleep(2)
            currentVideo = driver.current_url
            time.sleep(2)
            listVideos = find_video()
            print("Where's the list of all the videos on this page (*~▽~) :")
            for x in listVideos:
                print("\t"+str(x))
            requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"currentVideo":YouTube_Get_Video_Id_From_Url(currentVideo),"action":currentAction, "videos":listVideos, "index":index, "position":actionNumber.get()})
            actionNumber.incr()
            if "watchContext" in x:
                if x["watchContext"]["stopsAt"] == "never":
                    print("We're going to watch it 'til the end ! (*⌒∇⌒*)")
                    watch_the_video_for(find_video_length_in_seconds())
                else :
                    print("We're going to watch it for : " + str(x["watchContext"]["stopsAt"]) + "seconds (*⌒∇⌒*)")
                    watch_the_video_for(int(x["watchContext"]["stopsAt"]))
                if isLogedIn:
                    if "social" in x["watchContext"]:
                        #Envoye à Sylvain les likes ou dislikes
                        if x["watchContext"]["social"] == 'like':
                            print("I like it !! (ᗒᗊᗕ)")
                            currentAction = 4
                            like_video()
                            time.sleep(2)
                            requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction,"position":actionNumber.get()})
                            actionNumber.incr()
                        else :
                            print("It wasn't great thought ... (๑꒪▿꒪)*")
                            currentAction = 5
                            dislike_video()
                            time.sleep(2)
                            requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction,"position":actionNumber.get()})
                            actionNumber.incr()
        elif x["action"] == 'goToChannel':
            print("Intresting ! Let's visit this channel ~ヾ(＾∇＾)")
            currentAction = 6
            go_to_channel()
            time.sleep(2)
            listVideos = find_video()
            print("Where's the list of all the videos on this page (*~▽~) :")
            for x in listVideos:
                print("\t"+str(x))
            requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "videos":listVideos, "position":actionNumber.get()})
            actionNumber.incr()
        elif x["action"] == 'home':
            print("Let's go back to homepage (＾▽＾)")
            currentAction = 7
            home_page()
            time.sleep(2)
            listVideos = find_video()
            print("Where's the list of all the videos on this page (*~▽~) :")
            for x in listVideos:
                print("\t"+str(x))
            requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "videos":listVideos, "position":actionNumber.get()})
            actionNumber.incr()
        time.sleep(2)
    time.sleep(10)
    print("Fiouf, it's the end of our journey, hope you like it （⌒▽⌒ゞ")
    print("Cya soon !")
    driver.quit()

def launch():
    print("Hi, I'm Pybot, and I'm going to take you on a YouTube journey ( ´ ▽ ` )ﾉ")
    YouTube_Acces_Website()
    time.sleep(2)
    YouTube_Accept_Cookies()
    time.sleep(2)
    YouTube_Deny_Log_In()
    print("We're on YouTube homepage ! (　＾∇＾)")
    print("Just let me grab my map and see where we go from here ⊂((・▽・))⊃")
    file = ''
#    with open('bot.json') as jfile:
#        file = json.load(jfile)["0"]
    url = "https://scriptgenyoutube.miage.dev/generate"
    #Recuperer le json dans le payload avec un request a un front end
    payload = json.dumps({
      "type": "conspi",
      "watchNext": "15",
      "watchFromURL": "0",
      "watchFromHome": "10",
      "search": "conspi",
      "watchFromSearch": "5",
      "watchFromChannel": "5",
      "watchRecommended": "15",
      "stopsAt": "5",
      "social": "like",
      "interactionPercent": "50",
      "order": [
        "home",
        "next",
        "search",
        "channel",
        "recommended"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    time.sleep(1)
    afile = response.text
    file = json.loads(afile)["actions"]
    print(r"We're all set, let's go ! \(*≧∇≦*)/")
    time.sleep(1)
    robot(file)





launch()