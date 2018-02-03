counts = {'chuck': 1, 'fred': 42, 'jan': 100}

for key in counts:
    print(key, counts[key])

print('_________________________________\n')

once  = {'a': 1, 'b': 2}
twice = {'a': 2, 'b': 4}

for key in once:
    print("Once: %s" % once[key])
    print("Twice: %s" % twice[key])

print('_________________________________\n')

prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

total = 0

for key in prices:
    total += prices[key] * stock[key]
    print(key)
    print('price: ${}'.format(prices[key]))
    print('stock: {}'.format(stock[key]))
print('Total: ${}'.format(total))

print('_________________________________\n')

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            stock[item] -= 1
            total += prices[item]
        print(item, stock[item])
    return (total)


print(compute_bill(shopping_list))
