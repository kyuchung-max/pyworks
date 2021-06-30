while True:
    try:
        x=int(input('술자 입력: '))
        print(x)
        break
    except ValueError:
        print('숫자가 아님, 다시 입력:')