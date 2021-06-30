try:
    f=open('c:/pyfile/hello.txt', 'r')
    data=f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print('파일 없음')