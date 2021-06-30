#threading module
import threading

def function_a():
    print('5초')
    timer=threading.Timer(5,function_a)
    timer.start()

function_a()