# Simple Object

class LotteryPlayer:
    def __init__(self):
        self.name = "Rolf"
        self.numbers = (5, 9, 12, 3, 1, 21)

    def summation(self):  # Creating a Method within the Object
        return sum(self.numbers)

    def total(self):  # Creating a Method within the Object
        return len(self.numbers)


player = LotteryPlayer()

print(player.name)
print(player.numbers)
print(player.summation())
print(player.total())

# Multiple Objects

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def summation(self):  # Creating a Method within the Object
        return sum(self.numbers)

    def total(self):  # Creating a Method within the Object
        return len(self.numbers)


player_one = LotteryPlayer("Rolf")
player_two = LotteryPlayer("James")


print(player_one.name)
print(player.numbers)
print(player_two.name)
print(player_two.numbers)