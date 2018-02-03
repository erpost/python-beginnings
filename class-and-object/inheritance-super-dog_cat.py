import random

class Animal(object):

    def __init__(self, name):
        self.name = name

class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Shih Tzu', 'Beagle', 'Mutt'])

    def fetch(self, thing):
        print("{} goes after the {}".format(self.name, thing))

d = Dog("Puck")

print(d.name)
print(d.breed)
d.fetch("stick")
