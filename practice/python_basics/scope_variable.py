a = 10 #global

def display():
    a = 15 #local
    def show():
        print(a)
    show() #local
    

display()

# like other programming languages like java, C++ etc. Python does not have block scope

a, b = 5,7

if a < b:
    c = a + b
    
print(c) # c is avalilable outside the if block.

# But if it is inside a function it will be a local scope

num1, num2 = 3, 4

def add():
    if a < b:
        result = num1 + num2
        print(result) # 'result' is local scope variable
        
# print(result) - using 'result' outside the fuction will show error