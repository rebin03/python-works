# In higher order function we can return functions

def hello(name):
    print("Hello has been executed.")
    
    def greet():
        print("Hi, good morning!")
        
    def welcome():
        print("Hey, you are welcome.")
        
    if name == "John":
        return greet
    else:
        return welcome
    
new_func = hello("John")
new_func()