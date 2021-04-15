from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flags import Flag
from crement import Lever
import time
import random
import os
from googleapiclient.discovery import build
import googleapiclient.errors

myAPIYouTubeKey = 'AIzaSyBEkQeSVr0S0kh0OAj5PR4EexFbb-e6fSk'
myClientId = '708274977995-a6olhaq2oqf661uulukfl1tgl80m2pc3.apps.googleusercontent.com'
myClientSecret = 'SyUtUZBKTO2DeSASooc9c1Zv'
mySecretFileName = 'client_secret_708274977995-a6olhaq2oqf661uulukfl1tgl80m2pc3.apps.googleusercontent.com'


myFlag = Flag()
myLever = Lever()


PATH = "C:\chromedriver.exe"
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
driver = webdriver.Chrome(PATH,options=opt,desired_capabilities=caps)






'''
PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
'''






'''
driver = webdriver.Firefox(executable_path=r"C:\geckodriver.exe")
'''
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

#driver.find_elements_by_id("channel-name")[0].

'''
How to scroll down
https://selenium-python.readthedocs.io/faq.html?highlight=is#how-to-scroll-down-to-the-bottom-of-a-page
'''

def foo():
    print("foo")

def bar():
    print("bar")
    
def zoo():
    print("zoo")

l = {1:foo, 2:bar, 3:zoo}
for x in l.keys():
    l[x]()


'''
TODO

search_bar(text)       -- Validate
search_with_url(url)   -- Validate
go_to_channel()        -- Validate
#select_video()
    Watching a video :
        All the videos are in the div 'id="secondary-inner"' --> div 'id="related"' --> div 'id="contents"'
        Inside the div 'id="contents"', it only contains all the videos. Find them in a list with find_elements...
        Once selecterd, div 'id="dismissible"' --> a 'id="thumbnail"'
    From a research :
        All the videos are in the div 'id="container"' --> div 'id="primary"' --> div 'id="contents"' --> div 'id="contents"'
        Inside the div 'id="contents"', it contains 'ytd-video-renderer' objects with 'class="style-scope ytd-item-section-renderer"'
        CAREFUL, it doesn't only contains videos
        Once selecterd, div 'id="dismissible"' --> a 'id="thumbnail"'
    Homepage :
        div 'id="primary"' --> div 'id="contents"' // 2 possibilities
            1_ It's a video with 'ytd-rich-item-renderer' object, 'class="style-scope ytd-rich-grid-renderer"' type, in which
                div 'id="content"' --> div 'id="contents"' --> div 'id="dismissible"' --> a 'id="thumbnail"'
            2_ It's a 'ytd-rich-section-renderer' object, that has div 'id="content"' --> div 'id="dismissible"' --> div 'id="contents"'
                It contains the list of the videos, 'ytd-rich-item-renderer' object with 'class="style-scope ytd-rich-shelf-renderer"' with div 'id="contents"' --> div 'id="dismissible"' --> a 'id="thumbnail"'
like_the_video()       -- Validate
dislike_the_video()    -- Validate
watch_the_video_for() --> time.sleep(random.randint(0,"max video length")
'''

def z():
    YouTube_Acces_Website()
    time.sleep(0.5)
    YouTube_Accept_Cookies()
    time.sleep(0.5)
    YouTube_Deny_Log_In()


def find_video():
    try:
        l = []
        d = dict()
        # Retourner une liste
        i = 0
        # Peut récuperer des None, mais récupère tout
        for x in driver.find_elements_by_css_selector("#thumbnail"):
            print(x.get_attribute("href"))
            l.append(x.get_attribute("href"))
            i += 1
        print(i)
        #return d[driver.current_url] = l
    except:
        print("Error in find_video")
            

def YouTube_Toggle_AutoPlay():
    try:
        driver.find_element_by_css_selector("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button:nth-child(1) > div > div").click()
    except:
        pass

def Google_Accept_Cookies():
    try:
        driver.find_element_by_css_selector('#zV9nZe > div').click()
    except:
        pass

def YouTube_Accept_Cookies():
    try:
        driver.find_element_by_xpath("/html/body/div/c-wiz/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button").click()
    except:
        pass

def select_video(n=1):
    # Preferer cliquer sur le thumbnail
    '''
    if len(driver.find_elements_by_xpath("//ytd-toggle-button-renderer/a/paper-button/yt-formatted-string")) != 0:
        # From a research
        print("research")
        driver.find_elements_by_xpath('//div[@id="content"]/ytd-page-manager[@id="page-manager"]/ytd-search/div[@id="container"]/ytd-two-column-search-results-renderer/div[@id="primary"]/ytd-section-list-renderer/div[@id="contents"]/ytd-item-section-renderer/div[@id="contents"]/ytd-video-renderer')[n].click()
    elif len(driver.find_elements_by_id("ytp-caption-window-container")) != 0:
        # From a watching video
        print("video")
        driver.find_elements_by_xpath('//div[@id="secondary-inner"]/div[@id="related"]/ytd-watch-next-secondary-results-renderer/div[@id="items"]/ytd-compact-video-renderer')[n].click()
    #elif driver.current_url == "https://www.youtube.com/":
    else:
        # From homepage
        # Tous ce qui est dans des sections est inselectionnable
        print("homepage")
        driver.find_elements_by_xpath('//ytd-app/div[@id="content"]/ytd-page-manager[@id="page-manager"]/ytd-browse/ytd-two-column-browse-results-renderer/div[@id="primary"]/ytd-rich-grid-renderer/div[@id="contents"]/ytd-rich-item-renderer')[n].click()
    '''
    try:
        if driver.current_url == "https://www.youtube.com/":
            # From homepage
            # TODO : Tous ce qui est dans des sections est inselectionnable
            print("homepage")
            driver.find_elements_by_xpath('//ytd-app/div[@id="content"]/ytd-page-manager[@id="page-manager"]/ytd-browse/ytd-two-column-browse-results-renderer/div[@id="primary"]/ytd-rich-grid-renderer/div[@id="contents"]/ytd-rich-item-renderer')[n].click()
        elif len(driver.find_elements_by_xpath('//div[@id="player-container-inner"]/div[@id="player-container"]/ytd-player/div[@id="container"]/div[@id="movie_player"]')) != 0:
            # From a watching video
            print("video")
            driver.find_elements_by_xpath('//div[@id="primary-inner"]/div[@id="related"]/ytd-watch-next-secondary-results-renderer/div[@id="items"]/ytd-compact-video-renderer')[n].click()
        elif len(driver.find_elements_by_css_selector("#tabsContent > tp-yt-paper-tab.style-scope.ytd-c4-tabbed-header-renderer.iron-selected > div")) != 0:
            driver.find_element_by_css_selector("#tabsContent > tp-yt-paper-tab:nth-child(4) > div").click()
            driver.find_elements_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer")[n].click()
        else:
            # From a research
            print("research")
            driver.find_elements_by_xpath('//div[@id="content"]/ytd-page-manager[@id="page-manager"]/ytd-search/div[@id="container"]/ytd-two-column-search-results-renderer/div[@id="primary"]/ytd-section-list-renderer/div[@id="contents"]/ytd-item-section-renderer/div[@id="contents"]/ytd-video-renderer')[n].click()

    except (NoSuchElementException, ElementNotInteractableException):
        if myLever.get() == 0:
            select_video(n+1)
            myLever.incr()
        else:
            print("Error in select_video()")
    finally:
        myLever.setLever(0)
        
        
    


def watch_the_video_for(n=0):
    try:
        time.sleep(n)
    except:
        print("Error in watch_the_video_for()")
    
def dislike_video():
    try:
        driver.find_element_by_xpath("//ytd-toggle-button-renderer[2]/a/yt-icon-button/button/yt-icon").click()
    except:
        print("Error in dislike_video()")
    
def like_video():
    try:
        driver.find_element_by_xpath("//ytd-toggle-button-renderer/a/yt-icon-button/button/yt-icon").click()
    except:
        print("Error in like_video()")

def go_to_channel():
    try:
        driver.find_element_by_xpath("//ytd-video-owner-renderer/a/yt-img-shadow/img").click()
    except:
        print("Error in go_to_channel()")
    """
    myUrl = driver.find_elements_by_id("channel-name")[0].find_element_by_class_name("yt-simple-endpoint").get_attribute("href")
    search_with_url(myUrl)
    """

def search_with_url(url):
    try:
        driver.get(url)
    except:
        print("Error in search_with_url()")

def search_bar(text):
    try:
        driver.find_element_by_id("search").send_keys(text)
        driver.find_element_by_id("search-icon-legacy").click()
    except:
        print("Error in search_bar()")


def YouTube_FireFox_Log_In():
    # From homepage
    driver.find_element_by_css_selector("ytd-button-renderer.style-scope:nth-child(3) > a:nth-child(1) > paper-button:nth-child(1) > yt-formatted-string:nth-child(2)").click()

def YouTube_FireFox_Accept_Cookies():
    driver.find_element_by_css_selector("div.VfPpkd-RLmnJb").click()

def YouTube_Find_First_Video_Link():
    driver.get("https://www.youtube.com/")
    time.sleep(1)
    driver.find_element_by_xpath("//yt-button-renderer/a/paper-button/yt-formatted-string").click()
    time.sleep(1)
    driver.switch_to.frame("iframe")
    driver.find_element_by_css_selector("div#introAgreeButton").click()
    time.sleep(1)
    driver.switch_to.default_content()
    print(driver.find_element_by_xpath("//a[@id='video-title-link']").get_attribute("href"))

def YouTube_Deny_Log_In():
    # Probably not working
    # driver.find_element_by_xpath("//yt-button-renderer/a/paper-button/yt-formatted-string").click()
    driver.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/tp-yt-paper-button/yt-formatted-string").click()
    time.sleep(1)
    driver.switch_to.default_content()

def YouTube_Acces_Website():
    try:
        driver.get("https://www.youtube.com/")
    except:
        print("Error in YouTube_Acces_Website()")

def YouTube_Deny_Log_In_And_Validate_General_Condition():
    try:
        driver.find_element_by_xpath("//yt-button-renderer/a/paper-button/yt-formatted-string").click()
        time.sleep(1)
        driver.switch_to.frame("iframe")
        driver.find_element_by_css_selector("div#introAgreeButton").click()
        time.sleep(1)
        driver.switch_to.default_content()
    except:
        print("Error in YouTube_Deny_Log_In_And_Validate_General_Condition()")
  
def YouTube_Get_First_Video_Link():
    # You need to be on YouTube home page to call
    print(driver.find_element_by_xpath("//a[@id='video-title-link']").get_attribute("href"))

def YouTube_Click_On_First_Video_From_Home_Page():
    driver.find_element_by_xpath("//a[@id='video-title-link']").click()
  
  
def YouTube_Get_Video_Title_From_Url(url):
    # You need to have validate the 2 pop up before using it
    driver.get(url)
    print(driver.find_element_by_xpath("//h1[@class='title style-scope ytd-video-primary-info-renderer']").text)

def YouTube_Get_Video_Title_From_Page():
    print(driver.find_element_by_xpath("//h1[@class='title style-scope ytd-video-primary-info-renderer']").text)
    
def YouTube_Get_Current_Url():
    try:
        return driver.current_url
    except:
        print("Error in YouTube_Get_Current_Url()")
    
def YouTube_Get_Current_Video_Id():
    print(driver.current_url.split("=")[1].split("&")[0])

def YouTube_Get_Video_Id_From_Url(url):
    print(url.split("=")[1].split("&")[0])
    

## Changer la fonction pour qu'elle prenne en paramètre l'ID de la vidéo
def YouTube_Get_Comments_From_Video_Id():
    # Ne fonctionne pas ; peuit-être faut-il être owner de la vidéo pour pouvoir récupérer les commentaires
    with build('youtube','v3',developerKey='AIzaSyDQpIOHBpjzWLy2iZCWJHbCNAmXi_Fcyt0') as youtube_API:
        myRequest = youtube_API.comments().list(
            part='id',
            id='WUvTyaaNkzM'
        )
        myResponse = myRequest.execute()
        print(type(myResponse))
        print(myResponse)
        print(myResponse['items'])

def YouTube_Get_Captions_From_Video_Id():
    # Ajouter les autorisations pour récupérer les captions
    with build('youtube','v3',developerKey='AIzaSyDQpIOHBpjzWLy2iZCWJHbCNAmXi_Fcyt0') as youtube_API:
        myRequest = youtube_API.captions().download(
            id='WUvTyaaNkzM',
        )
        myResponse = myRequest.execute()
        print(type(myResponse))
        print(myResponse)

#YouTube_Get_Captions_From_Video_Id()

def a():
    driver.get("https://www.youtube.com/")
    time.sleep(1)
    driver.find_element_by_xpath("//yt-button-renderer/a/paper-button/yt-formatted-string").click()
    time.sleep(1)
    driver.switch_to.frame("iframe")
    driver.find_element_by_css_selector("div#introAgreeButton").click()
    time.sleep(1)
    driver.switch_to.default_content()
    driver.find_element_by_xpath("//a[@id='video-title-link']").click()



def lastChance():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
    request = youtube.captions().list(part="snippet",videoId="M7FIvfx5J10")
    response = request.execute()
    print(myResponse)



'''
# Flag 0
myFlag.plantFlag()

driver.get("https://www.youtube.com/")

# Flag 1
myFlag.plantFlag()

time.sleep(1)
driver.find_element_by_xpath("//yt-button-renderer/a/paper-button/yt-formatted-string").click()
# Flag 2
myFlag.plantFlag()
time.sleep(1)

#driver.find_element_by_xpath("//div[@id='introAgreeButton']/span/span").click()



#driver.switch_to_frame("iframe")
driver.switch_to.frame("iframe")
driver.find_element_by_css_selector("div#introAgreeButton").click()




# Flag 3
myFlag.plantFlag()
time.sleep(1)

driver.switch_to.default_content()
#print(driver.page_source)
#driver.find_element_by_xpath("//div[@id='introAgreeButton']/span/span").click()
print(driver.find_element_by_xpath("//a[@id='video-title-link']").get_attribute("href"))
'''

'''
button
text
label-container
thumbnail
'''

'''
try:
    a = driver.find_elements_by_xpath("//div[@id='thumbnail']")
    print(a)
    a.click()
    
    print("Guacamole")
finally:
    # Flag 2
    myFlag.plantFlag()





'''





'''
# Flag 0
myFlag.plantFlag()



# Flag 1
myFlag.plantFlag()

driver.get("https://www.youtube.com/")

# Flag 2
myFlag.plantFlag()
time.sleep(7)

"""
try:
    validate = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//paper-button[@id='button' and @aria-label='Non merci'"))
    )
    print(validate.text)
    accept = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "introAgreeButton"))
    )
    accept.click()
    
finally:
    # Flag 3
    myFlag.plantFlag()
    
"""
try:
    firstVid = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "yt-simple-endpoint inline-block style-scope ytd-thumbnail"))
    )
    print(firstVid)
    print(firstVid.find_element_by_xpath('//a[contains(@href,"href")]'))
finally:
    # Flag 4
    myFlag.plantFlag()
#    driver.quit()
    
    
    
    
    
    
    
    
    
    
NB = """
search = driver.find_element_by_id("search")
search.send_keys("Coronavirus")
search.send_keys(Keys.RETURN)

driver.page_source
"""
'''

