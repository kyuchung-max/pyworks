#global 전역 변수
def one_up():
    global x
    x = x+1
    return x
x=0
print(one_up())
print(one_up())
