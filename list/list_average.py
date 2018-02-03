numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp.lower() == 'done':
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)