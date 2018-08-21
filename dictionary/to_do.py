#Flattening a dictionary.
# Given the following dictionary:

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

# Let's write a function that will flatten the dictionary above into something like:

# {
#   'a': 5,
#   'b': 6,
#   'c.f': 9,
#   'c.g.m': 17,
#   'c.g.n': 3,
# }

from flatten_dict import flatten

print(flatten(dict))

# for key in dict:
#     if type(dict[key]) is int:
#         print(key, ':', dict[key])
#     else:
#         print()

/Users/erpost/.python/venv/bin/python "/Users/erpost/Library/Mobile Documents/com~apple~CloudDocs/Python/python-beginnings/dictionary/to_do.py"
{('c', 'g', 'm'): 17, ('b',): 6, ('c', 'f'): 9, ('a',): 5, ('c', 'g', 'n'): 3}