 
# # my_set = {10, 20, 30, 40, 50}
# # x = 30

# # if x in my_set:
# #     print(f"{x} is in the set.")
# #     my_list = list(my_set)
# #     index = my_list.index(x)
# #     print(f"{x} is in the set: {index}")
# # else:
# #     print(f"{x} is not in the set.")

# # Step 1: Create a set
# my_set = {"apple", "banana", "cherry", "orange"}

# # Step 2: Convert the set to a list to maintain index positions
# my_list = list(my_set)

# # Step 3: Take user input
# user_input = input("Enter a fruit name: ")

# # Step 4: Check if it exists in the set
# if user_input in my_set:
#     index = my_list.index(user_input)
#     print(f"'{user_input}' exists in the set at position {index}")
# else:
#     print(f"'{user_input}' does not exist in the set.")


# printing my name using asterisk
def my_name():
    t=["*********" ,"****" ,"*      *"  ,"*****" ,"*****"]
    s=["    *    " ,"*   " ,"* *    *"  ,"  *  " ,"  *  "]
    x=["    *    " ,"*** " ,"*   *  *"  ,"  *  " ,"  *  "]
    y=["    *    " ,"*   " ,"*    * *"  ,"  *  " ,"  *  "]
    p=["    *    " ,"****" ,"*      *"  ,"***  " ,"*****"] 
    first_name=[t,s,x,y,p]
    for Tenji in first_name: 
        print(Tenji)
my_name()