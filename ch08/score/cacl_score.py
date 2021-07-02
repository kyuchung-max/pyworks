with open('scorelist.txt','r') as f:
    d2=[]
    for i in range(3):
        d2.append(f.readline().split())
    print(d2)
    '''
    [
        ['a', '1', '1'], 
        ['b', '2', '2'], 
        ['c', '3', '3']]
    '''
    for i in range(3):
        d2[i][1]=int(d2[i][1]) #kor
        d2[i][2]=int(d2[i][2]) #math
        d2[i].append(d2[i][1]+d2[i][2]) #총점
        d2[i].append(d2[i][3]/2) #avg
    #print(d2)

    print('name  kor   math  total   avg')
    for i in range(3):
        print('{0} {1} {2} {3} {4}'.format(d2[i][0],d2[i][1],d2[i][2],d2[i][3],d2[i][4]))

    kor_sum=0
    math_sum=0
    for i in range(3):
        kor_sum += d2[i][1]
        math_sum += d2[i][2]
    print('kor: %.1f, math: %.1f' % (kor_sum/3, math_sum/3))