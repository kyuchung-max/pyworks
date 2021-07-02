with open('scorelist.txt','a') as f:


    while True:
        try:

            key = input('성적을 저장?  y 누르면 입력 처리  n 누르면 입력 종료')
            if key == 'y':
                name = input('이름 :')
                kor = int(input('국어 :'))
                math = int(input('수학 :'))
                #avg = (kor + math) / 2

                f.write(name + ' ')
                f.write(str(kor) + ' ')
                f.write(str(math) + '\n')
               # f.write(str(avg) + '\n')
            elif key == 'n':
                break
            else:
                print('잘못 입력함. 다시 입력')
        except ValueError:
            print('잘못 입력, 다시 입력: ')
    print('입력 종료')