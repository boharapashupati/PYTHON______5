# class Car:
#     def  __init__(self,color,model):
#         self.color = color 
#         self.model = model

#     def honk(self):
#         print("beep,beep")
    
#     def brake(self):
#         print("brake")
    
#     def accelerate(self):
#         print("accelerate")

#     def turn(self):
#         print("turn")


# my_car = Car("red", "toyota")
# my_car.honk()


# my_car.brake()
# my_car.accelerate()
# my_car.turn()


# how to dont use self in class method


class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner        # private variable
        self.__balance = balance    # private variable

    # Getter for owner
    def get_owner(self):
        return self.__owner

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Setter for deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    # Setter for withdraw
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid or Insufficient balance")

