# ---------------- MODULES ---------------- #
# imported webdriver class from selenium module
from selenium import webdriver

# imported service class from selenium module
from selenium.webdriver.chrome.service import Service

# imported By class from selenium module
from selenium.webdriver.common.by import By

# # imported Keys class from selenium module
# from selenium.webdriver.common.keys import Keys

# imported time module
import time

# imported random module
import random

import os
from dotenv import load_dotenv
load_dotenv()


# ---------------- WORKING WITH SELENIUM DRIVER ---------------- #
# variable to store chrome diver path
chromeDriverPath = os.getenv('CHROMEDRIVER_PATH')

# created a driver object
driver = webdriver.Chrome(service=Service(chromeDriverPath))


# ---------------- DAY48: AUTOMATED COOKIE CLICKER ---------------- #
# get method to launch the URL
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# variable to store the cookie clicker URL  
cookie = driver.find_element(By.ID, "cookie")

# variable to store the count per second
cps = driver.find_element(By.CSS_SELECTOR, "#cps")

"""function to buy items"""
def buyItems():
    # get all the store items
    items = driver.find_elements(By.CSS_SELECTOR, "#store div:not(.grayed) b")

    # list to store the store items prices
    itemsPrices = [float(item.text.split("-")[1].split()[0].replace(",", "")) for item in items if item.text != ""]

    # variable to store the max item price index
    maxItemPriceIndex = itemsPrices.index(max(itemsPrices))

    # click on the item
    items[maxItemPriceIndex].click()

# variable to store the timeout
timeout = time.time() + 5

# variable to store the total time
totalTime = time.time() + 30


"""loop to click the cookie and buy the items"""
while totalTime >= time.time():
    cookie.click()
    if time.time() >= timeout:
        buyItems()
        timeout = time.time() + 5

# print the count per second
print(cps.text)

# quit the browser
driver.quit()









##########################################################################################################################################################










# ---------------- SCRAPPING DATA FROM AMAZON ---------------- #
# # get method to launch the URL
# driver.get("https://www.amazon.in/Logitech-Master-Advanced-Wireless-Mouse/dp/B084TFH4BN/?_encoding=UTF8&pd_rd_w=denFQ&content-id=amzn1.sym.b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_p=b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_r=A0H30T6P9D47K9AKFJ5Z&pd_rd_wg=7RE1e&pd_rd_r=3ba085bc-a147-47d9-b384-ab88776e0db2&ref_=pd_gw_ci_mcx_mr_hp_atf_m")

# # variable to store the price
# price = driver.find_element(By.CLASS_NAME, "a-price-whole").text

# # print the price
# print(price)

# # variable to store the link
# helpLink = driver.find_element(By.XPATH, "//*[@id='navFooter']/div[1]/div/div[7]/ul/li[6]/a").get_attribute("href")

# # print the help link
# print(helpLink)


# ---------------- SCRAPPING DATA FROM PYTHON.ORG ---------------- #
# # get method to launch the URL
# driver.get("https://www.python.org")

# eventDict = {}

# for i in range(1, 6):
#     # find the element by xpath
#     eventDate = driver.find_element(By.XPATH, f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i}]/time").text

#     # find the element by xpath
#     eventName = driver.find_element(By.XPATH, f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i}]/a").text

#     # add the event date and event name to the dictionary
#     eventDict[i] = {"time": eventDate, "name": eventName}

# # print the event dictionary
# print(eventDict)


# ---------------- SCRAPPING DATA FROM WIKIPEDIA ---------------- #
# # get method to launch the URL
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# # variable to store the search term
# articlesNum = driver.find_element(By.XPATH, "//*[@id='articlecount']/a[1]")

# # print the number of articles
# print(articlesNum)

# # click on the element
# articlesNum.click()

# # variable to store the view history link
# viewHistory = driver.find_element(By.LINK_TEXT, "View history")

# # click on the element 
# viewHistory.click()

# # variable to store the search bar
# searchBar = driver.find_element(By.NAME, "search")

# # send keys to the search bar
# searchBar.send_keys("Python")

# # send enter key to the search bar
# searchBar.send_keys(Keys.ENTER)