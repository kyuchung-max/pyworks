#dictionary
person={}
print(person)

person['name']='이순신'
person['age']=50

print(person)

person['address']='전라도'

for i in person:
    print(person)

del person['address']
print(person)
