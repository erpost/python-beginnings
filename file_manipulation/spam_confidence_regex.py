import re

lst = []

with open('mbox-short.txt') as f:
    for line in f.readlines():
        line = line.rstrip()
        confidence = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
        if len(confidence) > 0:
            num = float(confidence[0])
            lst.append(num)
    print(max(lst))
