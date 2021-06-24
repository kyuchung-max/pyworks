def avg(a):
    sum=0
    c = len(a)
    for i in a:
        sum += i
        print('i= %d, sum= %d' % (i, sum))
        avg = sum/c
    return avg

avg= avg([70,80,90,100])
print('평균 :', avg)
