
# class parent:
#     def myMethod(self):
#         print("This is parent class method")
    
# class child(parent):
#     def yourMethod(self):
#         print("This is child class method")
    
# c = child()
# # c.yourMethod() 


# class Employee:
#     def __init__(self,name, salary):
#         self.__name = name
#         self.__salary = salary

#     def getName(self):
#         return self.__name
#     def getSalary(self):
#         return self.salary
    
# class SalesOfficer(Employee):
#     def __init__(self, name, salary,inc):
#         super().__init__(name, salary)
#         self.incnt  = inc
#     def getSalary(self):
#         return self.salary+self.incnt
    
# e1 = Employee("John", 50000)
# print("total salary for {}is rs.{}".format(e1.getName(), e1.getSalary()))

# s1 = SalesOfficer("John", 50000, 1000)
# print("total salary for {}is rs.{}".format(s1.getName(), s1.getSalary()))






class example:
    def add(sef, a=None, b=None,c=None):
        x= 0
        if a!= None and b!= None and c!=None:
            x= a+b+c
        elif a!= None and b!= None and c != None:
            x= a+b
        elif a is not None:
            return x
        

obj= example()

print(obj.add(10,20,30))    
print(obj.add(10,20))