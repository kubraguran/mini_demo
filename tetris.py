import turtle


#mini screen
wn = turtle.Screen()
wn.title("Tetris by Kubra")
wn.bgcolor("black")
wn.setup(height=800, width=600)
wn.tracer(0)


#score
score = 0

#pen for score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,300)
pen.write("Score: 0", align='center', font=("Courier", 24, "normal"))

class Shape:
    def __init__(self,x,y):
        #shape for destroy
        self.shape = turtle.Turtle()
        self.shape.speed(0)
        self.shape.shape("square")
        self.shape.shapesize(stretch_len=2, stretch_wid=1)
        self.shape.color("gold","pink")
        self.shape.penup()
        self.shape.goto(x,y)


#aralari 50 px
shapes = list(map(lambda i: Shape(-270 + i*50, 220), range(10)))

shapes_middle = list(map(lambda i: Shape(-300 + i*50, 190), range(10)))

shapes_bottom = list(map(lambda i: Shape(-250 + i*50, 160), range(10)))

for sh in shapes:
    sh.shape.goto(sh.shape.xcor() + 50, sh.shape.ycor() - 50)

for sh in shapes_bottom:
    sh.shape.goto(sh.shape.xcor() + 50, sh.shape.ycor() - 50)

for sh in shapes_middle:
    sh.shape.goto(sh.shape.xcor() + 50, sh.shape.ycor() - 50)



#shape 2
main_shape = turtle.Turtle()
main_shape.speed(0)
main_shape.shape("square")
main_shape.shapesize(stretch_len=6, stretch_wid=2)
main_shape.color("gold","blue")
main_shape.penup()
main_shape.goto(0,-200)


#draw movement -> 

def main_shape_left():
    if main_shape.xcor() > -230:
        x = main_shape.xcor()
        x -= 20
        main_shape.setx(x)

def main_shape_right():
    if main_shape.xcor() < 230:
        x = main_shape.xcor()
        x += 20
        main_shape.setx(x)
 


#check collision

def collision(ball,shapes):
    for shape in shapes:
        dst = ball.distance(shape.shape)
        if dst < 40:
           shape.shape.hideturtle()
           shapes.remove(shape)
           return True
   
    

#reset gane


def reset_game():
    ball.goto(0,0)
    ball.dx = 2
    ball.dy = 2
    main_shape.goto(0,-200)


#draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

#keyboard

wn.listen()
wn.onkeypress(main_shape_left, 'Left')
wn.onkeypress(main_shape_right,'Right')




#main loop

while True:
    wn.update()
    
    #collision(ball, Shape)
    if collision(ball,shapes) or collision(ball, shapes_middle) or collision(ball, shapes_bottom):
        ball.dy *= -1
        pen.clear()
       
        pen.write("Score {}".format(score), align='center',font=("Courier", 24, "normal "))
        score += 1
        

    #move to ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #check for wall
    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1

    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1

    if ball.ycor() < -360:
        ball.sety(-360)
        ball.dy *= -1

    if ball.ycor() > 360:
        ball.sety(360)
        ball.dy *= -1


    if (ball.xcor() < 270 and ball.xcor() > -380) and (ball.ycor() < main_shape.ycor() + 40 and ball.ycor() > main_shape.ycor() - 40):
        if ball.distance(main_shape) < 40:
           ball.sety(main_shape.ycor() + 40)
           ball.dy *= -1
    elif ball.ycor() < -360:
          ball.sety(-360)
          ball.dy *= -1


 

        




 







