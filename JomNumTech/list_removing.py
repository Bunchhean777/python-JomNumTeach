
# Remove elements from a list.
name = ['user1','user2','user3','user4']

# Removes the first occurrence of an elements
name.remove('user1')
print("After remove 'user1' : ",name)

# Removes the element at a specific index or the last element it n index is specified
popped_value = name.pop(1)
print("Popped element: ",popped_value)
print("After pop: ",name)

# del statment deletes an element at a specified index.
del name[2]

# Iterating over lists
for list_name in name:
    print(list_name)