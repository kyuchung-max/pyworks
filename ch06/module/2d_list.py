#이차원 리스트

li = [ [10,20],
       [30,40],
       [50,60] ]
print('li[0][0]=', li[0][0])
print('li[0][1]=', li[0][1])
print('li[1][0]=', li[1][0])

print(len(li) )
'''
for x, y in li:
    print(x,y)
'''

for i in range(len(li) ):
    for j in range(len(li[i]) ):
        print(li[i][j], end=' ')
    print()
