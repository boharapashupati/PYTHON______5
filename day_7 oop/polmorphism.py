# class Duck:
#     def sound(self):
#         print("quack","quack")

# class anotherBrid:
#     def sound(self):
#         return "I am similar to duck"
    
# def makesound(duck):
#     print(duck.sound())


# duck = Duck()
# another = anotherBrid()

#     # calling method of duck class
# makesound(duck)
# makesound(another)



from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def draw(self):
        "Abstract ,method"


class circle(Animal):
    def draw(self):
        print("Drawing a circle")
        return
    
class rectangle(Animal):
    def draw(self):
        super().draw()
        print("Drawing a rectangle")
        return
    
shapes = [circle(), rectangle()]
for shape in shapes:
    shape.draw()
        