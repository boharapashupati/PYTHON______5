 

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))  

    

# def greet (name):
    
#     return f"Hello, {name}!"
# print(greet("Alice"))  


# fibonaccihw


# docstring 


n = int(input("How many terms? "))
a, b = 0, 1

for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
