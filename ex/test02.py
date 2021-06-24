#1
kuk=80
english=75
math=55
avg=(kuk+english+math)/3
print(avg)

#2
print(13% 2)

n=13
if n%2 ==0:
    print('짝수')

else:
    print('홀수')

#3
pin='881120-1068234'
yyyymmdd=pin[0:6]

print(yyyymmdd)

g=pin[7]
#print(num)
if g=='1':
    print('남자')
else:
    print('여자')

a='a:b:c:d:'
b= a.replace(':','#')
print(b)

a=['lif','is', 'too', 'short']
r= ' '.join(a)
print(r)

s= 'life is too short'
g= s.split()
print(g)

a='a:b:c:d:'
s= a.split(':')
print(s)

a=(1,3,4)
a= a+(5,)
print(a)

a=dict()
print(a)
