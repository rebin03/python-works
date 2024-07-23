def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operators_dict = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():

    num1 = float(input("Enter first number: "))
    for op in operators_dict:
        print(op)

    flag = True
    while flag:
        
        operator = input("Pick an operator: ")
        num2 = float(input("Enter the next number: "))
        calculator_function = operators_dict[operator]
        output = calculator_function(num1, num2)
        print(f"{num1} {operator} {num2} = {output}")

        should_continue = input(f"Enter 'y' to continue with {output} or 'n' to start new calculation or 'x' to exit: ").lower()
        
        if should_continue == 'y':
            num1 = output
        elif should_continue == 'n':
            num1 = output
            flag = False
            calculator()
        else:
            print("Bye")
            flag = False
            
calculator()