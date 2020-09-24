### PURPOSE: To demonstrate how to call and use methods of a class object ##

from pet import Pet

myPet = Pet()
print(myPet.name)
myPet.name = "New name"
print(myPet.name)

secondPet = Pet()
secondPet.name = "Indiana"
print(f"secondPet is named {secondPet.name}.")

secondPet.do_trick("jump")
myPet.do_trick()
print(f"Is myPet living? {myPet.living}.")
myPet.living = False
print(f"Is myPet living? {myPet.living}.")
print(f"Is secondPet living? {secondPet.living}.")
myPet.test = "No"
print (secondPet.test)
