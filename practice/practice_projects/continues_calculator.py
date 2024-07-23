def calculator(num):
    operator = input("Pick an operator: ")
    next_num = int(input("Enter next number: "))
    if operator == "+":
        result = num + next_num
    elif operator == "-":
        result = num - next_num
    elif operator == "*":
        result = num * next_num
    elif operator == "/":
        result = num / next_num
        
    print(f"{num} {operator} {next_num} = {result}")
    
    dec = input(f"Enter 'y' to continue calculation with {result} or 'n' to start new calculation or 'x' to exit:")
    
    if dec == "y":
        calculator(result)
    elif dec == "n":
        num = int(input("Enter first number: "))
        calculator(num)
    else:
        exit()

num = int(input("Enter first number: "))
print("+\n-\n*\n/")

calculator(num)