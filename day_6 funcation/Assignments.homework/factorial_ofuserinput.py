# def factorial(n):    
# 	if n < 0:        
# 		print("Negative numbers not allowed.")    
# 	else:            
# 		if n == 1 or n == 0:            
# 			return 1        
# 		else:            
# 			return n * factorial(n-1)
			
# n = int(input("Enter the number: "))
# print(factorial(n))


# def printme(str):
# 	print(str)
# 	return

# printme("Hello")
# printme("Welcome to python programming")















def factorial(n):
    if n == 1:
        return 1        #  base case
    else:
        return n * factorial(n - 1)   # recursive call

print(factorial(5))
