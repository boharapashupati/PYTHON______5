
# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 4, 5]
# c = a 
 
# print(a is c )
# print(a is b )


# print("id(a):", id(a))
# print("id(b):", id(b))
# print("id(c):", id(c))




#  identity operator
# a ="pashupati"
# b ="pashupati"
# c = a

# print(a is b)
# print(a is c)

# print("id(a):", id(a))
# print("id(b):", id(b))
# print("id(c):", id(c))

a = "pashupati"
b = "pashupati"
print(a is b)  # True, because both variables point to the same string object in memory
print(a is not b)  # False, because both variables point to the same string object in memory
print(a == b)  # True, because the values of both variables are equal
print(a != b)  # False, because the values of both variables are equal
