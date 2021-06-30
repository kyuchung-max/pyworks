import random

com=random.randint(1,30)
while True:
    try:

        guess=int(input('맞혀 보세요(1~30): ') )
        if  guess>30 or guess<1:
            print('범위를 벗어남, 다시 입력: ')
        if com > guess:
            print('너무 작아요')

        elif com < guess:
            print('너무 커요')

        elif com == guess:
            print('정답')
            break
    except ValueError:
        print('숫자가 아님, 다시 입력: ')

