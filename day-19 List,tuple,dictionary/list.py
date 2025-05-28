# # str1 ="Hello"
# # str2 = "World"
# # blank
# # print("string 1:", str1)
# # print("string 2:", str2)
# # str3 = str1-str2
# # print("string 3:",str



# # newString ="HELLO"*3
# # print(newString)



# str1 = "Hello"
# str2 = "World"
# print("string 1:",str1)
# print("string 2:",str2)
# str3 = str1+str2*3
# print("string 3:",str3)
# str4 = (str1+str2)*3
# print("string 4:",str4)



def is_palindrome(text):
    return text == text[::-1]

# Example usage:
word = input("Enter a word: ")

if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
