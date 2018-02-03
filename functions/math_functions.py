while True:
    operator = input("To multiply or divide, please select * or /: ")
    if operator == "/" or operator == "*":
        break
    else:
        print("That is an invalid operator, please try again\n")


def math_function(num1, num2):
    if operator == "*":
        math_function = int(num1) * int(num2)
        return math_function

    elif operator == "/":
        math_function = int(num1) / int(num2)
        return math_function


num1 = input("Please provide a whole number: ")
num2 = input("And provide a second whole number: ")
answer = math_function(num1, num2)

print(num1, operator, num2, "is:", str(answer))
