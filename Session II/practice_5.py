"""5. Write a python program which works as a calculator, it only does two operation addition and subtraction. 
Everytime the program asks for two numbers and then operation. The program should be running all the time until user enters stop."""

while True:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    operation = input("Enter the operation (+ and - only allowed): ")

    if operation == "+":
        print(first_number + second_number)
    elif operation == "-":
        print(first_number - second_number)
    else:
        print("Invalid operator. Only + and - allowed.")

    stop_or_not = input(
        "Enter stop to stop the calculator. Enter to continue for next operation. \n")
    if stop_or_not == "stop":
        break
