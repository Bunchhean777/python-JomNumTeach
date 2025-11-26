# Jump statement is use to change normal flow of program. instead of running line by line they allow the program to stop, skip, exit a funtio or do nothing.
# break: stop the loop completely
# contine: skip the current step and goes to the next one
# return: exits a function and give back a value
# pass: used as a placeholder

# break and continue keyword
for i in range(5):
    if i == 3:
        continue
    print(i)

# return keyword
def operator(a,b):
    return a + b

sum = int(operator(1,2))
print(sum)