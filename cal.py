def add(num1,num2):       #define functions
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    if num2 == 0:
        print("Error! cannot divide with Zero")            #Handle division by zero with appropriate error messages
        return None
     return num1/num2

while True:           # Calculator for Meun Loop
    print("---Simple Calculator---")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exist")

    choice = int(input("Which Operation you performed? (1-5) "))
    if choice == 5:
        print("Exiting calculator. Goodbye!")
        break

    try:
        num1 = float(input("Enter a first number: "))      #take input from user
        num2 = float(input("Enter a second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue
    if choice == 1:
        print(f"Addition of two numbers: {num1+num2}")        # Apply conditions
    elif choice == 2:
        print(f"Subtract of two number: {num1-num2}")
    elif choice == 3:
        print(f"Multiply of two number: {num1*num2}")
    elif choice == 4:
        result = divide(num1, num2)
        if result is not None:
            print(f"Divide of two number: {result}")
    else:
        print("Invalid Choice. Please choose from 1 to 5.")
