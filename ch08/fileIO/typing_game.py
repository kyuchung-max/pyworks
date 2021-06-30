import random
import time

f=open('words.txt','r')
word=f.read().split()
#print(word)
f.read()

n=1     #문제 번호
print('[타자게임] 준비되면 엔터')
input()
start=time.time()
q=random.choice(word)
while n <= 10:
    print('문제',n)
    print(q)
    x=input()   #사용자가 입력
    if q==x:
        print('통과')
        n +=1
        q=random.choice(word)
    else:
        print('오타 다시')
    #n += 1
print('게임 종료')
end=time.time()
et=end-start
print('타자 시간: %.2f초' % et)