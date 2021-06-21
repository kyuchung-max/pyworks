#
age=int(input('나이 입력: '))
#charge=0

if age<8:
    print('취학 전 아동')
    charge=1000
elif age<14:
    print('초등학생')
    charge=2000
elif age<20:
    print('중고생')
    charge=3000
else:
    print('일반인')
    charge=4000

print('입장료 %d원' % charge)
    
