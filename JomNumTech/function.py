# Function is a block of code that performs a specific task.
# Why use functions?
# Avoid repeating code
# Organize your program into smaller parts
# Reuse code in other programs
# Improve readability and debugging

#declare the function
def ask():
    print(f"What's your major?")

# call the function
ask()
# Declare a function with parameters
def area_of_triangle(base, height):
    area = 0.5 * base * height
    return area

#  call the function
triangle_area = area_of_triangle(10, 5)
print(f"The area of the triangle is: {triangle_area}")

