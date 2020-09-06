class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        
        return False
    
    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y
    
    def incX(self, increment):
        self.x += increment
    
    def incY(self, increment):
        self.y += increment