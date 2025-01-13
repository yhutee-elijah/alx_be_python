def perform_operation(num1, num2, operation):
    match operation:
       case "add":
           return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
               print("Zero division not allowed")
            elif:
                return num1 / num2
