# for loop in python
# Syntax:
# for variable in sequence:
#     -> code block to be executed


# using for loop:
print("-" * 50)
print("> Using for loop with range function:")
for i in range(1,10,3):
    print(f"Iteration number value of i: {i}")

# list of programming languages
print("-" * 50)
programming_languages = ["Python", "Java", "JavaScript", "C++"]
print(f"> The programming languages list is: {programming_languages[1]}")
print("-" * 50)

# using loop for each item in a list
print("> Using for loop to iterate: ")
for pl in programming_languages:
    print(f"Programming languages name is: {pl}")

