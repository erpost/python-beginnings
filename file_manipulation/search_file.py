fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('b'):
        print(line)

# using continue

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('b'):
        continue
    print(line)