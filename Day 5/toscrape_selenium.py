### PURPOSE: Demonstrate different ways of interacting with a website using selenium
## selenium documentation: https://selenium-python.readthedocs.io/installation.html

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

## create a new driver
driver = webdriver.Firefox()
## wait at least 10 seconds for an element to load
driver.implicitly_wait(10)

## go to scrolling page
driver.get("http://quotes.toscrape.com/scroll")

#get all of the quotes on the page
quotes = driver.find_elements_by_class_name("quote")
print(f"There are {len(quotes)} quotes on this page.")
time.sleep(3) #wait a few seconds

#let's scroll the web page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)

#and run the quotes again
new_quotes = driver.find_elements_by_class_name("quote")
quotes.extend(new_quotes)
print(f"There are {len(quotes)} unique quotes now.")

#repeat as necessary
