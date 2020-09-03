"""PURPOSE: demonstrate coding fundamentals in python """

## basic operations in python ##


########## VARIABLES ############

#strings

## 4 ways of formatting strings ##

#Booleans

#ints

#floats


#adding an int and a float results in a float

#lists


#dicts (i.e., dictionaries)

######### CONDTIONALS ############
# equivalency

# inequalities

# "not"

#conditionals in Python

######### LOOPS ############
# count from 1 to 10


#count from 1 to 10, start at 5


#count from 1 to 10 by 2


#while loops


######### FUNCTIONS ############


#create a function that takes arguments and returns a value

# create a docstring to indicate what the function is supposed to do




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


#how many words are in the list?

#replace each "The" with "Yikes!"

#upper case (.lower() for lower case)

#strip: removes  leading characters from both ends

#check if all characters are alphabetic

#check if the first character is a space


#reverse the list:  nothing before 1st colon mean start at the beginning; nothing after first colon means go to the end.

#find the index of the first occurrence of "Georgia"

#count how many times a word occurs

#find the first index of a string

#print the last 3 characters


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
