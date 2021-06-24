import time

input('엔터를 누르고 20초를 센다')
start= time.time()

input('20초를 센다 엔터를 누름')
end=time.time()
et = end-start
print('실제 시간: ', et, '초')
print('시간 차이: ', abs(et-20),'초')
