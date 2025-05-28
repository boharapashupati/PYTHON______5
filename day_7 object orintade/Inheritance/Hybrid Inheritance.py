# class Manager(CEO): 
#    def managerMethod(self):
#       print ("I am the Manager")

# class Employee1(Manager): 
#    def employee1Method(self):
#       print ("I am Employee one")
      
# class Employee2(Manager, CEO): 
#    def employee2Method(self):
#       print ("I am Employee two")      

# # creating instances 
# emp = Employee2()
# # method calls
# emp.managerMethod() 
# emp.ceoMethod()
# emp.employee2Method()



class Animal:
    def speak(self):
        print("Animals can make sound!  ")

class Dog(Animal):
      def bark(self):
         print("Dog barks!  ")

class Cat(Animal):
      def meow(self):
         print("Cat meows!  ")
   
class HybridAnimal(Dog, Cat):
      def hybrid_sound(self):
         print("Hybrid animal can bark and meow!  ")

my_hybrid_animal = HybridAnimal()
my_hybrid_animal.speak()  # Inherited from Animal
my_hybrid_animal.bark()   # Inherited from Dog
my_hybrid_animal.meow()   # Inherited from Cat
my_hybrid_animal.hybrid_sound()  # Method of HybridAnimal

    