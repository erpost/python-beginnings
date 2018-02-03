import re

lst = []

with open('sum_42.txt') as f:
    for line in f.readlines():
        num = re.findall('([0-9]+)', line)
        for i in num:
            i = int(i)
            lst.append(i)
print(sum(lst)) # should equal 445833

lst2 = []

with open('sum_21291.txt') as f:
    for line in f.readlines():
        num = re.findall('([0-9]+)', line)
        for i in num:
            i = int(i)
            lst2.append(i)
print(sum(lst2)) # should equal 379339