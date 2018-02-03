open_file = open("romeo.txt")
dct = dict()
for line in open_file:
    for word in line.split():
        dct[word] = dct.get(word, 0) + 1

print(dct)
print()

bigcount = None
bigword = None
for word,count in dct.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)