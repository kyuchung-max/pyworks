def oneup2(x):
    return x+1

oneup=lambda x: x+1
print(oneup(1))
print((lambda x:x+1)(3))

#print(oneup2(1))

#3의 배수
times=lambda n:n*3
print(times(2))
print((lambda n:n*3)(2))