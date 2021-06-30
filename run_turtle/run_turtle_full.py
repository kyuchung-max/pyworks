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

def start():
    global playing
    if playing==False:
        playing=True
        t.clear()
        play()

def message(m1,m2):
    t.clear()
    t.goto(0,100)
    t.write(m1,False,'center',("",20))
    t.goto(0,-100)
    t.write(m2,False,'center',("",15))

def play():
    global score
    global playing

    t.forward(10)

    if random.randint(1,5)==3:
        ang=te.towards(t.pos())
        te.setheading(ang)
    speed=score+5
    if speed>15:
        speed=15
    te.forward(speed)

    if t.distance(tf) <12:
        score += 1
        t.write(score)
        x=random.randint(-230,230)
        y = random.randint(-230, 230)
        tf.goto(x,y)

    if t.distance(te)<12:
        text='Score : '+str(score)
        message('Game over',text)
        playing=False
        score=0

    if playing:
        t.ontimer(play,100)

 #main
score=0
playing=False
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
t.onkeypress(start,'space')
t.listen()
message('Turtle Run','[space]')
t.mainloop()