f=open('c:/pyfile/2021kbo.txt','w')
team=['기아','삼성','엘지','nc','키움','kt','ssg','롯데']

for i in team:
    f.write(i + ' ')

f.close()
'''

n=len(team)
for i in range(n):
    f.write(team[i] + ' ')
f.close()
'''
f=open('c:/pyfile/2021kbo.txt','r')
data=f.read()
print(data)
f.close()