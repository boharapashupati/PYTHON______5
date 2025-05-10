# class student:
#     def __init__(self, name, topic, date, time,):  
#         self.__name = name
#         self.__topic = topic
#         self.__date = date  
#         self.__time = time
#         # private variables
        

#     def display(self):
#         print("Name:", self.__name)
#         print("Topic:", self.__topic)
#         print("Date:", self.__date)  
#         print("Time:", self.__time)
#         print("-----------------------------")


# student1 = student("bipan", "OOP", "2025-05-10", "04:18 PM")
# student2 = student("sapna", "Encapsulation", "2025-05-11", "04:10 PM")
# student3 = student("ashok", "Operators", "2025-05-12", "04:10 PM")
# student4 = student("partiva", "Lambda", "2025-05-13", "04:15 PM")


# student1.display()
# student2.display()
# student3.display()
# student4.display()


# # class Student:
# #     def __init__(self, name, topic, date, time):
# #         self.name = name
# #         self.topic = topic
# #         self.date = date
# #         self.time = time

# #     def display(self):
# #         print(f"{self.name} will present on '{self.topic}' at {self.time} on {self.date}")


# # student1 = Student("bipna", "OOP", "2025-05-10", "4:10 pM")
# # student1.display()






class parent:
    def myMethod(self):
        print("This is parent class method")
    
class child(parent):
    def yourMethod(self):
        print("This is child class method")
    
c = child()
c.yourMethod() 