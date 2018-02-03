def preword(prefix):
    word = input("Enter a word that begins with 'Pre': ").lower()

    if word.isalpha():
        if word[0:3] == prefix:
            print("This is a valid word")
            return True
        else:
            print("Not a valid word")
            return False
    else:
        print("Not a valid word")
        return False

# % time preword("pre")
preword("pre")
