def median(lst):
    print(lst)
    slst = sorted(lst)
    print(slst)
    if len(slst) % 2 != 0:
        med = int(len(slst) / 2)
        print('index= ', med)
        print(slst[med])
        return slst[med]
    else:
        med1 = int(len(slst) / 2) - 1
        med2 = int(len(slst) / 2)
        print('indices= ', med1, ',', med2)
        print(slst[med1], '+', slst[med2], '=', (slst[med1] + slst[med2]) / 2)
        return (slst[med1] + slst[med2]) / 2.0


median([4, 5, 5, 4])
median([-1, 2, 6, -5, 4, 2, 9])
