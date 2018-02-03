open_file = open("romeo.txt")
lst = list()
for line in open_file:
    for word in line.split():
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
