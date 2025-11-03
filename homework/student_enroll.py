
# User inputs
student_name = input("Enter student name: ")
python_score = float(input("Enter Python score: "))
Java_score = float(input("Enter Java score: "))
Cpp_score = float(input("Enter C++ score: "))

# Calculate average score
average = (python_score + Java_score + Cpp_score) / 3

# Determine grade based on average score. using conditionals if-elif-else from Control flow statements
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
elif average >= 50:
    grade = 'E'
else:
    grade = 'F'

# Display the report/summary
print(f"📑 Student Montly Score Report")
print(f"----------------------------------")
print(f"Student Name : {student_name}")
print(f"Python Score : {python_score}")
print(f"Java Score   : {Java_score}")
print(f"C++ Score    : {Cpp_score}")
print(f"Average Score: {average:.2f} and Grade: {grade}")
print(f"----------------------------------")

# Recap message to the student
print("📢 Recap ")
print(f"The student  {student_name} has achieved an average score of {average:.2f}, which corresponds to grade '{grade}'.")