def who_do_you_know():
    people = input("Who do you know? (Separate names with a comma: ")
    people_normalized = [person.strip().lower() for person in people.split(",")]
    return people_normalized

who_list = who_do_you_know()

def ask_user():
    person = input("Input the name of a person you know: ")
    if person.strip().lower() in who_list:
        print("You know {}!".format(person))
    else:
        print("Sorry, you don't know {}!".format(person))

ask_user()

# Alternate Option: Embedding Function in Another Function

def who_do_you_know():
    people = input("Who do you know? (Separate names with a comma: ")
    people_normalized = [person.strip().lower() for person in people.split(",")]
    return people_normalized

def ask_user():
    person = input("Input the name of a person you know: ")
    if person.strip().lower() in who_do_you_know():
        print("You know {}!".format(person))
    else:
        print("Sorry, you don't know {}!".format(person))

ask_user()
