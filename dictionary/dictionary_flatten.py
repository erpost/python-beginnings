from flatten_dict import flatten


dict = {
    'a': 5,
    'b': 6,
    'c': {
        'f': 9,
        'g': {
            'm': 17,
            'n': 3
        }
    }
}

print(flatten(dict))
