import re

with open('mbox-short.txt') as f:
    for line in f.readlines():
        line = line.rstrip()
        domain = re.findall('^From .*@([^ ]*)', line)  # match any non-whitespace character is [^ ]
        if len(domain) > 0:
            print(domain)
