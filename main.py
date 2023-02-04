import time
from turtle import Screen
from cell import Cell
from matrix_functions import check_cell, MATRIX_SIZE
from frame import Frame


screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("Game of Life")
screen.tracer(0)
screen.update()
screen.listen()

matrix = [[0 for i in range(MATRIX_SIZE)] for j in range(MATRIX_SIZE)]

frame = Frame(matrix)
cell = Cell(matrix)

screen.update()


def go_left():
    frame.go_left()
    screen.update()
def go_right():
    frame.go_right()
    screen.update()
def go_up():
    frame.go_up()
    screen.update()
def go_down():
    frame.go_down() 
    screen.update()

def create_pattern(): 
    
    frame.convert_cord()
    matrix = frame.matrix
    cell.clear_screen()
    cell.matrix = matrix
    cell.draw_all_cells(matrix)
    screen.update()


def start():
    frame.clear_screen()
    matrix  = cell.matrix
    while True:
        matrix = check_cell(matrix)
        cell.matrix = matrix
        cell.clear_screen()
        cell.draw_all_cells(matrix)
        screen.update()
        time.sleep(0.1)

def exit_game():
    screen.bye()
    exit()
        
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_left, "Left")
screen.onkeypress(create_pattern, "space")
screen.onkeypress(start, "Return")
screen.onkeypress(exit_game, "Escape")




screen.mainloop()
