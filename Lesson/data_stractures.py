# 1 Write a Python program to sum all the items in a list.
mylist = [1, 2, 3, 3, 4, 5]
total = sum(mylist)
print("Sum of the list:", total)

# 2 Write a Python program to remove duplicates from a list.
mylist = [1, 2, 3, 3, 4, 5]
unique_list = list(set(mylist))
print("List after removing duplicates:", unique_list)

# 3 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.
mylist = [1, 2, 3, 3, 4, 5]
# Indices to remove: 0, 4, 5
indices_to_remove = {0, 4, 5}
filtered_list = [item for i, item in enumerate(mylist) if i not in indices_to_remove]
print("Filtered list:", filtered_list)

# 4 Write a Python program to get the difference between the two lists.
mylist = [1, 2, 3, 3, 4, 5]
mylist2 = [1, 2, 7]
difference = list(set(mylist) - set(mylist2))
print("Difference between lists:", difference)

# 5 Write a Python program to convert a tuple to a dict.
mytuple = ("green", "red", "black", "blue")
# Convert tuple to dictionary with keys as indices
mydict = {i: mytuple[i] for i in range(len(mytuple))}
print("Tuple converted to dictionary:", mydict)

# 6 Write a Python program to add a key to a dict.
mydict = {"a": "1", "b": "2", "c": "3"}
mydict["d"] = "4"  # Add a new key-value pair
print("Dictionary after adding a key:", mydict)

# 7 Write a Python program to remove a key from a dict.
mydict = {"a": "1", "b": "2", "c": "3"}
del mydict["b"]  # Remove the key "b"
print("Dictionary after removing a key:", mydict)

# 8 Write a Python program to get the maximum and minimum value in a dict.
mydict = {"a": "1", "b": "2", "c": "3"}
values = [int(value) for value in mydict.values()]
print("Max value:", max(values))
print("Min value:", min(values))

# 9 Write a Python program to create a difference of two sets and print the result.
set1 = {1, 2, 3, 4, 5}
set2 = {1, "b", "c", "d", "e"}
difference_set = set1.difference(set2)
print("Difference of sets:", difference_set)
