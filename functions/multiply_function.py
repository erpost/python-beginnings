def product(nums):
    total = 0
    print(nums)
    for n in nums:
        if total == 0:
            total = n
        else:
            total *= n
    print(total)
    return total

product([4, 5, 5])

# ---------------------------#

def product(nums):
    total = 1
    print(nums)
    for n in nums:
        total *= n
    print(total)
    return total

product([4, 5, 5])

# ---------------------------#

def multiply(num1, num2):
    multiply = int(num1) * int(num2)
    return multiply


num1 = input("Please provide a whole number: ")
num2 = input("And provide a second whole number: ")

answer = multiply(num1, num2)

print(num1, "*", num2, "is:", str(answer))