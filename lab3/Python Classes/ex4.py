import math

class Point:
    def __init__(self):
        self.x = ""
        self.y = ""
    
    """def getintegers(self):
        self.x=int(input("x ="))
        self.y=int(input("y ="))"""

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.new_x=int(input("new x ="))
        self.new_y=int(input("new y ="))
        self.x = new_x
        self.y = new_y
        
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
"""user = Point()
user.getintegers()
user.show()
user.dist()"""