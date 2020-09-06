import random
from tkinter import *

cellWidth = 20
cellHeight = 20

class Interface():

    def __init__(self, board, snake):
        root = Tk()
        root.title("Snake")
        root.configure(width = board.width*cellWidth, height = board.height*cellHeight)
        root.resizable(False, False)

        cells = {}

        for x in range(0, board.width):
            cells[x] = {}

            for y in range(0, board.height):
                cell = Frame(root, width = cellWidth, height = cellHeight)
                cell.pack_propagate(0)
                cell.place(x = x*cellWidth, y = y*cellHeight)

                cells[x][y] = cell
        
        self.board = board
        self.snake = snake
        self.cells = cells
        self.root = root
        self.lastPositions = []

        self.update()

    def mainloop(self):
        self.root.mainloop()
    
    def update(self):
        newPositions = self.snake.getPositions()

        for point in self.lastPositions:
            print(point in newPositions)
            if not (point in newPositions):
                cell = self.cells[point.x][point.y]

                cell.configure(bg = "#FFFFFF")
        
        for point in newPositions:
            cell = self.cells[point.x][point.y]

            cell.configure(bg = "#FF8866")