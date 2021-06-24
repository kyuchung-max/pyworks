import random

for i in range(10):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    total=dice1+dice2
    print(total)
    if total==7:
        print('seven thrown')

    if total==11:
        print('eleven thrown')

    if dice1==dice2:
        print('double thrown')
