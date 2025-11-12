
# Console Calculator with python.

# while is true while user doesn't type exit
while True:

    # assigne from user
    num1 = float(input("\nEnter number to calculate : "))
    num2 = float(input("Enter number to calculate : "))

    # assigne from user to choosing operator
    print("\nPlease selete an operator (+,-,*,/) & type 'exit' to exit program: ")
    operator = input("Enter here : ")

    # match is the main process
    match operator:
        case '+':
            print(f"\nSum of two numer {num1} + {num2} = {float(num1+num2)}")
        case '-':
            print(f"\nSub of two number {num1} - {num2} = {float(num1-num2)}")
        case '*': 
            print(f"\nMul of two number {num1} * {num2} = {float(num1*num2)}")
        case '/':
            print(f"\nDiv of two number {num1} / {num2} = {float(num1/num1)}")
        case _:
            print("Invalid please try again!")

    # ask user to continue or break is true continue false break
    next_calculation = input("\nLet's do next calculation? (yes/no): ")
    
    if next_calculation == "no":
        break
