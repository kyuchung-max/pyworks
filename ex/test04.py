'''
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

#5qjs
f1=open('test.txt','w')
f1.write('life is too short')
f1.close()

f2=open('test.txt','r')
print(f2.read())
f2.close()

#6
user_input=input('입력')
f=open('test.txt','a')
f.write(user_input)
f.write('\n')
f.close()
'''

#7
f=open('test.txt','r')
body=f.read()
f.close()

body=body.replace('java','python')

