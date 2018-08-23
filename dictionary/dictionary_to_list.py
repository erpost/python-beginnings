dct = {'chuck': 1, 'fred': 42, 'jan': 100}

# print dictionary
print(dct)

# change dictionary keys into list
print(list(dct))

# change dictionary keys into list with method
print(dct.keys())
print(list(dct.keys()))

# change dictionary values into list with method
print(dct.values())
print(list(dct.values()))

# change dictionary into tuple with method
print(dct.items())
p_tuple = tuple(dct.items())
print(p_tuple)


# change dictionary keys into sorted list
for d in sorted(dct.keys()):
    print(d, '-', dct[d])
