#!/usr/bin/env python3

#Ce script contient l'ensemble des fonctions qui permet de naviguer automatiquement et de manière controlée sur le web
#Particulièrement, il est utilisé pour naviguer et scrapper YouTube
#Voici la liste des fonctions :
#    YouTube_Google_Log_In(thisLogin)
#    YouTube_Google_Log_Out()
#    YouTube_Acces_Website()
#    YouTube_Accept_Cookies()
#    YouTube_Deny_Log_In()
#    YouTube_Toggle_AutoPlay()
#    YouTube_Get_Video_Id_From_Url(url)
#    YouTube_Music_No_Thanks()
#    home_page()
#    scrollDown()
#    find_caption()
#    find_video()
#    select_video(n=0)
#    find_video_length_in_seconds()
#    watch_the_video_for(n=0)
#    dislike_video()
#    like_video()
#    go_to_channel()
#    search_with_url(url)
#    search_bar(text)
#    robot(file)
#    test_select_video(n=0)
#    test_find_video()
#    test_go_to_channel()
#    test_search_bar(text)
#    test_like_video()
#    test_dislike_video()
#    test_find_video_length_in_seconds()
#    test_scroll_down()
#    test_YouTube_Toggle_AutoPlay()
#    test_YouTube_Google_Log_Out()
#    test_YouTube_Google_Log_In(email, password)
#    test_YouTube_Acces_Website()
#    
#Voici la liste du code qui n'est pas dans des fonctions :
#    Ligne 70 à 107
#    Ligne 544 à 556


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



#Cette première partie, morcellée, pas encore dans un fonction, permet d'instancier le webdriver, qui est utilisé pour naviguer de manière automatique et controlé par un programme sur le web
#La deuxième partie est ligne 502
#Important :
#    PATH correspond au cheminoù est stocké le webdriver
#driver est la variable qui contient le webdriver, et qui va donc être manipulé pour naviguer sur le web

PATH = r"C:\chromedriver.exe"
# driver = webdriver.Chrome(PATH)

#options = uc.ChromeOptions()
#options.add_extension("./extension_1_35_2_0.crx")
#driver = uc.Chrome()



#Options for the ChromeDriver

opt = webdriver.ChromeOptions()
caps = webdriver.DesiredCapabilities.CHROME.copy()

#opt.add_argument("--no-sandbox")
opt.add_argument("--disable-gpu")
opt.add_argument("--allow-running-insecure-content")
opt.add_argument("--ignore-ssl-errors=yes")
opt.add_argument("--window-size=1280,720")
opt.add_argument("--ignore-certificate-errors")
opt.add_argument("--disable-dev-shm-usage")
#opt.add_extension("./extension_1_35_2_0.crx")
#opt.add_extension("extension_1_35_2_0.crx")
caps['goog:loggingPrefs'] = { 'browser':'ALL' }


#Load the driver
#driver = webdriver.Chrome(PATH, options=opt, desired_capabilities=caps)
driver = uc.Chrome(PATH, options=opt, desired_capabilities=caps)








#Paramètres :
#    String  email       l'email du compte avec lequel on veut se loger
#    String  password    le mot de passe associé à l'email en paramètres
#Cette fonction permet de s'identifier avec un email et un mot de passe donnée à partir de la page d'acceuil de YouTube
#Fonctionne depuis n'importe quel endroit du site
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
    except:
        print("Error in YouTube_Google_Log_In(email, password)")

#Cette fonction permet de se déconnecter depuis la page d'accueil de YouTube
#Fonctionne depuis n'importe quel endroit du site
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


#Cette fonction permet d'accéder à la page d'accueil de YouTube
def YouTube_Acces_Website():
    try:
        driver.get("https://www.youtube.com/")
    except:
        print("Error in YouTube_Acces_Website()")

#Cette fonction permet d'accepter les cookies
#En effet, sur Google, lorsqu'un nouvel utilisateur souhaite bénéficer des services de Google, il est obligé d'accepter les cookies
#Comme chaque lancement du script agit comme un nouvel utilisateur, il est nécessaire de les accepter à chaque fois
def YouTube_Accept_Cookies():
    try:
        driver.find_element_by_css_selector("#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.qqtRac > form > div.lssxud > div > button").click()
    except:
        print("Error in YouTube_Accept_Cookies()")

#Cette fonction permet de ne pas s'identifier lorsqu'une fenêtre pop up s'ouvre dans le navigateur
#Elle apparait la première fois que l'on souhaite utiliser un service Google
def YouTube_Deny_Log_In():
    try:
        driver.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/tp-yt-paper-button/yt-formatted-string").click()
        time.sleep(1)
        driver.switch_to.default_content()
    except:
        print("Error in YouTube_Deny_Log_In()")

#Cette fonction permet de cliquer sur le bouton auto-play
#Auto-play est un bouton qui agit comme un toggle ; étant activé par défaut, un nombre impair de cliques empêche la lecture automatique de vidéos.
#Un nombre pair active la lecture automatique de vidéos
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


#Paramètre :
#    String  url l'url d'une vidéo YouTube
#Return :
#    String      l'id de l'url
#Error :
#    String  ''  String vide
#Permet de récupérer l'id d'un url de vidéo YouTube passé en paramètre.
#Retourne un String vide s'il rencontre une erreur
def YouTube_Get_Video_Id_From_Url(url):
    try:
        if url == "https://www.youtube.com/":
            return ''
        return url.split("=")[1].split("&")[0]
    except:
        print("Error in YouTube_Get_Video_Id_From_Url(url)")
        return ''

#Cette fonction permet de décliner l'offre de YouTube Music
def YouTube_Music_No_Thanks():
    try:
        driver.find_element_by_css_selector("ytd-button-renderer#dismiss-button > a > tp-yt-paper-button > yt-formatted-string").click()
    except:
        print("Error in YouTube_Music_No_Thanks()")

#Cette fonction retourne une liste des comptes qui peuvent etres utilise pour se connecter a un compte Google
def get_Google_Accounts():
    api = S4GAPI("pierre.rambert@hotmail.fr","Pj1101vC")
    return api.get_credentials_api().get_credentials_all("youtube")

#Cette fonction permet de revenir à la page d'accueil de YouTube
#Fonctionne depuis n'importe où sur le site
def home_page():
    try:
        driver.find_element_by_css_selector("#logo > a > div > #logo-icon").click()
    except:
        print("Error in home_page()")

#Cette fonction permet de scroller vers le bas
#L'objectif est de charger plus de vidéos
def scrollDown():
    try:
        driver.execute_script("window.scrollBy(0,1500);")
    except:
        print("Error in scrollDown()")

#FONCTION A DISPARAITRE
#Return :
#    String  caption Un String contenant toutes les captions de la vidéo en cours
#Cette fonction permet de récupérer tous les sous-titres d'une vidéo depuis la page YouTube de cette vidéo
def find_caption():
    try:
        driver.find_element_by_xpath("//div[3]/div/ytd-menu-renderer/yt-icon-button/button/yt-icon").click()
        driver.find_elements_by_css_selector(".ytd-menu-popup-renderer > ytd-menu-service-item-renderer")[0].click()
        caption = "".join([e.get_attribute('innerHTML') for e in driver.find_elements_by_css_selector("div.cue-group > div > div")])
        return caption
    except:
        print("Error in find_caption()")
        return ''

#Return :
#    List    l   Retourne une liste contenant tous les id des vidéos chargées sur la page actuelle
#Cette fonction retourne une liste contenant tous les id des vidéos chargées sur la page actuelle
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

#Paramètre :
#    int n   Numéro de la vidéo à visionner
#Permet de visionner la n-ième vidéo sur la page. Fonctionne sur la page d'accueil, après une recherche dans l'outil de recherche YouTube, depuis une vidéo ou depuis l'onglet vidéo d'une chaine YouTube.
#Si aucun paramètre n'est donné, c'est la toute première vidéo qui est visionnée
def select_video(n=0):
    # Ajouter une clause IndexError
    currUrl = driver.current_url
    if currUrl == "https://www.youtube.com/":
        # From homepage
        print("homepage")
        driver.find_elements_by_css_selector("#contents > ytd-rich-item-renderer")[n].click()
    elif "watch?v=" in currUrl:
        # From a watching video
        print("video")
        driver.find_elements_by_css_selector("#items > ytd-compact-video-renderer")[n].click()
    elif "results?search_query=" in currUrl:
        # From a search
        print("search")
        driver.find_elements_by_css_selector("#contents > ytd-video-renderer > #dismissible > ytd-thumbnail")[n].click()
    else:
        # From a video tab from a channel
        print("channel")
        driver.find_elements_by_css_selector("#items > ytd-grid-video-renderer")[n].click()
#    try:
#        currUrl = driver.current_url
#        if currUrl == "https://www.youtube.com/":
#            # From homepage
#            print("homepage")
#            driver.find_elements_by_css_selector("#contents > ytd-rich-item-renderer")[n].click()
#        elif "watch?v=" in currUrl:
#            # From a watching video
#            print("video")
#            driver.find_elements_by_css_selector("#items > ytd-compact-video-renderer")[n].click()
#        elif "results?search_query=" in currUrl:
#            # From a search
#            print("search")
#            driver.find_elements_by_css_selector("#contents > ytd-video-renderer > #dismissible > ytd-thumbnail")[n].click()
#        else:
#            # From a video tab from a channel
#            print("channel")
#            driver.find_elements_by_css_selector("#items > ytd-grid-video-renderer")[n].click()
#    except:
#        print("Error in select_video() / " + driver.current_url + " / " + str(n))


#Return :
#    int res Durée de la vidéo en secondes
#Trouve la durée de la vidéo sur la page web, convertit le temps trouvé en secondes et le retourne
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


#Paramètre :
#    int n   Nombres de secondes de visionnage de la vidéo
#Prends en paramètre un nombre de secondes et hatle le programme pendant cette durée.
#Permet de simuler le visionnage d'une vidéo.
#Si aucun paramètre n'est donné, alors la fonction n'halte pas le programme
def watch_the_video_for(n=0):
    try:
        time.sleep(n)
    except:
        print("Error in watch_the_video_for()")

#Cette fonction permet de dislike une vidéo.
#Cette fonction n'a un effet que si le robot s'est "log in" avec un compte Google
def dislike_video():
    try:
        driver.find_element_by_css_selector(".ytd-video-primary-info-renderer > #top-level-buttons > .style-scope:nth-child(2) #button > #button > .style-scope").click()
    except:
        print("Error in dislike_video()")

#Cette fonction permet de like une vidéo.
#Cette fonction n'a un effet que si le robot s'est "log in" avec un compte Google
def like_video():
    try:
        driver.find_element_by_css_selector(".ytd-video-primary-info-renderer > #top-level-buttons > .style-scope:nth-child(1) #button > #button > .style-scope").click()
    except:
        print("Error in like_video()")

#Cette fonction permet depuis la page de visonnage d'une vidéo d'accéder à la chaine qui a uploader cette vidéo
#Cette fonction, une fois sur la chaine, va automatiquement sur l'onglet "Vidéos"
def go_to_channel():
    try:
        driver.find_element_by_css_selector("#top-row > ytd-video-owner-renderer > a").click()
        videoTab = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#tabsContent > tp-yt-paper-tab")))
        time.sleep(1)
        videoTab[1].click()
    except:
        print("Error in go_to_channel()")

#Paramètres :
#    String  url L'url d'une vidéo YouTube
#Cette fonction de charger la page d'une vidéo YouTube depuis son url
def search_with_url(url):
    try:
        driver.get(url)
    except:
        print("Error in search_with_url()")

#Paramètre :
#    String  text    Texte correspondant à la recherhce YouTube
#Permet d'entrer des mots-clefs, du texte dans l'outil de recherche YouTube depuis n'importe quel endroit de YouTube.
#YouTube gardant en mémoire la recherche précédante, cette fonction efface tous ce qui à été écris et entre le String passé en paramètre et exécute la recherche
def search_bar(text):
    try:
        # Query
        driver.find_element_by_css_selector("#search-input > #search").clear()
        driver.find_element_by_css_selector("#search-input > #search").send_keys(text)
        driver.find_element_by_css_selector("#search-icon-legacy").click()
    except:
        print("Error in search_bar()")


def t():
    thisSession = str(int(time.time()))
    print(thisSession)
    urlForDB = "test.netops.fr"
    a = requests.post("https://"+ urlForDB + "/api/session/new",headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"id":thisSession})
    print(a)
    actionNumber = Lever()
    currentAction = 7
    print(currentAction)
    time.sleep(2)
    listVideos = find_video()
    print(listVideos)
    a = requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "videos":listVideos})
    print(a)

#Paramètre :
#    List    x   Une liste contenant des dictionnaires, correspondant aux actions que doit exécute le script
#Cette fonction permet de lire une liste et d'exécuter les instructions stockées dans des dictionnaires.
#Cette fonction correspond au "robot", qui va utiliser la quasi totalité des autres fonctions pour fonctionner.
#Elle envoye à des points clefs des requêtes à la DataBase
#Variables :
#    String          thisSession     Converti le nombre de secondes depuis l'Epoch en String. Permet d'assurer un ordre entre les différentes sessions
#    Boolean         toggle_auto_play_bool   Permet d'assurer le bon fonctionnement de YouTube_Toggle_AutoPlay()
#    Object          actionNumber        Permet d'avoir un objet qui assure l'incrémentation de l'index de chaque action, pour garder dans la BdD l'odre de déroulement des actions faites par le robot
#    int         currentAction       Permet de savoir quelle est l'action actuellement réalisée par le robot. Sera envoyée dans la requête à la BdD
def robot(file):
    urlForDB = "test.netops.fr"
    thisSession = str(int(time.time()))
    a = requests.post("https://"+ urlForDB + "/api/session/new",headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"id":thisSession})
    print(a)
    lets_toggle = False
    isLogedIn = False
    actionNumber = Lever()
    currentAction = 7
    time.sleep(2)
    listVideos = find_video()
    a = requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "videos":listVideos, "position":actionNumber})
    print(a)
    actionNumber.incr()
    for x in file:
        YouTube_Deny_Log_In()
        if x["action"] == 'settings':
            #Envoyer à Sylvain les settings modifés
            currentAction = 1
            if "autoPlay" in x["options"]:
                requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "position":actionNumber})
                actionNumber.incr()
                YouTube_Toggle_AutoPlay(x["options"]["autoPlay"])
            if "login" in x["options"]:
                YouTube_Google_Log_In(x["options"]["login"])
                requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "email":x["options"]["login"], "position":actionNumber})
                actionNumber.incr()
                #TODO : Recuperer le mdp avec le login et se login avec
                isLogedIn = True
            if "logout" in x["options"]:
                requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "email":"log out", "position":actionNumber})
                actionNumber.incr()
                YouTube_Google_Log_Out()
                isLogedIn = False
        elif x["action"] == 'search':
            currentAction = 2
            search_bar(x["toSearch"])
            time.sleep(2)
            listVideos = find_video()
            requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "videos":listVideos, "key_word" : x["toSearch"], "position":actionNumber})
            actionNumber.incr()
        elif x["action"] == 'watch':
            #Envoyer à Sylvain l'id de la vidéo et les id de toutes les vidéos
            currentAction = 3
            index = -1
            videoLever = True
            if "url" in x:
                search_with_url(x["url"])
            elif "index" in x :
                select_video(x["index"])
                index = x["index"]
            currentVideo = driver.current_url
            time.sleep(2)
            listVideos = find_video()
            requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"currentVideo":YouTube_Get_Video_Id_From_Url(currentVideo),"action":currentAction, "videos":listVideos, "index":index, "position":actionNumber})
            actionNumber.incr()
            if "watchContext" in x:
                if x["watchContext"]["stopsAt"] == "never":
                    watch_the_video_for(find_video_length_in_seconds())
                else :
                    watch_the_video_for(int(x["watchContext"]["stopsAt"]))
                if isLogedIn:
                    if "social" in x["watchContext"]:
                        #Envoye à Sylvain les likes ou dislikes
                        if x["watchContext"]["social"] == 'like':
                            currentAction = 4
                            time.sleep(2)
                            like_video()
                            requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction,"position":actionNumber})
                            actionNumber.incr()
                        else :
                            currentAction = 5
                            dislike_video()
                            requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "position":actionNumber})
                            actionNumber.incr()
        elif x["action"] == 'goToChannel':
            currentAction = 6
            go_to_channel()
            time.sleep(2)
            listVideos = find_video()
            requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "videos":listVideos, "position":actionNumber})
            actionNumber.incr()
        elif x["action"] == 'home':
            currentAction = 7
            home_page()
            listVideos = find_video()
            requests.post("https://"+ urlForDB + "/api/log/new", headers={"accept":"application/ld+json","Content-Type": "application/ld+json"}, json={"session":thisSession,"action":currentAction, "videos":listVideos, "position":actionNumber})
            actionNumber.incr()
        time.sleep(1)
    time.sleep(10)
    driver.quit()




#Les fonctions qui suivent sont censé tester toutes les fonctions du robot (celles qui peuvent être automatiquement testés).
#L'idée sous-jacente est de récupérer le code html actuel de la page, un "screenshot", et de vérifier si la fonction réalise effectivement ce pourquoi elle à été appelé avec des "select" intelligent à l'aide de BeautifulSoup.
#Nommage : "test_" + NomDeLaFonctionTesté
#Return :
#    Boolean     Retourne si le test à été validé ou non
def test_select_video(n=0):
#    S'assurer que l'url ouverte par le robot correspond bien à la n-ième url dans le code de la page enregistré
    soup = BeautifulSoup(driver.find_element_by_css_selector("html").get_attribute("outerHTML"), 'html.parser')
    currUrl = driver.current_url
    strUrl = ''
    if currUrl == "https://www.youtube.com/":
        strUrl = str(soup.select('#contents > ytd-rich-item-renderer > div > ytd-rich-grid-media > div#dismissible > ytd-thumbnail > a')[n])
    elif "watch?v=" in currUrl:
        strUrl = str(soup.select('#items > ytd-compact-video-renderer > div > ytd-thumbnail > a')[n])
    elif "results?search_query=" in currUrl:
        strUrl = str(soup.select('#contents > ytd-video-renderer > div#dismissible > ytd-thumbnail > a')[n])
    else:
        strUrl = str(soup.select("#items > ytd-grid-video-renderer > #dismissible > ytd-thumbnail > a")[n])
    strUrl = strUrl[:strUrl.index(">")]
    url = strUrl[strUrl.index('href="')+6:]
    url = url[:url.index('"')]
    select_video()
    return 'https://www.youtube.com' + url == driver.current_url

def test_find_video():
#    S'assurer que toutes les vidéos de la page ont bien été chargés dans la liste
    soup = BeautifulSoup(driver.find_element_by_css_selector("html").get_attribute("outerHTML"), 'html.parser')
    mySet = set()
    for x in soup.select("#dismissible > ytd-thumbnail > a#thumbnail"):
        x = str(x)
        url = x[x.index('href="')+6:]
        url = url[:x.index('"')]
        mySet.add(url)
    return mySet == set(find_video)

def test_go_to_channel():
#    S'assurer que la chaine ouverte par le robot correspond bien à la chaine de la page d'avant
    soup = BeautifulSoup(driver.find_element_by_css_selector("html").get_attribute("outerHTML"), 'html.parser')
    strName = str(soup.select("#text > a")[0])
    strName = strName[strName.index('>')+1:strName.index('<',2)]
    go_to_channel()
    soup = BeautifulSoup(driver.find_element_by_css_selector("html").get_attribute("outerHTML"), 'html.parser')
    strName2 = str(soup.select("ytd-channel-name > div > div > yt-formatted-string > a")[0])
    strName2 = strName2[strName2.index('>')+1:strName2.index('<',2)]
    return strName == strName2

def test_search_bar(text):
#    S'assurer que l'url coresponde bien aux mots tapés, avec correction URL Special encoding : https://secure.n-able.com/webhelp/NC_9-1-0_SO_en/Content/SA_docs/API_Level_Integration/API_Integration_URLEncoding.html
    inUrl = urllib.parse.quote_plus(query)
    search_bar(text)
    time.sleep(1)
    return 'https://www.youtube.com/results?search_query=' + inUrl == driver.current_url

def test_like_video():
#    Vérifier que le driver.find_element_by_css_selector(".ytd-video-primary-info-renderer > #top-level-buttons > .style-scope:nth-child(1) #button > #button").get_attribute("aria-pressed") == True
    soup = BeautifulSoup(driver.find_element_by_css_selector("html").get_attribute("outerHTML"), 'html.parser')
    return 'aria-pressed="false"' in str(soup.select(".ytd-video-primary-info-renderer > #top-level-buttons > .style-scope:nth-child(1) #button > #button"))

def test_dislike_video():
#    Vérifier que le driver.find_element_by_css_selector(".ytd-video-primary-info-renderer > #top-level-buttons > .style-scope:nth-child(2) #button > #button").get_attribute("aria-pressed") == False
    soup = BeautifulSoup(driver.find_element_by_css_selector("html").get_attribute("outerHTML"), 'html.parser')
    return 'aria-pressed="false"' in str(soup.select(".ytd-video-primary-info-renderer > #top-level-buttons > .style-scope:nth-child(2) #button > #button"))

def test_find_video_length_in_seconds():
#    Vérifier que dans le code de la page enregistré, la longueure convertie correspond bien

    soup = BeautifulSoup(driver.find_element_by_css_selector("html").get_attribute("outerHTML"), 'html.parser')
    strTime = soup.select("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div.ytp-time-display.notranslate > span.ytp-time-duration")
    strTime = strTime[strTime.index('>')+1:strTime.index('<',2)]
    listTime = strTime.split(":")[::-1]
    res = 0
    for i in range(len(listTime)):
        res += int(listTime[i]) * (60**i)
    return res == find_video_length_in_seconds()

def test_scroll_down():
    strSoup = str(BeautifulSoup(driver.find_element_by_css_selector("html").get_attribute("outerHTML"), 'html.parser'))
    scrollDown()
    strSoup2 = str(BeautifulSoup(driver.find_element_by_css_selector("html").get_attribute("outerHTML"), 'html.parser'))
    return strSoup2 > strSoup

def test_YouTube_Toggle_AutoPlay():
#    Vérifier que driver.find_element_by_css_selector("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button:nth-child(1) > div > div").get_attribute("href") est différent entre le code de la page enregistré et le code actuel
    soup = BeautifulSoup(driver.find_element_by_css_selector("html").get_attribute("outerHTML"), 'html.parser')
    resStr = soup.select('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button:nth-child(1) > div > div')
    YouTube_Toggle_AutoPlay()
    soup = BeautifulSoup(driver.find_element_by_css_selector("html").get_attribute("outerHTML"), 'html.parser')
    resStr2 = soup.select('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button:nth-child(1) > div > div')
    return resStr != resStr2

def test_YouTube_Google_Log_Out():
#    Vérfier que len(driver.find_element_by_css_selector("yt-formatted-string#text.style-scope.ytd-button-renderer.style-suggestive.size-small")) == 1
    soup = BeautifulSoup(driver.find_element_by_css_selector("html").get_attribute("outerHTML"), 'html.parser')
    return len(soup.select("yt-formatted-string#text.style-scope.ytd-button-renderer.style-suggestive.size-small")) == 1

def test_YouTube_Google_Log_In(email, password):
#    Vérifier que len(driver.find_element_by_css_selector("yt-formatted-string#text.style-scope.ytd-button-renderer.style-suggestive.size-small")) == 0
    soup = BeautifulSoup(driver.find_element_by_css_selector("html").get_attribute("outerHTML"), 'html.parser')
    return len(soup.select("yt-formatted-string#text.style-scope.ytd-button-renderer.style-suggestive.size-small")) == 0

def test_YouTube_Acces_Website():
#    Vérifier que driver.current_url = 'https://www.youtube.com/'
    YouTube_Accept_Cookies()
    time.sleep(1)
    YouTube_Deny_Log_In()
    time.sleep(2)
    return driver == 'https://www.youtube.com/'



#Cette deuxième partie pas encore dans une fonction s'exécute dès que le programme est exécuté.
#Il permet de demander au webdriver d'arriver à la page d'accueil de YouTube, d'ouvrir la liste d'instruction donnée par le fichier "bot.json", et d'exécuter ces instructions

def launch():
    YouTube_Acces_Website()
    time.sleep(2)
    YouTube_Accept_Cookies()
    time.sleep(2)
    YouTube_Deny_Log_In()
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
    robot(file)




#launch()
#---------------------------------------------

#Verifier sur un serveur
#FAIRE DES TESTS SUR select_video() !!
#Pour la mise sur serveur :
#    Faire en sorte de pouvoir recuperer le json de lecture
#    Avoir des logs d'erreurs
#Envoyer la duree de visionnage de la video en secondes
#Refaire un script qui est joli visuellement