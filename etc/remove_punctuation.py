import string

def no_punct(data):
    exclude = set(string.punctuation)
    data = ''.join(ch for ch in data if ch not in exclude)
    return data


print(no_punct("Hello, this is my favorite line... Eric is cool! :)"))
