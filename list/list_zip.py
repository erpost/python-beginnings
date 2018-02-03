list = [1, 2, 3]
list2 = [4, 5, 6]

for x,y in zip(list, list2):
    print(x,',',y)

###################################################
print()

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a > b:
        print(a)
    else:
        print(b)
