###### PURPOSE: demonstrate python fundamentals ######

first = "Peter"
last = "Rich"
age = 42
weight = 195.5
lights_on = False

# formatting strings
print("Hello "+first+" "+last+".  Are you "+str(age)+" years old?") #Concatentation
print("Hello %s %s.  Are you %d years old?" % (first, last, age)) #old string formatting
print("Hello {} {}. Are you {} years old?".format(first, last, age)) # .format() method
print(f"Hello {first} {last}.  Are you {float(age)} years old?") #fstring
