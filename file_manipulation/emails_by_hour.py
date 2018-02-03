name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
lines = open(name)
lst = list()
hours = list()
counts = dict()
eml_hr = list()

for line in lines:
    if line.startswith('From '):
        lst.append(line.split(' ')[6])

for line in lst:
    hours.append(line.split(':')[0])

for hour in hours:
    counts[hour] = counts.get(hour, 0) + 1

for key, val in counts.items():
    newtup = (key, val)
    eml_hr.append(newtup)

eml_hr = sorted(eml_hr)

for key, val in eml_hr:
    print(key, val)
