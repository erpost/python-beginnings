# Pass "add_two_numbers" into "methodception"

def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

print(methodception(add_two_numbers))

# Use lambda to pass function

print(methodception(lambda: 35 + 100))

# built-in Filter function

my_list =[13, 56, 77, 484]
print(list(filter(lambda x: x % 2 ==0, my_list)))

def negative_nums(x):
    return x % 2 != 0
print(list(filter(negative_nums, my_list)))

# Filter is identical to List Comprehension

print([x for x in my_list if x % 2 ==0])