from Point import Point
from Heading import Heading

from collections import deque

defaultSnake = [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)]
defaultHeading = Heading.EAST

class Snake():

    def __init__(self, board, snake = defaultSnake, heading = defaultHeading):
        self.board = board
        self.snake = deque(snake)
        self.lastHeading = heading
        self.heading = heading
        self.dead = False
        self.growCount = 0

    def getNextPos(self):
        front = self.snake[-1]

        if self.heading == Heading.NORTH:
            newFront = self.board.getAbove(front)
        elif self.heading == Heading.EAST:
            newFront = self.board.getRight(front)
        elif self.heading == Heading.SOUTH:
            newFront = self.board.getBelow(front)
        elif self.heading == Heading.WEST:
            newFront = self.board.getLeft(front)
        
        return newFront

    def checkCollision(self):
        for i in range(0, len(self.snake)-1):
            if self.snake[-1] == self.snake[i]:
                return True
        
        return False
    
    def move(self):
        if self.dead:
            return False
        
        if self.growCount > 0:
            self.growCount -= 1
        else:
            self.snake.popleft()
        
        newFront = self.getNextPos()
        
        if not newFront:
            self.dead = True

            return False
        
        self.snake.append(newFront)
        self.lastHeading = self.heading

        if self.checkCollision():
            self.dead = True

            return False

        return True
    
    def grow(self, increment):
        self.growCount += increment

    def setHeading(self, heading):
        lastAndNewHeadings = {self.lastHeading, heading}

        if Heading.NORTH in lastAndNewHeadings and Heading.SOUTH in lastAndNewHeadings:
            return
        elif Heading.EAST in lastAndNewHeadings and Heading.WEST in lastAndNewHeadings:
            return
        
        self.heading = heading
    
    def getPositions(self):
        return list(self.snake)