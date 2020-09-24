#### PURPOSE: show how to use BeautifulSoup to scrape web page data ####
### documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
## import needed libraries
from bs4 import BeautifulSoup
import requests
import csv
import re

def separator(description):
    print (f"------------ {description} ------------" )

# #fetch all the data from a single URL
# url = "https://scholar.google.com/citations?user=JFv6vGMAAAAJ&hl=en"
# page = requests.get(url)
#
# #turn the page into Soup
# soup = BeautifulSoup(page.content, features="lxml")
#
# # print(soup.prettify())
#
# # first_link = soup.a
# # print("First link tag:",first_link)
# # print("First link text",first_link["href"])
# # print(first_link.attrs) #get the name of the first link
#
# bodyTag = soup.body
# # for child in bodyTag.children:
# #     print(child.name)
# #
# # for child in bodyTag.descendants:
# #     print(child.name)
#
# print(f"There are {len(list(bodyTag.descendants))} HTML tags in this document.")
# #
# # print the text of all the descendants of body
# # for child in bodyTag.descendants:
# #     print(child.string)
# #
# # get the link to all of my publications.  Note that these all have the class: gsc_a_at.  use "find" to just get the first instance.
# separator("Get Google Scholar Info")
# pubs = soup.find_all("a",{"class":"gsc_a_at"})
# print(f"There are {len(pubs)} reference links on this page.")
#
# # print the title of each of my pubs
# for i in range(len(pubs)):
#     print(f"{i+1}. {pubs[i].text} \n")
#
# #get the URLS for each of my publications
# for i in range(len(pubs)):
#     print(f"{i+1}. {pubs[i].get('data-href')} \n")
#
# #write the title and URL for each publication to a list of dicts.  Then, save it to a .csv
# separator("My pubs in a list of dicts")
# pub_data = []
# for pub in pubs:
#     this_pub = {}
#     this_pub["title"] = pub.text
#     this_pub["url"] = pub.get('data-href')
#     pub_data.append(this_pub)
# print(f"There are {len(pub_data)} publications in this list (see below):\n {pub_data}")
#
# pub_file = csv.writer(open("Peter_Rich_publications.csv", "w"))
# pub_file.writerow(["title","url"])
# for pub in pub_data:
#     pub_file.writerow([pub["title"],pub["url"]])

#use the "string" keyword to search for specific strings
separator("Using the 'string' keyword")
news_request = requests.get("https://news.byu.edu")
news_soup = BeautifulSoup(news_request.content, "lxml")
story = news_soup.find("a",string=re.compile("\w*Devotional:\w*"))
print( story.get("href") )

#use "select" method to use a css selector (to get selector syntax, use the copy option in Chrome)
separator("Use the 'select' method with unnammed, buried info")


#work your way up the tree (look for ancestors instead of descendants) using find_parents, find_next_sibling, etc.
