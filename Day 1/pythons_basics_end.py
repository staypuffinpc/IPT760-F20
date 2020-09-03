"""PURPOSE: demonstrate coding fundamentals in python """

## basic operations in python ##
print (5 + 6) # addition
print (5 - 6) # subtraction
print (5.0 / 6) # division
print (6 % 5) # displays the remainder
print (4*5) # multiplication
print (2**6) # exponents

########## VARIABLES ############

#strings
first = "Peter"
last = "Rich"

print ("My name is ", first + last)
## 4 ways of formatting strings ##

print ("My name is "+first + " "+ last+".") # Concatentation
print ("My name is %s %s." % (first, last)) # the "old" formatting way
print ("My name is {} {}.".format(first, last)) # the new .format() way
print (f"My name is {first} {last}.") # f strings

#Booleans
lights = True
print ("Are the lights on?", lights)

#ints
age = 42
print ("What is my age?", age)
#floats
weight = 195.3
print ("What is my weight?", weight)

#adding an int and a float results in a float
print ("Age + weight: ", age + weight)

#lists
siblings = ["David", "Robyn", "Rebecca", "Michael","Peter","Dan","Matt", "Sarah","Liz", "Adam"]
ages = [46, 45, 44, 42, 41, 39, 39, 36, 33, 29]
print("I am " + siblings[4]+" and I am "+str(ages[4])+ " years old.")
print ("The oldest sibling is ", ages[0])
print ("The youngest sibling is ", siblings[-1])

#dicts (i.e., dictionaries)
rich_siblings = {
    "David" : 47,
    "Robyn" : 46,
    "Rebecca" : 45,
    "Michael" : 43,
    "Peter" : 42,
    "Dan" : 40,
    "Matt" : 40,
    "Sarah" : 37,
    "Liz" : 34,
    "Adam" : 30
}

print ("How old is David?", rich_siblings["David"])

######### CONDTIONALS ############
# equivalency
print ("Does 5 = 2+3?", 5 == 2+3)

# inequalities
print ("Am I over 50 years old?", age > 50)
print ("Am I younger than 50 years old?", age < 30)
print ("Am I at least 42 years old?", age >= 42 )

# "not"
print ("Is 15 not the same as 6+8?", 15 != 6+8)

#conditionals in Python
if (5 > 6) :
    print("hello word!")
else:
    print("what a cruel world!")

if (5 == 6) :
    print ("looks like they're the same")
elif (6 < 5):
    print ("wow, that's really weird that 6 is less than 5")
else:
    print ("that makes sense")


######### LOOPS ############
# count from 1 to 10
for i in range(10):
    print (i)

#count from 1 to 10, start at 5
for i in range(5,10):
    print (i)

#count from 1 to 10 by 2
for i in range(1,10,2):
    print (i)

#while loops
import time
counter = 7
while counter > 0:
    print (counter)
    counter = counter -1
    time.sleep(1)

######### FUNCTIONS ############
def silly():
    ## do something silly
    pass

#create a function that takes arguments and returns a value
def avg(num1, num2):
    average = (num1 + num2) *.5
    return average

# create a docstring to indicate what the function is supposed to do
define whatsyourname():
    """the purpose of this function is to
    ask people what their name is"""
    name = input("What's your name?")
    print (f"Oh, hello there {name}")



######### LIST METHODS ############
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

######### STRING METHODS ###########
#sample string to work with
article1S2 = '''The actual Enumeration shall be made within three Years after the first Meeting of the Congress of the United States, and within every subsequent Term of ten Years, in such Manner as they shall by Law direct. The Number of Representatives shall not exceed one for every thirty Thousand, but each State shall have at Least one Representative; and until such enumeration shall be made, the State of New Hampshire shall be entitled to choose three, Massachusetts eight, Rhode Island and Providence Plantations one, Connecticut five, New York six, New Jersey four, Pennsylvania eight, Delaware one, Maryland six, Virginia ten, North Carolina five, South Carolina five and Georgia three.
'''
#split the text into a list with each word
words = article1S2.split()
for word in words:
    print(word)

#how many words are in the list?
print("There are "+str(len(words))+" words in this list.")

#replace each "The" with "Yikes!"
yikes = article1S2.replace('The','Yikes!')
print(yikes)

#upper case (.lower() for lower case)
print(article1S2.upper())

#strip: removes  leading characters from both ends
print(article1S2.lstrip())

#check if all characters are alphabetic
print("All alphabetic? ",article1S2.isalpha())

#check if the first character is a space
print("Is first character a space?",article1S2[0:1].isspace())
print("Is LAST character a space?",article1S2[-1:].isspace())


#reverse the list:  nothing before 1st colon mean start at the beginning; nothing after first colon means go to the end.
print(article1S2[::-1])

#find the index of the first occurrence of "Georgia"
print(article1S2.index("Georgia"))

#count how many times a word occurs
print(article1S2.count("the"))

#find the first index of a string
print(article1S2.find("New York"))

#print the last 3 characters
print(article1S2[-3:])


# ######### WORKING WITH AN EXTERNAL FILE ############
# import os
# ## First, retrieve the file and store it in a variable ##
# fileDir = os.path.dirname(os.path.realpath('__file__'))
# fileName = os.path.abspath(os.path.join(fileDir,'../data/us_constitution.txt'))
#
# #open the file, read it into a variable named 'constitution' as a single string and then close it ('with' will close the file)
# with open(fileName,'r') as text:
#     constitution = text.read().replace('\n','')
#
# print(constitution)
#     #possible modes (2nd argument))
#         # r = read only
#         # w = write mode.  Will overwrite existing info
#         # a = append mode. Adds to the end of the file
#         # r+ = read/write
#         # x  open for exclusive creation.  Only works for NEW files
#         # b = binary mode
#         # t = text mode (Default)
