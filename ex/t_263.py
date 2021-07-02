
def positive(a):
    a2=[]
    for i in a:
        if i>=0:
            a2.append(i)
    return a2

print(positive([1,-1]))


li=[1,2,3,4,5]
print(list(map(lambda x:x*3,li)))