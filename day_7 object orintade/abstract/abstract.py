# from abc import ABC , abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

#     def perimeter(self):
#         return 2 * 3.14 * self.radius
    

# Circle = Circle(5)
# print(f"Area: {Circle.area()}")
# print(f"Perimeter: {Circle.perimeter()}")

class Animal:

    def speak(self):

        print("Animal speaks")

class Dog(Animal):

    def speak(self):

        print("Dog barks")

dog = Dog()

dog.speak()