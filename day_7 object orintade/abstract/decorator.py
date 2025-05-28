# # def my_function(x):
# #     print("The number is=",x)

# # def my_decorator(some_function, num):
# #     def wrapper(num):
# #         print("Inside Wrapper to check odd/even")
# #         if num%2 == 0:
# #             ret = "Even"
# #         else:
# #             ret = "Odd"
# #         some_function(num)
# #         return ret
# #     print ("wrapper function is called")
# #     return wrapper

# # no=10
# # my_function = my_decorator(my_function, no)
# # print ("It is ",my_function(no))

# def my_decorator(some_function):
#     def wrapper(num):
#         print("Inside Wrapper to check odd/even")
#         if num%2 == 0:
#             ret = "Even"
#         else:
#             ret = "Odd"
#         some_function(num)
#         return ret
#     print ("wrapper function is called")
#     return wrapper

# @my_decorator
# def my_function(x):
#     print("The number is=",x)
# no=10
# print ("It is ",my_function(no))






from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

d = Dog()
d.make_sound()  # Output: Bark
# c = Cat()
# c.make_sound()