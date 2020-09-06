from Board import Board
from Snake import Snake
from Interface import Interface

import threading

board = Board(20, 20, True)
snake = Snake(board)
interface = Interface(board, snake)

def gameFunction():
    while snake.move():
        interface.update()

gameThread = threading.Thread(target = gameFunction)
gameThread.start()

interface.mainloop()