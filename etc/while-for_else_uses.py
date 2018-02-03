# for/else statements

fruits = ['banana', 'apple', 'orange', 'pear', 'tomato', 'grape']

print('You have...')
for f in fruits:
    if f == 'tomato':
        print('A tomato is not a fruit!')  # (It actually is.)
        break
    print('A', f)
else:
    print('A fine selection of fruits!')

####################################################################
print()

# while/else statements

import random

print('Lucky Numbers! 3 numbers will be generated.')
print('If one of them is a "5", you lose!')

count = 0
while count < 3:
    num = random.randint(1, 6)
    print(num)
    if num == 5:
        print('Sorry, you lose!')
        break
    count += 1
else:
    print('You win!')
