import sys

print('input number')
n=int(input())
if n==0:
    print('0으로 나눌수 없음')
    sys.exit()
print(3/n)