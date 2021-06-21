year= int(input('년도 입력: '))
if( ((year % 4 ==0) & year%100 !=0) | year%400 ==0):
    print("%d년은 윤년이다" % year)
else:
    print('%d년은 윤년이 아니다' %year)
    
    

