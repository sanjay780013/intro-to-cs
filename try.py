import turtle

def draw(side):
    window = turtle.Screen()
    window.bgcolor("red")
    turtle.shape("turtle")
    turtle.color("yellow")
    turtle.speed(2)
    brad = turtle.Turtle()
    #if side ==0:
        #angie = turtle.turtle()
        #angie.shape("arrow")
        #angie.color("blue")
        #angie.circle(100)
    s =0
    while s < side:
        brad.forward(100)
        brad.right(90)
        s=s+1
    window.exitonclick()
draw(4)
     
        
        
  
