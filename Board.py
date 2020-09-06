from Point import Point

class Board():
    
    def __init__(self, width, height, wrap):
        self.width = width
        self.height = height
        self.wrap = wrap
    
    def setWrap(self, wrap):
        self.wrap = wrap

    def isInBounds(self, point):
        if point.x < 0 or point.x > self.width-1:
            return False
        elif point.y < 0 or point.y > self.height-1:
            return False
        
        return True

    def sanitise(self, point):
        if self.wrap:
            if point.x < 0:
                point.setX(self.width-1)
            elif point.x > self.width-1:
                point.setX(0)
            
            if point.y < 0:
                point.setY(self.height-1)
            elif point.y > self.height-1:
                point.setY(0)
            
            return point
        elif self.isInBounds(point):
            return point

    def getLeft(self, point):
        newPoint = self.sanitise(Point(point.x-1, point.y))
        
        return newPoint

    def getRight(self, point):
        newPoint = self.sanitise(Point(point.x+1, point.y))
        
        return newPoint

    def getAbove(self, point):
        newPoint = self.sanitise(Point(point.x, point.y-1))
        
        return newPoint

    def getBelow(self, point):
        newPoint = self.sanitise(Point(point.x, point.y+1))
        
        return newPoint