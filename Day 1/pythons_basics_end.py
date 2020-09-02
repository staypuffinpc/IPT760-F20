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


######### FUNCTIONS ############



######### LIST METHODS ############




######### WORKING WITH AN EXTERNAL FILE ############
