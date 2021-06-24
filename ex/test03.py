a= 'life is too short, you need python'
if 'wife'in a: print('wife')
elif 'python' in a and 'you' not in a: print('python')
elif 'shirt' not in a: print('shirt')
elif 'need'in a: print('need')

i= 0
while True:
    i += 1
    if i>5  :break
    print(i*'*')

i= 0
for i in range(1,6):
    for j in range(1,i+1):
        print('*', end='')
    print()

for i in range(1,101):
    print(i)

#p148 Q5
A=[70,60,55,75,95,90,80,80,85,100]
total=0
for score in A:
    total += score
avg=total/len(A)
print(avg)

#Q6
num=[1,2,3,4,5]
result=[]
for n in num:
    if n%2 ==1:
        result.append(n*2)
print(result)

#list 내포
result2=[]
result2=[n*2 for n in num if n%2 ==1]
print(result)
