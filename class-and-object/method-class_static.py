class Students:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avg(self):
        return sum(self.marks) / len(self.marks)

    @classmethod    # Class Method
    def go_to_school(cls):
        print("I am going to school")

    @staticmethod    # Static Method
    def go_to_school():
        print("I am going to school")

anna = Students("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(90)
anna.marks.append(78)

Students.go_to_school()
