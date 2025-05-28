# Parent Class
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

# Child Class
class Student(Person):
    def __init__(self, name, age, address, college, major):
        super().__init__(name, age, address)  # Inherit from Person
        self.college = college
        self.major = major

    def display_student_info(self):
        self.display_info()  # Call parent method
        print(f"College: {self.college}")
        print(f"Major: {self.major}")

# Creating an object of Student class
me = Student("pashupati", 19, "Kathmandu, Nepal", "TU", "Computer Engineering")

# Displaying the information
me.display_student_info()
