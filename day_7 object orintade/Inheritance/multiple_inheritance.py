


# class division:
#     def __init__(self, a,b):
#         self.n=a
#         self.d=b
#     def divide(self):
#         return self.n/self.d
# class modulus:
#     def __init__(self, a,b):
#         self.n=a
#         self.d=b
#     def mod_divide(self):
#         return self.n%self.d
    
# class div_mod(division,modulus):
#     def __init__(self, a,b):
#         self.n=a
#         self.d=b
#     def div_and_mod(self):
#         divval=division.divide(self)
#         modval=modulus.mod_divide(self)
#         return (divval, modval)


# x = div_mod(10,3)
# print("division:", x.divide())
# print("modulus:", x.mod_divide())
# print("divmod:",x.div_and_mod())




# class person:
#     def __init__(self,name):
#         self.name=name
#     def greet(self):
#         return f"hello, my name is {self.name}"
    
# class Empoloyee:
#     def __init__(self,employee_id):
#         self.employee_id=employee_id        
#     def get_id(self):
#         return f"my employee id is {self.employee_id}"

# class Manager(person,Empoloyee):
#     def __init__(self, name, employee_id,department):
#         person.__init__(self,name)
#         Empoloyee.__init__(self,employee_id)
#         self.department=department
    
#     def show_details(self):
#         return f"{self.greet()} {self.get_id()} i manage the  {self.department} department"
    

# m=Manager("Alice", 101, "sales")
# print(m.greet())
# print(m.get_id())
# print(m.show_details())

 
class Person:
    def __init__(self, name):
        self.name = name
        print("Person init called")

    def greet(self):
        return f"Hello, my name is {self.name}"

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id
        print("Employee init called")

    def get_id(self):
        return f"My employee ID is {self.employee_id}"

class Manager(Person, Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name)  # This only calls Person's __init__
        Employee.__init__(self, employee_id)  # Need to call explicitly or redesign classes
        self.department = department

    def show_details(self):
        return f"{self.greet()} {self.get_id()} I manage the {self.department} department"
    
    
m=Manager("Alice", 101, "sales")
print(m.greet())
print(m.get_id())
print(m.show_details())
