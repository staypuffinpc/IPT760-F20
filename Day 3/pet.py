#define a base class for a Pet
class Pet:
    """ a companion animal """

    living = True
    test = "Yes"

    def __init__(self):
        self.breed = ""
        self.size = 2
        self.name = "No name"

    def do_trick(self,type="roll"):
        if type == "jump":
            print("I'm jumping. I promise.")
        elif type == "roll":
            print("Look at me roll over.")
        elif type == "dead":
            print("AAAAAAAAAggggggh!")
        else:
            print("I won't work for free.")
