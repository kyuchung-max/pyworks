customer_num=int(input('입장객 수 입력: '))
col_num=int(input('좌석 열 수 입력: '))
#row_num = customer_num / col_num

if customer_num % col_num ==0:
    row_num= int(customer_num/col_num)
else:
    row_num= customer_num//col_num +1
    #row_num= int(customer_num/col_num +1)
#print(row_num, '개의 줄이 필요')

print('자리 배치도')
for i in range(0,row_num):
    for j in range(1,col_num+1):
        seat_num=i*col_num+j
        print(seat_num, end=' ')
        if seat_num >= customer_num:
            break;
    print() #다음 줄 프린트
