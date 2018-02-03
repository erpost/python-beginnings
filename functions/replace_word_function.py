def censor(text, word):
    word_sub = '*' * len(word)
    print(text.replace(word, word_sub))

    return text.replace(word, word_sub)


censor('this hack is wack hack.', 'hack')
censor('the password is spam.', 'spam')
censor('hey hey hey.', 'hey')
