from tkinter import *
import random

GAME_WIDTH = 800
GAME_HEIGHT = 800
speed = 100
SPACE_SIZE = 20
BODY_PARTS = 2
SNAKE_COLOR = "#00ffe4"
RABBIT_COLOR = "#ffffff"
APPLE_COLOR = "red"
HUNTER_COLOR = "#41d50e"
BG_COLOR = "#000000"

# Snake game's snake
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

# Act as regular food that grows the snake
class Rabbit:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=RABBIT_COLOR, tag="rabbit")    


# Eden Apple that give snake extra power and speed (Increase Difficulty)
class Apple:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=APPLE_COLOR, tag="apple")
    
# Act as enemy to hunt the snake (Appears every 10 rounds)
class Hunter:
    def __init__(self):
        self.coordinates = {}
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates[(x, y)] = NONE
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=HUNTER_COLOR, tag="hunter")

def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def next_rd(snake, rabbit, apple, hunter):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == rabbit.coordinates[0] and y == rabbit.coordinates[1]:
        global day
        day += 1
        label.config(text="Day:{}".format(day))
        canvas.delete("rabbit")
        rabbit = Rabbit()
        if day > 0 and day % 14 == 0:
            canvas.delete("apple")
            apple = Apple()
        if day > 0 and day % 10 == 0:
            hunter = Hunter()
    elif x == apple.coordinates[0] and y == apple.coordinates[1]:
        day += 1
        global speed 
        speed -= 20
        label.config(text="Day:{}".format(day))
        canvas.delete("apple")
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collisions(snake, hunter):
        game_over()
    else:
        window.after(speed, next_rd, snake, rabbit, apple, hunter)

def check_collisions(snake, hunter):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    for part in snake.coordinates[1:]:
        if x == part[0] and y == part[1]:
            return True
    if (x, y) in hunter.coordinates:
        return True
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas', 50), text='You Are Dead', fill='red')

window = Tk()
window.title("sneaky snake")
window.resizable(True, True)

day = 0
direction = 'down'

label = Label(window, text="Day:{}".format(day), font=('consolas', 20))
label.pack()

canvas = Canvas(window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
rabbit = Rabbit()
apple = Apple()
hunter = Hunter()
next_rd(snake, rabbit, apple, hunter)

window.mainloop()