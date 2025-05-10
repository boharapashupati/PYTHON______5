# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount


#     def get_balance(self):
#         return self.__balance
    

#     # def withdraw(self, amount):
#     #     self.__balance -= amount

#     # def __str__(self):
#     #     return f"BankAccount(balance={self.__balance})"
    
#     account = BankAccount(100)
#     account.deposit(50)
#     print(account.get_balance())  



class student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        self.__age = age


stud = student('pashupati', 20)
print('Name:', stud.name, stud.get_age())
stud.set_age(20)

print('Name:', stud.name , stud.get_age())