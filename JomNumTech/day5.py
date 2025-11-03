
# Arithmetic Operators
num1 = 10
num2 = 6
print("\n+ Arithmetic Operators:")
print(f"Addition: {num1 + num2}")          
print(f"Subtraction: {num1 - num2}")       
print(f"Multiplication: {num1 * num2}")    
print(f"Division: {num1 / num2:.2f}")          
print(f"Floor Division: {num1 // num2}")   
print(f"Modulus: {num1 % num2}")           
print(f"Exponentiation: {num1 ** num2}")   
# Assignment Operators
a = 5
a += 3  
print("\n+ Assignment Operators:")
print("a += 3:", a)
a -= 2
print("a -= 2:", a)
# Comparison Operators
print("\n+ Comparison Operators:")
x = 15
y = 10
print(f"x == y : {x == y}")   
print(f"x != y : {x != y}")      
print(f"x > y : {x > y}")     
print(f"x < y : {x < y}")     
print(f"x >= y : {x >= y}")   
print(f"x <= y : {x <= y}")   

# Logical Operators
print("\n+ Logical Operators:")
print(f"x > 10 and y < 20 : {x > 10 and y < 20}")
print(f"x > 10 or y < 20 : {x > 10 or y < 20}")
print(f"not (x > 10) : {not (x > 10)}")

# Mebership Operators
print("\n+ Membership Operators:")
programming_languages = ["Python", "Java", "C++", "JavaScript"]
print(f"Java in programming_languages : {'Java' in programming_languages}")
print(f"Ruby not in programming_languages : {'Ruby' not in programming_languages}")
print(f"C++ in programming_languages : {'C++' in programming_languages}")

# Indentity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("\n+ Identity Operators:")
print(f"true (a is b) : {a is b}")
print(f"false (a is c) : {a is c}")