import turtle

turtle=turtle.Turtle()

def square(length,angle):
       turtle.color(0,0,1)
       turtle.pensize(5)
       turtle.forward(length)
       turtle.right(angle)
       turtle.forward(length)
       turtle.right(angle)
       turtle.forward(length)
       turtle.right(angle)
       turtle.forward(length)
square(100,90)

for i in range(25):
    turtle.right(105)
    square(100,90)

