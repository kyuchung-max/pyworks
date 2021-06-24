import time

print(time.time()) #1970 1.1 이후 초로 계산
print(time.localtime())
print(time.ctime())
print(time.strftime('%x', time.localtime()))
print(time.strftime('%c', time.localtime()))

for i in range(1,11):
    print(i)
    time.sleep(1)

