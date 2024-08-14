def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

def calculator(num1,num2):
    
    op = input("\n+ for addition\n- for subtraction\n* for multiplication\n/ for division\nSelect operator: ")
    
    if op == "+":
        res = add(num1,num2)
    elif op == "-":
        res = subtract(num1,num2)
    elif op == "*":
        res = multiply(num1,num2)
    elif op == "/":
        res = divide(num1,num2)
    else:
        print("invalid operator")

    return res

flag = True
while flag:
    
    num1, num2 = map(int, input("Enter two numbers: ").split())
    result = calculator(num1,num2)
    print(f"Result is :{result}")
    
    s = input("Do you want to continue calculating? type 'yes' or 'no'\n").lower()
    
    if s == 'no':
        flag = False

    
    