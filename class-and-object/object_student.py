class Students:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avg(self):
        return sum(self.marks) / len(self.marks)

    def go_to_school(self):
        print("{} is going to {}.".format(self.name, self.school))

anna = Students("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(90)
anna.marks.append(78)

print(anna.name)
print(anna.school)
print(anna.marks)
print(anna.avg())
anna.go_to_school()