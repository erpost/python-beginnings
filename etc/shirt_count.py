# Module 4 - Section 3 - Task 2
# Program: Shirt Count

shirt_size = ""
sm_shirt = 0
med_shirt = 0
lg_shirt = 0

while shirt_size != "exit":
    shirt_size = input("What size shirt would you like [S M L].  Type \"exit\" when you are done: ").lower()
    if shirt_size == "s":
        sm_shirt += 1
        print("One small shirt ordered.")
    elif shirt_size == "m":
        med_shirt += 1
        print("One medium shirt ordered.")
    elif shirt_size == "l":
        lg_shirt += 1
        print("One large shirt ordered.")
    elif shirt_size != "exit":
        print("That is not a valid response.  Please try again\n")

print("You have ordered", sm_shirt, "small shirt(s),", med_shirt, "medium shirt(s) and", lg_shirt, "large shirt(s)")