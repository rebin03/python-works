def add_numbers(n1, n2):
    return n1+n2

def add_numbers(n1, n2, n3):
    return n1+n2+n3

print(add_numbers(100, 50, 250))

# Python do not support method overloading by default. It will redefine the existing function with same name. 
# print(add_numbers(100, 30))