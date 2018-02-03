import re

EMAIL = re.compile(r'^From (\S*) (.*)')

with open('mbox-short.txt') as f:
    for line in f.readlines():
        line = line.rstrip()
        m = EMAIL.match(line)
        if m:
            print(line)