fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("We don't have a " + dict_key)

    description = fruit.get(dict_key, "We don't have a " + dict_key)
    print(description)
