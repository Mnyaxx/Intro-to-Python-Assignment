def calculator():
    print("Welcome to the simple calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("What do you want to do? (+, -, *, /): ")
    
    if op == '+':
        result = num1 + num2
        print("The answer is:", result)
    elif op == '-':
        result = num1 - num2
        print("The answer is:", result)
    elif op == '*':
        result = num1 * num2
        print("The answer is:", result)
    elif op == '/':
        if num2 == 0:
            print("Oops! You can't divide by zero.")
        else:
            result = num1 / num2
            print("The answer is:", result)
    else:
        print("Sorry, that's not a valid operation.")
    
    print("Thanks for using the calculator!")

calculator()

