from turtle import Turtle, Screen

screen = Screen()
tom = Turtle()

def up():
    tom.setheading(90) #tom.left(90)
    # tom.forward(20)
    
def down():
    tom.setheading(270)
    # tom.forward(20)
    
def left():
    tom.setheading(180)
    # tom.forward(20)
    
def right():
    tom.setheading(0)
    # tom.forward(20)

def move():
    tom.forward(20)
    
def clear_screen():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

    
screen.listen()
screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")
screen.onkey(fun=left, key="Left")
screen.onkey(fun=right, key="Right")
screen.onkey(fun=clear_screen, key="c")
screen.onkey(fun=move, key="space")





screen.exitonclick()