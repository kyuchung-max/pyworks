with open('2021kbo.txt','w') as f:
    team=['삼성','lg','기아','롯데']
    for i in team:
        f.write(i+'\n')

with open('2021kbo.txt','r') as f:
    #data=f.readlines()
    #rint(data)

    '''
    for i in range(4):
        data=f.readline().split()
        print(data)
    '''
    d2=[]
    for i in range(4):
        d2.append(f.readline().split())
    print(d2)