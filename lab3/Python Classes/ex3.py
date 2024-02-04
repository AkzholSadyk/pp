class Shape():
    def __init__(self):
            pass
    
    def area(self):
            
            return 0  
class Square(Shape):

    def __init__(self,length=0):
        Shape.init(self)
        self.length=length
    def area(self):
          
          return self.length**2

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
rect= Rectangle(3,4)
print(rect.area())
