# import webdriver
from selenium import webdriver

# import Alert
from selenium.webdriver.common.alert import Alert

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# get ide.geeksforgeeks.org
driver.get("https://ide.geeksforgeeks.org / tryit.php / WXYeMD9tD4")

# create alert object
alert = Alert(driver)

# get alert text
print(alert.text)

# accept the alert
alert.accept()
