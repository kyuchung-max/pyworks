a= 'life is too short, you need python'
if 'wife'in a: print('wife')
elif 'python' in a and 'you' not in a: print('python')
elif 'shirt' not in a: print('shirt')
elif 'need'in a: print('need')

i= 0
while True:
    i += 1
    if i>5  :break
    print(i*'*')

i= 0
for i in range(1,6):
    for j in range(1,i+1):
        print('*', end='')
    print()

for i in range(1,101):
    print(i)
