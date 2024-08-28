def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def muliply(x, y):
    return x*y

def divide(x, y):
    return x/y

def mod(x, y):
    return x%y

num1, num2 = map(int, input("Enter two numbers: ").split())

print(f"Addition      : {add(num1, num2)}")
print(f"Subtraction   : {sub(num1, num2)}")
print(f"Multiplicaton : {muliply(num1, num2)}")
print(f"Division      : {divide(num1, num2)}")
print(f"Modulus       : {mod(num1, num2)}")