from Board import Board
from Snake import Snake
from Interface import Interface
from time import sleep

import threading

board = Board(20, 20, True)
snake = Snake(board)
interface = Interface(board, snake)

def gameFunction():
    paused = False
    resumeCount = 0
    
    while not interface.windowClosed:
        if interface.state() != "normal":
            paused = True
            resumeCount = 0
            
            continue

        if paused:
            sleep(1)

            resumeCount += 1
            paused = resumeCount < 3

            continue
        
        snakeAlive = snake.move()

        if not snakeAlive:
            break

        interface.draw()
        sleep(0.1)

gameThread = threading.Thread(target = gameFunction)
gameThread.start()

interface.mainloop()