#abs()
def abs_sign(x):
    if x < 0:
        return -x
    else:
        return x
    
import math
def abs_square(x):
    y= x*x
    return math.sqrt(y)


n1= abs_sign(-3)
print(n1)
n2= abs_square(-3)
print(n2)
