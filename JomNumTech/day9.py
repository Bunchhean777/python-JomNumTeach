# Control flow statements (cont.)
# for each loop:
# > enumerate() : loop and through both value and index of an iterable at the same time.
# > zip() : allow you unzip a list of tuples or paired data.

# using loop for each item in a list
# fruits = ["Apple", "Banana", "Mango", "Orange"]
# for i, fruit in enumerate(fruits):
#     print(f"Index: {i}, Fruit name is: {fruit}")

# sequence
# for o in fruits:
#     print(f"Fruit name is: {o}")

# enumerate() method in for each loop:
pruducts_data = [
    {"id":101,"name":"coca","price": 2000},
    {"id":102,"name":"pepsi","price": 2000},
    {"id":103,"name":"ABC","price": 5000},
    {"id":104,"name":"Hanuman","price": 2500},
    {"id":105,"name":"Tiger","price": 2500},
]
print("\n@ List of products :")
for index,product in enumerate(pruducts_data):
    print(f"> Index of products {index} : ID: {product['id']}, Name: {product['name']}, Price: {product['price']}")

print('-'*60)

# zip() method in for each loop:
names = ["jabs","joe"]
ages = [12,24,12]
emails = ["user@gmail.com","joe@gmail.com"]

for name,age,email in zip(names,ages,emails):
    print(f"> Student info : ({name},{age},{email})")
