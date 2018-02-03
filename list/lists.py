# List with 4 items

zoo_animals = ["pangolin","cassowary","sloth","tiger"];

if len(zoo_animals) > 3:
    print("The first animal at the zoo is the " + zoo_animals[0])
    print("The second animal at the zoo is the " + zoo_animals[1])
    print("The third animal at the zoo is the " + zoo_animals[2])
    print("The fourth animal at the zoo is the " + zoo_animals[3])

# Access individual item by index

numbers = [5, 6, 7, 8]

print("Adding the numbers at indices 0 and 2...")
print(numbers[0] + numbers[2])
print("Adding the numbers at indices 1 and 3…")
print(numbers[1] + numbers[3])

# Append items to list

suitcase = []
suitcase.append("sunglasses")
suitcase.append("socks")
suitcase.append("toothbrush")
suitcase.append("toothpaste")

list_length = len(suitcase) # Number of items in list

print("There are %d items in the suitcase." %(list_length))
print(suitcase)

# Find location in List

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck") # Finds location of duck in list
animals.insert(duck_index, "cobra") # Insert cobra in front of duck

print(duck_index)
print(animals)

# Multiply list with For Loop

my_list = [1,9,3,8,5,7]

for number in my_list: # List For Loop
    print(number * 2)

# Square and Sort List with For Loop

start_list = [5, 3, 1, 2, 4]
square_list = [] # Empty List

for number in start_list:
    square = number ** 2
    square_list.append(square)

square_list.sort() # Sort list
print(square_list)

my_list = [0, 1, 2, 3, 4, 5]
an_equal_list = [x for x in range(5)] # another way to create a list

multiply_list = [x * 3 for x in range(5)]
print(multiply_list)  # will iterate 0-4 and multiply each by 3