#1개씩 랜덤 추출
import random
try:
    f=open('c:/pyfile/2021kbo.txt','r')
    data=f.read().split()
    team=random.choice(data)
    print(team)

    f.close()
except FileNotFoundError as e:
    print(e)