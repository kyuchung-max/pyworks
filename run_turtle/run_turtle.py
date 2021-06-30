import turtle as t
import random

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)


def turn_left():
    t.setheading(180)
    t.forward(10)


def turn_down():
    t.setheading(270)
    t.forward(10)

def play():
    t.forward(10)
    te.forward(9)
    ang=te.towards(t.pos())
    te.setheading(ang)

    #
    if t.distance(tf) <12:
        x=random.randint(-230,230)
        y=random.randint(-230,230)
        tf.goto(x,y)

    if t.distance(te)>=12:
        t.ontimer(play,100)
    t.ontimer(play,100) #0.1 sec
 #main
 t.setup(500,500)
 t.title('달려라 거북이')
t.bgcolor('orange')
t.shape('turtle')
t.speed(0)
t.up()
t.color('white')    #주인공

te=t.Turtle()       #적
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0,200)

tf=t.Turtle()       #먹이
tf.shape('circle')
tf.color('green')
tf.speed(0)
tf.up()
tf.goto(0,-200)
t.onkeypress(turn_right, 'Right')
t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_left, 'Left')
t.onkeypress(turn_down, 'Down')
t.listen()
play()
t.mainloop()