


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




class person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        return f"hello, my name is {self.name}"
    
class Empoloyee:
    def __init__(self,employee_id):
        self.employee_id=employee_id        
    def get_id(self):
        return f"my employee id is {self.employee_id}"

class Manager(person,Empoloyee):
    def __init__(self, name, employee_id,department):
        person.__init__(self,name)
        Empoloyee.__init__(self,employee_id)
        self.department=department
    
    def show_details(self):
        return f"{self.greer()} and my employee id is {self.get_id()} and I am in {self.department} department"
    

m=Manager("Alice", 101, "sales")
print(m.greet())
print(m.get_id())
print(m.show_details())

 
