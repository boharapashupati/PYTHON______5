# my_dict = {'name': 'Pashupati', 'age': 22}
# print("Before clear:", my_dict)   # {'name': 'Pashupati', 'age': 22}

# my_dict.clear()                   # सबै elements हटाइयो

# print("After clear:", my_dict)    # {}


# # (dict.fromkeys )method -2
# # Keys list
# keys = ['name', 'age', 'gender']

# # dict.fromkeys() use to new dictionary create with keys and default value none
# new_dict = dict.fromkeys(keys)

# print("New dict without value:", new_dict)



# # Keys
# keys = ['name', 'age', 'country']
# # dict.fromkeys() use to new dictionary create with keys and default value 0

# # dict.fromkeys()le sabii key ma 0 value rakha xa 
# new_dict = dict.fromkeys(keys, 0)

# print("New dict with value 0:", new_dict)




# 3_method = dict.copy() use to copy the dictionary
#  explane: Copy() method lē dictionary kō shallow (sāmān'ya) copy banā'um̐ch
# Yasalē original dictionary kō exact nakkala banā'um̐cha, tara tyō alaga object huncha.

# yuta purano jhalo (dictionary) banauxau
# original_bag = {
#     "math": "Class 10 Book",
#     "science": "Class 9 Book"
# }

# # dict.copy() ley purano jhola ko nakalw banauxa  – trw new_bag ho 
# new_bag = original_bag.copy()

# # naya jhola ma yuta book (value) change garxau
# new_bag["math"] = "Class 12 Book"

# # aba herxau purano ra naya jhola ko vitrw ke xa vaenrw 
# print(" Original Bag:", original_bag)  # purano jhola ko book puranii xa
# print(" New Bag:", new_bag)            # new jhola  – math book fereko  xa




# # 4_method = dict.get() use to get the value of the key
# # explane: get() method lē dictionary bātō key kō value prāpt garna upayōg huncha.

# # student dictionary
# student = {
#     "name": "bipna",
#     "age": 23
# }

# # get() use garew "name" khojne – key xa vane  value firta
# print("Name:", student.get("name"))  # Output: bipna

# # get() use garew "age" khojne – key xa vane  value firta
# print("Age:", student.get("age"))    # Output: 23

# # get() use
# # garew "school" khojne – key छैन vane default value None firta
# print("School:", student.get("school", "Not Found"))  # Output: Not Found




# # 5_method = dict.items() use to get the key-value pairs of the dictionary.

# student = {
#     "name": "sirjana",
#     "age": 22,
#     "city": "Kathmandu"
# }

# # dict.items() lw sabii key-value joderw tuplw ma rakha xa
# # print(student.items())


# # loop use garerw
# for key, value in student.items():
#     print(f"{key}: {value}")



# # 6_method = dict.keys() use to get the keys of the dictionary.

# dict.keys() method use to get the keys of the dictionary
# student = { "name": "hello",  "age": 22,"city": "Kathmandu"}

# # dict.keys() le sabii key hru laii nikala
# keys = student.keys()

# # keys dekhuxa
# print("Keys:", keys)

# # For loop use garerw sabii key hru laii print garna sakinchha
# for key in student.keys():
#     print("Key:", key)


# # 7_method = dict.pop() use to remove the key-value pair from the dictionary.


# student = {
#     "name": "sarika",
#     "age": 22,
#     "city": "Kathmandu"
# }

# # key hataune ra  value line
# print("Removed age:", student.pop("age"))  

# # abako dictionary ma "age" xaina
# print("Now student:", student)

# # key xain vane default dine
# print("Removed grade:", student.pop("grade", "Not Found"))



# method_9# dict.update() use to update the dictionary with another dictionary or key-value pairs.

student = {
    "name": "Pashupati",
    "age": 22
}

# naya dictionary sanga update garne
student.update({"city": "Kathmandu", "age": 23})  # age overwrite हुन्छ

# aarko tarika key-value diyrw
student.update(gender="Male")

print("Final Student Dictionary:", student)
