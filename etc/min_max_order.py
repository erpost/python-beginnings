min_order = 1
max_order = 10
price_per_lb = 7.99

order_amount = int(input("Please enter the number of pounds of cheese you'd like (1-10 lbs): "))

total_cost = int(order_amount) * price_per_lb

if int(order_amount) >= min_order and order_amount <= max_order:
    print("Your total for", order_amount, "lbs of cheese is $", total_cost)
elif int(order_amount) < min_order:
    print("Your order of", order_amount, "lbs is below the minimum.  Please try again.")
else:
    print("Your order of", order_amount, "lbs is above the maximum.  Please try again.")