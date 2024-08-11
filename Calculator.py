def calculator():
    # Display the available operations
    print("Select operation:")
    print("1. Addition:")
    print("2. Subtraction:")
    print("3. Multiplication:")
    print("4. Division:")
    
    # Get user input for operation
    choice = input("Enter choice (1/2/3/4): ")
    
    # Check if the choice is valid
    if choice not in ['1', '2', '3', '4']:
        print("Invalid input")
        return
    
    # Get user input for numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input")
        return
    
    # Perform calculation based on the chosen operation
    if choice == '1':
        result = num1 + num2
        operation = "addition"
    elif choice == '2':
        result = num1 - num2
        operation = "subtraction"
    elif choice == '3':
        result = num1 * num2
        operation = "multiplication"
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed")
            return
        result = num1 / num2
        operation = "division"
    
    # Display the result
    print(f"The result of {operation} is: {result}")

# Call the calculator function
calculator()
