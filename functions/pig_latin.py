def pigLatin():
    print("Welcome to Pig Latin")
    answer = input("Input a word and hit 'Enter': ")
    print("Your word in Pig Latin is:")
    print(answer[1:].capitalize() + answer[:1].lower() + "ay")
pigLatin()