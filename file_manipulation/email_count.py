open_file = open('mbox-short.txt')
count = 0

for line in open_file:
    if line.startswith('From '):
        line = line.rstrip()
        count +=1
        print(line.split(' ')[1]) # split and print location 1 on the same line

print('There were {} lines in the file with From as the first word'.format(count))