import random
from tkinter import *
from Heading import Heading

cellWidth = 20
cellHeight = 20

class Interface():
    
    def __init__(self, board, snake):
        root = Tk()
        root.title("Snake")
        root.configure(width = board.width*cellWidth, height = board.height*cellHeight)
        root.resizable(False, False)

        def onClose():
            self.windowClosed = True
            root.destroy()
        
        root.protocol("WM_DELETE_WINDOW", onClose)

        root.bind("w", lambda e: snake.setHeading(Heading.NORTH))
        root.bind("W", lambda e: snake.setHeading(Heading.NORTH))
        root.bind("<Up>", lambda e: snake.setHeading(Heading.NORTH))

        root.bind("d", lambda e: snake.setHeading(Heading.EAST))
        root.bind("D", lambda e: snake.setHeading(Heading.EAST))
        root.bind("<Right>", lambda e: snake.setHeading(Heading.EAST))

        root.bind("s", lambda e: snake.setHeading(Heading.SOUTH))
        root.bind("S", lambda e: snake.setHeading(Heading.SOUTH))
        root.bind("<Down>", lambda e: snake.setHeading(Heading.SOUTH))

        root.bind("a", lambda e: snake.setHeading(Heading.WEST))
        root.bind("A", lambda e: snake.setHeading(Heading.WEST))
        root.bind("<Left>", lambda e: snake.setHeading(Heading.WEST))

        cells = {}

        for x in range(0, board.width):
            cells[x] = {}

            for y in range(0, board.height):
                cell = Frame(root, width = cellWidth, height = cellHeight)
                cell.pack_propagate(0)
                cell.place(x = x*cellWidth, y = y*cellHeight)
                cell.configure(bg = "#FFFFFF")

                cells[x][y] = cell
        
        self.board = board
        self.snake = snake
        self.cells = cells
        self.root = root
        self.lastPositions = []
        self.windowClosed = False

        self.draw()

    def mainloop(self):
        self.root.mainloop()

    def state(self):
        return self.root.state()
    
    def draw(self):
        newPositions = self.snake.getPositions()

        for point in self.lastPositions:
            if not (point in newPositions):
                cell = self.cells[point.x][point.y]

                cell.configure(bg = "#FFFFFF")
        
        for point in newPositions:
            cell = self.cells[point.x][point.y]

            cell.configure(bg = "#FF8866")
        
        self.lastPositions = newPositions