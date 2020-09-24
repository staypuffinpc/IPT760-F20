### PURPOSE: To demonstrate how to scrape info from the web using beautiful soup
## Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
## import libraries
import requests
from bs4 import BeautifulSoup
import re

# First, get a web page
url = "https://scholar.google.com/citations?user=JFv6vGMAAAAJ&hl=en"
req = requests.get(url)
scholar_soup = BeautifulSoup(req.content, "lxml")

# print(scholar_soup.prettify())
name = scholar_soup.find("div",attrs={"id":"gsc_prf_in"})
print(f"This scholar is named {name.text}.")

#just get the first link
first_link = scholar_soup.find("a")
print(first_link)

#get all links
all_links = scholar_soup.find_all("a")
print(f"There are {len(all_links)} links on this google scholar profile page.")
print(all_links[9])

#get publication publication links
pubs = scholar_soup.find_all("a",attrs={"class":"gsc_a_at"})
for pub in pubs:
    print(f"{pub.text}\n")



#### ----------- BYU NEWS ------------- ###

#1. get the web page
news = requests.get("https://news.byu.edu/")
#2. turn it into soup
news_soup = BeautifulSoup(news.content, "lxml")

#3. search the soup for whatever you want
someObject = news_soup.div("a")
print(len(someObject))

# select element based on css selector syntax
##dummybodyid > div.Page-contentWrapper > div.Page-content > main > div > div.ListImageLarge-items.list.list-1.list-items-10 > div:nth-child(10) > div > div.PromoImageLarge-content.promo-content > div.PromoImageLarge-title.promo-title-large > a
article = news_soup.select("#dummybodyid > div.Page-contentWrapper > div.Page-content > main > div > div.ListImageLarge-items.list.list-1.list-items-10 > div:nth-child(10) > div > div.PromoImageLarge-content.promo-content > div.PromoImageLarge-title.promo-title-large > a")
print (article)

# find an element with a specific word
devotional = news_soup.find(string=re.compile(".*Devotional.*")).parent.get("href")
print(devotional.text)
