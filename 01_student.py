# Meet the Student

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student: {self.name}, Marks: {self.marks}")

s1 = Student("Areesha", 95)
s1.display()
