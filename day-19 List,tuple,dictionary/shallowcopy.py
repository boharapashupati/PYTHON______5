import copy 
original_list =[   [1, 2, 3, 4, 5] ,[6, 7, 8, 9, 10], [11, 12, 13, 14, 15] ]
shallow_copied_list = copy.copy(original_list)
shallow_copied_list[0][0] = 100  # Modifying the first element of the first sublist
print("Original List after modification:", original_list)
print("Shallow Copied List after modification:", shallow_copied_list)