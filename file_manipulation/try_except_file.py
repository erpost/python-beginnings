fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('{} cannot be found'.format(fname))
    quit()

count = 0
for line in fhand:
    if line.startswith('c'):
        count += 1
print('There were {} objects found in {}'.format(count, fname))