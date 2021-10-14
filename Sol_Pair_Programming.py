import turtle

turtle.showturtle()
turtle.shape('turtle')

side = int(input("Enter the side value"))

if 0 < side <= 100: 

    for x in range(20):
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.forward(side)
        if x % 2 == 0:
            turtle.left(175)
            turtle.pencolor('red')
        else:
            turtle.left(225)
            turtle.pencolor('green')

    turtle.end_fill()
    
elif 100 < side <= 200:
    
        for x in range(20):
            turtle.fillcolor("cyan")
            turtle.begin_fill()
            turtle.forward(side)
            if x % 2 == 0:
                turtle.right(175)
                turtle.pencolor('red')
            else:
                turtle.right(225)
                turtle.pencolor('blue')

        turtle.end_fill()
        
else:
    
        for x in range(20):
            turtle.fillcolor("red")
            turtle.begin_fill()
            turtle.forward(side)
            if x % 2 == 0:
                turtle.left(175)
                turtle.pencolor('blue')
            else:
                turtle.left(225)
                turtle.pencolor('yellow')

        turtle.end_fill()    

turtle.ht()