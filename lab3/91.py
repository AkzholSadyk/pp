"""We have used the Student class to create an object named x.

What is the correct syntax to execute the printname method of the object x?"""


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname= lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Akzhol", "Sadyk")
x.printname()
