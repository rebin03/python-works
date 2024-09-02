# Functions which accept functions as parameter or return functions are called Higher order function.

def greet_louder(name):
    print(f"Hello, Good morning {name}!".upper())

def greet_softer(name):
    print(f"Hello, Good morning {name}!".lower())

# This is Higher order function
def hello(func, name):
    func(name)
    print("This is from display() function")
    
hello(greet_louder, "Helen")
hello(greet_softer, "John")