#with as: f.close()생략
with open('data.txt', 'w') as f:
    f.write('hello\n')
    f.write('%d\n' % 15000)
    unit='1 inch는 %.2fcm' % 2.54
    f.write(unit)

with open('data.txt', 'r') as f:
    data=f.read()
    print(data)