def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operation"
    
    def main():
        print("Arithmetic Operations")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation to (add, subtract, multiply, divide): ").strip().lower()
        result = perform_operation(num1, num2, operation)
        print(f"Result is: {result}")   

        if __name__ == "__main__":
            main()