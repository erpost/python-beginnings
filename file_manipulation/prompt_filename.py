fname = input('Enter the file name: ')
fhand = open(fname)
count = 0

for line in fhand:
    if line.startswith('c'):
        count += 1
print('There were {} objects found in {}'.format(count, fname))