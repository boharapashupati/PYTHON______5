class Car:                      # Class
    def __init__(self, color, model):
        self.color = color      # Attribute
        self.model = model      # Attribute
    
    def honk(self):             # Method
        print("BEEP BEEEP!")

# Creating an object
my_car = Car("Red", "Toyota")   # Object
my_car.honk() 
# Output: BEEP BEEEP!


#  class Car:
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