import turtle as t
import random as r

t.shape('turtle')
t.speed(5)
t.bgcolor('pink')
t.setup(500,500)

for x in range(300):
    angle = r.randint(1,360)
    t.setheading(angle)
    t.forward(10)

t.mainloop()