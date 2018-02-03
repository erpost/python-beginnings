# Dictionaries

# Print Dictionary and Type

my_dict = {'name': 'Jose', 'age': 90, 'grades': [13, 45, 66, 90]}

print(my_dict)
print(type(my_dict))

# Tuple Within Dictionary & Print Sum

lottery_player = {
    'name': 'Rolf',
    'numbers': (13, 45, 66, 23, 22)
}

print(sum(lottery_player['numbers']))

# Print only Even Numbers in Range

print([n for n in range(11) if n % 2 == 0])

people_you_know = ["Rolf", " John", "anna", "GREG"]
normalized_people = [person.strip().lower() for person in people_you_know]

print(normalized_people)

# Print Values from Keys

residents = {'Puffin': 104, 'Sloth': 105, 'Burmese Python': 106}

print(residents['Puffin'])
print(residents['Sloth'])
print(residents['Burmese Python'])

# Dictionaries Within List

universities = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'US'
    }
]
