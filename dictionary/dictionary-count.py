names = ['csev', 'cwen', 'csev', 'zqian', 'cwen', 'csev']
counts = dict()

# long way

for name in names:
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
print(counts)

# short way using "get" method

for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
