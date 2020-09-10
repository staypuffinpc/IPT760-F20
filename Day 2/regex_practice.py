###### PURPOSE:  to demonstrate how to use regex patterns in Python #######

### first, get a string to search
import os # the os library allows us to access the file system
fileDir = os.path.dirname(os.path.realpath('__file__'))
fileName = os.path.abspath(os.path.join(fileDir,"../data/pres_Nelson_birthday.txt"))
# open the file, read it into a variable named 'announcement' as a single string and then close it ('with' will close the file automatically after it's been read)
with open(fileName,'r') as text:
    announcement = text.read() #now we have 'announcement' as a long string.

# print (announcement)

### Now that we've got the text, let's create some regex search strings

#start by importing the regular expression module
import re


# get all numbers in the document
pattern = "\d+"

#now use "search" to search for that string, e.g.,
nums = re.search(pattern,announcement)
print(nums) #notice that this is not iterable.
if nums:
    print("we have a match!")
else:
    print("sorry, I couldn't find that pattern")

print ("nums is a: ",type(nums)) #note that it's a Match object.
print(nums)

## let's get a list of all the numbers in this text so we can read them
num_list = re.findall(pattern, announcement)
print (f"num_list is a {type(num_list)} with {len(num_list)} items.")
for num in num_list:
    print(num)

# find all the years in the original text.
year_pattern = "\d{4}"
years = re.findall(year_pattern, announcement)
print("----------- YEARS -----------")
for year in years:
    print(year)

# get just the first paragraph #
para_pattern = "^\w*.*"
first = re.search(para_pattern,announcement)
print("----------- 1st Paragraph -----------")
if first:
    print (first.group(0))
else:
    print ("I could not match that pattern.")

#let's replace all the spaces in our "first" paragraph with hyphens
print (re.sub("\s","-",first.group(0)))
# now let's split the words from the first paragraph into a list
first_words = re.split("\s+[^\b]",first.group(0))
for word in first_words:
    print (word)

#list all the methods of the match object first
print(dir(first))
# help(first.group)
print(first.group(0).upper())
