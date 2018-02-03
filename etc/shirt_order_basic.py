sm_price = 6
med_price = 7
lg_price = 8
shirt_order = 0

size = input("What size shirt would you like: ")
quantity = input("How many shirts total: ")

if size.lower() == "s" or size.lower() == "small":
    shirt_order = int(sm_price) * int(quantity)
    print("Your total will be $", shirt_order)
elif size.lower() == "m" or size.lower() == "medium":
    shirt_order = int(med_price) * int(quantity)
    print("Your total will be $", shirt_order)
elif size.lower() == "l" or size.lower() == "large":
    shirt_order = int(lg_price) * int(quantity)
    print("Your total will be $", shirt_order)
else:
    print("Sorry, the size is not available ")