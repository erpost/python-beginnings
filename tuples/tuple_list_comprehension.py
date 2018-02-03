c = {'a': 10, 'c': 22, 'b': 1}
lst = list()
#print(sorted([(v,k) for k,v in c.items()]))

lst = sorted([(v,k) for k,v in c.items()])
print(lst)

lst = sorted(lst, reverse=True)

for v, k in lst:
    print(k, v)