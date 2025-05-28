
# For loop भनेको programming मा प्रयोग हुने एउटा control structure हो जुन कुनै कामलाई बारम्बार (repeat) गर्न प्रयोग गरिन्छ।
# for loop

# for i in range(5): #Iterate from 0 to 4
#     print(f"Number:{i}")


# furits=["apple", "banana", "cherry"]
# for furits in furits:
#     print(furits)


# for leatter in "hello":
#     print(leatter)  #Output: h e l l o

# A for loop is used to iterate over a sequence (like a list, tuple, string, or range).



# square

# for i in range(10,20):
#     print(f"{i}square: {i**2}")

# qube
# for i in range(10,20):
#     print(f"{i}cube: {i**3}")



# even numbers
# जुन संख्या 2 ले बाँड्दा बाँकी (remainder) 0 आउँछ, त्यसलाई even number भनिन्छ।
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# for num in numbers:
#     if num % 2 == 0:
#         print(num)



# odd numbers
# जुन संख्या 2 ले बाँड्दा बाँकी (remainder) 1 आउँछ, त्यसलाई odd number भनिन्छ।
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# for num in numbers:
#     if num % 2 != 0:
#         print(num)




# odd or even 

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# for num in numbers:
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")


# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Yo even number ho.")
# else:
#     print("Yo odd number ho.")







# number = 36 
# print("number  =",number)
# if number% 2 == 0:
#     if number% 3 == 0:
#         print("Divisible by 3 and 2")

#     else:
#         print("Divisible by 2 but not by 3")
# else:
#     if number% 3 == 0:
#         print("Divisible by 3 but not by 2")
#     else:
#         print("Not divisible by 2 or 3")



# def weekday (n):
#     match n:
#         case 0: return "Monday"
#         case 1: return "Tuesday"
#         case 2: return "Wednesday"
#         case 3: return "Thursday"
#         case 4: return "Friday"
#         case 5: return "Saturday"
#         case 6: return "Sunday"
#         case _: return "Invalid day number"

# print(weekday(3))
# print(weekday(6))
# print(weekday(7))




# def greeting(details):
#     match details:
#         case[time,name]:
#             return(f"Good {time}, {name}!")
#         case[time,*names]:
#             msg=''
#             for name in names:
#                 msg+=f"Good {time}, {name}!\n"
#             return msg
# print(greeting(["morning", "Alice"]))
# print(greeting(["afternoon", "Bob"]))
# print(greeting(["evening", "Eve"]))           






# # condition 
# def weekday(n):
#     if n == 0:
#         return "Monday"
#     elif n == 1:
#         return "Tuesday"


#     elif n == 2:
#         return "Wednesday"
#     elif n == 3:
#         return "Thursday"
    
#     elif n == 4:
#         return "Friday"
    
#     elif n == 5:
#         return "Saturday"
#     elif n == 6:
#         return "Sunday"
    
#     else:
#         return "Invalid day number"
    

# print(weekday(3)) 
# print(weekday(6)) 
# print(weekday(7)) 
# print(weekday(0))  




# numbers = [12, 18, 20, 25, 36, 40]
# for number in numbers:
#     print("number =", number)
#     if number % 2 == 0:
#         if number % 3 == 0:
#             print("Divisible by 3 and 2")
#         else:
#             print("Divisible by 2 but not by 3")
#     else:
#         if number % 3 == 0:
#             print("Divisible by 3 but not by 2")
#         else:
#             print("Not divisible by 2 or 3")



# yuta loop vitrw arko loop use garnee 






Zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.  
Simple is better than complex.
Complex is better than complicated.'''

for char in Zen:
    if char not in 'aeiou':
        print(char, end=' ')
