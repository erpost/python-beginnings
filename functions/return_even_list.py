def purify(lst):
    plst = []
    print(lst)
    for l in lst:
        if l % 2 == 0:
            plst.append(l)
        else:
            continue
    print(plst)
    return plst

purify([1, 2, 3, 4, 5, 6, 7])
