### STUDENT class constructor file ###

#You declare a class using the "class" keyword.  Typically, you'll use Title case
class Student:
    """A basic student object """

    #first, declare "global" variables that apply to all students
    alive = True

    # initialize the student object with default values
    def __init__(self, age = 10, email = "student@school.edu", grade=12, gpa=0 ): #must ALWAYS use "self" in class methods (i.e., functions)
        self.age = age
        self.email = email
        self.grade = grade
        self.gpa = gpa

    #create other methods to do things with student's info
    def update_grade(self,grade):
        self.grade = grade
        print(f"Grade was updated to {grade}")
