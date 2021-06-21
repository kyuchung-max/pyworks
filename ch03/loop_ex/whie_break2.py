#while break
while True:
    print('반복 계속? y/n : ')
    answer= input()

    if answer == 'y' or answer == 'Y':
        print('반복 계속')

    elif answer=='n' or answer == 'N':
        print('반복 중단')
        break
    else:
        print('잘못 입력')
