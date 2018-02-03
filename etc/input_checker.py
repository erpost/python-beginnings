print('Welcome to input checker!')
original = input("Enter a word:")

if len(original) > 0:							# Checks that something was inputted
    print(original)
else:
    print("Your input is empty")


print('Welcome to alphabetical input checker!')
original = input("Enter a word:")
if len(original) > 0 and original.isalpha():	# Checks that only alphabetical characters are inputted
    print(original)
else:
    print("This is not a word")