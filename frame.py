from turtle import Turtle

class Frame(Turtle):
    def __init__(self, matrix):
        super().__init__()
        self.parts = []
        self.create_frame()
        self.create_hole()
        self.matrix = matrix
    
       
    def create_frame(self):
        frame = Turtle()
        frame.shape('square')
        frame.color('red')
        frame.penup()
        frame.resizemode()
        frame.shapesize(0.5, 0.5)
        self.parts.append(frame)
    
    def create_hole(self):
        hole = Turtle()
        hole.shape('square')
        hole.color('black')
        hole.penup()
        hole.resizemode()
        hole.shapesize(0.4, 0.4)
        self.parts.append(hole)

    def go_up(self):
        for obj in self.parts:   
            x_cord = obj.position()[0]
            y_cord = obj.position()[1]
            obj.goto(x_cord,y_cord+10)

    def go_down(self):
        for obj in self.parts:   
            x_cord = obj.position()[0]
            y_cord = obj.position()[1]
            obj.goto(x_cord,y_cord-10)

    def go_right(self):
        for obj in self.parts:   
            x_cord = obj.position()[0]
            y_cord = obj.position()[1]
            obj.goto(x_cord+10,y_cord)

    def go_left(self):
        for obj in self.parts:   
            x_cord = obj.position()[0]
            y_cord = obj.position()[1]
            obj.goto(x_cord-10,y_cord)

    def convert_cord(self):
        frame = self.parts[0]
        x_cord = frame.position()[0]
        y_cord = frame.position()[1]
        new_x = int((x_cord+500)/10)
        new_y = int(-(y_cord+500)/10)
        if self.matrix[new_y][new_x] == 0:
            self.matrix[new_y][new_x] = 1
        else:
            self.matrix[new_y][new_x] = 0


    def clear_screen(self):
        for i in self.parts:
            i.hideturtle()
        self.parts = []