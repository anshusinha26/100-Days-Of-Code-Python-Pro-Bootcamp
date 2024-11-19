# ------------------------- MODULES ------------------------- #
# imported webdriver class from selenium module
from selenium import webdriver

# imported service class from selenium.webdriver.chrome module
from selenium.webdriver.chrome.service import Service

# imported By class from selenium.webdriver.common.by module
from selenium.webdriver.common.by import By

# imported Keys class from selenium.webdriver.common.keys module
from selenium.webdriver.common.keys import Keys

# imported time module
import time

import os
from dotenv import load_dotenv
load_dotenv()

# ------------------------- CONSTANTS ------------------------- #
# variable to store the path of the chromedriver
CHROME_DRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')

TWITTER_EMAIL = os.getenv('TWITTER_EMAIL')
TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')

# variable to store the promised speeds
PROMISED_DOWN = 30
PROMISED_UP = 30

"""this class is used to get the internet speed and tweet at the internet provider"""
class InternetSpeedTwitterComplaintBot:
    """this method initializes the driver object and the attributes to store the net speed"""
    def __init__(self):
        # created driver object to open the chrome browser
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))

        # attributes to store the net speed
        self.down = 0
        self.up = 0

    """this method is used to tweet at the internet provider"""
    def tweetAtProvider(self):
        # opened the website
        self.driver.get("https://x.com/login")

        # time to wait for the website to load
        time.sleep(5)

        # filled the email
        self.email = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
        self.email.send_keys(TWITTER_EMAIL)
        self.email.send_keys(Keys.ENTER)

        # time to wait for the website to load
        time.sleep(5)

        # # filled the username
        # self.username = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        # self.username.send_keys(TWITTER_USERNAME)
        # self.username.send_keys(Keys.ENTER)
        #
        # # time to wait for the website to load
        # time.sleep(5)

        # filled the password
        self.password = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        self.password.send_keys(TWITTER_PASSWORD)
        self.password.send_keys(Keys.ENTER)

        # time to wait for the website to load
        time.sleep(5)

        # filled the tweet
        self.tweetMsg = self.driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-block")
        self.tweetMsg.send_keys(f"Hey Jio, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")

        # time to wait for the website to load
        time.sleep(15)

        # clicked on the tweet button
        self.tweetButton = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
        self.tweetButton.click()

        # time to wait for the website to load
        time.sleep(5)

        # closed the browser
        self.driver.quit()

    """this method gets the internet speed"""
    def getInternetSpeed(self):
        # opened the website
        self.driver.get("https://www.speedtest.net/")

        # time to wait for the website to load
        time.sleep(5)

        # clicked on the cookie close button
        self.closeCookieButton = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[2]/div[1]/div/button")
        self.closeCookieButton.click()
        
        # time to wait for the website to load
        time.sleep(5)

        # clicked on the go button
        self.go = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        self.go.click()

        # time to wait for the website to load
        time.sleep(30)

        # attribute to store the download speed
        self.down = float(self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text)

        # time to wait for the website to load
        time.sleep(10)

        # attribute to store the upload speed
        self.up = float(self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text)