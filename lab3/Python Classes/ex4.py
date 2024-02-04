import math

class Point:
    def __init__(self):
        pass
    #    self.x = ""
    #    self.y = ""
    #    self.new_x= ""
    #    self.new_y= ""
    def show(self):
        self.x=int(input("x = "))
        self.y=int(input("y = "))
        print(f"Point({self.x}, {self.y})")

    def move(self):
        self.new_x=int(input("new x = "))
        self.new_y=int(input("new y = "))
        print(f"new Point({self.new_x}, {self.new_y})")
        
    def dist(self):
        print( math.sqrt((self.x - self.new_x) ** 2 + (self.y - self.new_y) ** 2))
    
user = Point()
user.show()
user.move()
user.dist()