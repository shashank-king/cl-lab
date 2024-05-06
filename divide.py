def divide_real_numbers(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero."
    else:
        return "Error: Both inputs must be real numbers."

# Take input from the user
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

if number1.replace('.', '', 1).isdigit() and number2.replace('.', '', 1).isdigit():
    result = divide_real_numbers(float(number1), float(number2))
    print("Result of division:", result)
else:
    print("Error: Please enter valid real numbers.")
