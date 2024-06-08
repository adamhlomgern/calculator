from art import logo


def greet():
    print(logo)
    print("This is the bestest calculator.")



#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Divide
def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero is not possible."
    return n1 / n2

#Multiply
def multiply(n1, n2):
    return n1 * n2


#Dictionary
operations = {
    "+": add, 
    "-": subtract, 
    "/": divide, 
    "*": multiply, 
}


#Get user inputs
def user_input():
    num1 =int(input("What's the first number?: "))
    num2 =int(input("What's the second number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    result = operations_execute(num1, num2, operation_symbol)
    print(f"The result is: {result}")
    
    y_or_n = input("Would you like to go again? type 'y' for yes or 'n' for no: ")
    if y_or_n == "y":
        user_input()
    else:
        print("Goodbye!")
        

#Execute the selected operation
def operations_execute(num1, num2, operation_symbol):
    if operation_symbol in operations:
        operation = operations[operation_symbol]
        return operation(num1, num2)
    else:
        return "Invalid operation."
    

#Main Execution
if __name__ == "__main__":
    greet()
    user_input()