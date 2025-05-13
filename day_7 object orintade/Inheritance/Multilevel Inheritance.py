# # parent class
# class Universe: 
#    def universeMethod(self):
#       print ("I am in the Universe")

# # child class
# class Earth(Universe): 
#    def earthMethod(self):
#       print ("I am on Earth")
      
# # another child class
# class India(Earth): 
#    def indianMethod(self):
#       print ("I am in India")      

# # creating instance 
# person = India()  
# # method calls
# person.universeMethod() 
# person.earthMethod() 
# person.indianMethod() 



class Animal:
   def __init__(self,species):
      self.species = species
      
   def eat(self):
      return f"{self.species} is eating"
   
class Mammal(Animal):
   def __init__(self, species, fur_color):
      super().__init__(species)
      self.fur_color = fur_color
      
   def breath(self):
      return f"{self.species} breathes air "
   
class Dog(Mammal):
   def __init__(self, species, fur_color, name):
      super().__init__(species, fur_color)
      self.name = name
      
   def bark(self):
      return f"{self.species} says woof!                          "
      

my_dog = Dog("Dog", "Brown", "Buddy")
print(my_dog.eat())  # Dog is eating
print(my_dog.breath())  # Dog breathes air   
print(my_dog.bark())  # Dog says woof!
