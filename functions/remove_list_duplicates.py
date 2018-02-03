def remove_duplicates(lst):
    lst2 = []
    print(lst)
    for l in lst:
        if l in lst2:
            continue
        else:
            lst2.append(l)
    print(lst2)
    return lst2


remove_duplicates([1, 1, 2, 2])
