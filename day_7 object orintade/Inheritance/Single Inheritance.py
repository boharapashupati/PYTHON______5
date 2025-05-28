# # parent class
# class Parent: 
#    def parentMethod(self):
#       print ("Calling parent method")

# # child class
# class Child(Parent): 
#    def childMethod(self):
#       print ("Calling child method")

# # instance of child
# c = Child()  
# # calling method of child class
# c.childMethod() 
# # calling method of parent class
# c.parentMethod() 



class person:
   def __init__(self,name,id):
      self.name=name
      self.id=id

   def get_details(self):
      return f"Name: {self.name},ID: {self.id}"
   

class student(person):
    def __init__(self,name,id,greade,courses):
      super().__init__(name,id)
      self.greade = greade
      self.name = name
      self.id = id   
      self.courses = courses


    def get_details(self):
      return f"Name: {self.name},ID: {self.id},  greade: {self.greade},  courses: {self.courses}"
    
student = student("pashupati", 843, "A", ["computer", "math", "english", "science"])
print(student.get_details())
   

