
 #Simple Calculator

 #Display the calculator title
print("===== SIMPLE CALCULATOR =====")

try:
     #Take the first number from the user
    num1 = float(input("Enter the first number: "))

    #Take the second number from the user
    num2 = float(input("Enter the second number: "))

     #Display the available arithmetic operations
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Take the user's choice
    choice = input("Enter your choice (1-4): ")

    # Perform the selected operation
    if choice == "1":
        result = num1 + num2
        print("Result:", result)

    elif choice == "2":
        result = num1 - num2
        print("Result:", result)

    elif choice == "3":
        result = num1 * num2
        print("Result:", result)

    elif choice == "4":
        # Check whether the second number is zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("Result:", result)

    else:
        # Handle an invalid operation choice
        print("Invalid choice. Please select a number from 1 to 4.")

# Handle inputs that are not valid numbers
except ValueError:
    print("Error: Please enter valid numeric values.")
