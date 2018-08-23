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

import collections

for key in dict:
    if type(dict[key]) is int:
        print(key, ':', dict[key])
    else:
        print(key, ':', dict[key])
