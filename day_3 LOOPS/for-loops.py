
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


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Yo even number ho.")
else:
    print("Yo odd number ho.")






