#open() write() close()
f=open('C:/pyfile/hello.txt','w')
f.write('hello python')
#f.write(1000)

f.write('%.1f\n' % 5.3)
num='%d' % 10000
f.write(num)
f.write('안녕\n')
f.close()