#다른 곳에 그리기
import turtle as t
t.shape('turtle')

def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n,d):
    for x in range(n):
        t.forward(d)
        t.left(360/n)
    
polygon(3)
polygon(5)

t.up()
t.forward(100)
t.down()
'''
for x in range(4):
    t.forward(50)
    t.left(90)
'''

polygon2(4,80)
polygon2(5,180)

t.mainloop()