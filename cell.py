from turtle import Turtle


class Cell(Turtle):
    def __init__(self, matrix):
        super().__init__()
        self.cells = []
        self.hideturtle()
        self.matrix = matrix
        self.draw_all_cells(self.matrix)

    def add_cell(self, x, y):
        cell = Turtle(shape="square")
        cell.color("white")
        cell.penup()
        cell.setx(x)
        cell.sety(y)
        cell.resizemode()
        cell.shapesize(0.4, 0.4)
        self.cells.append(cell)

    def draw_all_cells(self, matrix):

        y = 500
        for i in matrix:
            x = -500
            for j in i:
                if j == 1:
                    self.add_cell(x, y)
                x += 10
            y -= 10

    def clear_screen(self):
        for i in self.cells:
            i.hideturtle()
        self.cells = []
