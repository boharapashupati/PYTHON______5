class Employee:
    def __init__(self, name, age,salary):
        self.name = name  # public variable
        self.age = age # private variable
        self.salary = salary # protected variable
def display(self):
    print("Name:", self.name, "Age:", self.age, "Salary:", self.salary)
    e1 = Employee("Alice", 50000)
    print(e1.name) 
    print(e1.age)
    print(e1.salary)  


