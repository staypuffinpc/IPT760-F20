## PURPOSE: demonstrate how to use selenium to imitate a user and interact with a website

# import required libs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #to add delays
import getpass
from selenium.webdriver.common.action_chains import ActionChains
# we need these next 3 methods in order to wait until the presence of a particular element exists
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# set up/obtain initial vars
user = "pjrich"
password = getpass.getpass("gmail password?")

#create new driver object
driver = webdriver.Firefox()
driver.get("https://gmail.com")

#get the username/email field and fill it out
user_input = driver.find_element_by_id("identifierId")
user_input.send_keys(user)
next_btn = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
next_btn.click()

##note that google prevents you from using automated software to send emails now
