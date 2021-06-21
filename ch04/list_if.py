#list의 합격 판정
score=[70,80,50,60,90,40]
index=0

for i in score:
    index +=1
    if i>= 60:
        
        print('%d번 합격' % index)

    else:
        print('%d번 불합격' % index)

print('='*40)
n = len(score)
for i in range(0,n):
    if score[i]>=60:
        print('%d번 합격' % (i+1))

    else:
        print('%d번 불합격' % (i+1))
