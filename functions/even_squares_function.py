def even_squares(first, last):
    even = [x ** 2 for x in range(first, last) if (x ** 2) % 2 == 0]

    return even


print(even_squares(1, 11))
