def is_odd(number):
    if number%2 == 1:
        return True
    else:
        return False


print(is_odd(3))
print(is_odd(4))


def avg_n(*args): #가변 매개 변수
    r=0
    for i in args:
        r += i
        print(i,r)
    return r/len(args)
print(avg_n(1,2,3,4))

print('you' 'need')