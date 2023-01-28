from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 20
SPACE_SIZE = 80
BODY_PARTS = 2
SNAKE_COLOR = "#00ffe4"
RABBIT_COLOR = "#ffffff"
BG_COLOR = "000000"
# Should uptade tk version in the future
TK_SILENCE_DEPRECATION = 1

# Snake game's snake
class Snake:
    pass

# Act as regular food that grows the snake
class Rabbit:
    pass

# Eden Apple that give snake extra power and speed (Increase Difficulty)
class Apple:
    pass

# Act as enemy to hunt the snake (Appears every 10 rounds)
class Eagle:
    pass

window = Tk()
window.title("sneaky snake")
window.resizable(True, True)

day = 0
direction = 'down'

label = Label(window, text="Day:{}".format(day), font=('consolas', 40))
label.pack()

window.mainloop()