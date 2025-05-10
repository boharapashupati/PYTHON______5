#basic data type 
age = 21   #int
height = 5.9  #float
name ="alice"  #str
is_student = True #bool

#control structure



#conditional statement
if age > 18:
    print("Adult")
elif age == 18:
    print("Just an adult")
else:
    print("Not an adult")

    #for loop

for i in range(5): #Iterate from 0 to 4
    print(f"number {i}")

#while loop
count = 0
while count < 5:
    print("counting", count)
    count += 1

        #function
def greet(name):
    print(f"Hello, {name}!")

    #function call
    print(greet(name)) #Output: Hello, alice!
    