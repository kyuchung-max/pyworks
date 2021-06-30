li=[1,2,3,4,5]

li2=map(lambda x:x*3,li)
print(list(li2) )
print(list(map(lambda x:x*3,li )))

li3=filter(lambda x:x<4,li)
print(list(li3) )
print(list(filter(lambda x:x<4,li)))