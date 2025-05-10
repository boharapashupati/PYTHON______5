# n = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"
# print(n(5))  # Output: positive
# print(n(-3))  # Output: negative        
# print(n(0))  # Output: zero

# calc = lambda x, y:(x+y,x*y)
# res = calc(5, 3)
# print(res) 
# print(res[0])  # Output: 8

# number = [1, 2, 3, 4, 5]
# even = filter(lambda x: x % 2 == 0, number)
# print(list(even))  # Output: [2, 4]


# a = [1, 2, 3, 4, 5]
# b = map(lambda x: x * 2, a)
# print(list(b))  # Output: [2, 4, 6, 8, 10]


def describe_persona(**kwarge):
    for key,value in kwarge.items():
        print(f"{key.captitalize()}: {value}")
    
describe_persona(name="Alice", age=30, city="New York")


