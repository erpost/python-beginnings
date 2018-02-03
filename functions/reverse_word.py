def reverse(x):
    drow = ''
    for i in range(len(x) -1, -1, -1):
        drow += x[i]
        i -= 1
    # print(drow)
    return drow


print(reverse('abcd'))

# ---------------------------------------- #
to_one_hundred = list(range(101))
# print(to_one_hundred)

backwards_by_tens = to_one_hundred[::-10]
print(backwards_by_tens)
