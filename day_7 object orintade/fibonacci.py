
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = 20
for i in range(n):
    print(fibonacci(i))
           

