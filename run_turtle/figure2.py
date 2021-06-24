import turtle as t

t.shape('turtle')
n=5
for i in range(4):
    t.forward(100)
    t.right(360/n)

t.color('red')
n=3
for i in range(3):
    t.forward(100)
    t.left(360/n)
    
t.color('blue')
t.pensize(3)
t.circle(50)
