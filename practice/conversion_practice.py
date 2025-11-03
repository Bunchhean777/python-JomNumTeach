# Practice 002 : 
# Type Conversion — Implicit and Explicit Type Conversion
# 1. Convert int() to str()
# 2. Convert str() to int()
# 3. Convert int() to bool()
# 4. Convert bool() to int()
# 5. Convert int() to float()
# 6. Convert float() to int()
# 7. Convert float() to str()
# 8. Convert str() to float()

print("\n---Type Conversion Practice---\n")
# 1. Convert int() to str()
age = 30 
age_str = str(age)
print("1. Convert int to str: ", age_str, " | ", type(age_str))
# 2. Convert str() to int()
num_str = "101"
num = int(num_str)
print("2. Convert str to int: ", num, " | ", type(num))
# 3. Convert int() to bool()
num = 1
bool_value = bool(num)
print("3. Convert int to bool: ", bool_value, " | ", type(bool_value))
# 4. Convert bool() to int()
bool_value = True
num = int(bool_value)
print("4. Convert bool to int: ", num, " | ", type(num))
# 5. Convert int() to float()
num = 10
float_value = float(num)
print("5. Convert int to float: ", float_value, " | ", type(float_value))
# 6. Convert float() to int()
float_value = 3.14
num = int(float_value)
print("6. Convert float to int: ", num, " | ", type(num))
# 7. Convert float() to str()
float_value = 3.14
float_str = str(float_value)
print("7. Convert float to str: ", float_str, " | ", type(float_str))
# 8. Convert str() to float()
float_str = "3.14"
float_value = float(float_str)
print("8. Convert str to float: ", float_value, " | ", type(float_value))

