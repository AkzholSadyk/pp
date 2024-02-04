#What is the correct syntax to assign a "init" function to a class?



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age





class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)