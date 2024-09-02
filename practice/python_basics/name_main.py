# the term 'if __name__ = "__main__" will execute only when we run the file directly.
# When we run thie module from other files the code under this term will not executed.
# It's because if we call directly the module then __name__ is equal to "__main__"
# But when importing this module, the __name__ is assigned the value of module name.


def display(name):
    return name

def do_something():
    print("This function is doing something")

# if we didn't specify this then the following lines will run when we calling this in other modules. So, by doing this we can restrict certain code from execution.  
if __name__ == "__main__":
    
    print("This is name_main.py")
    name = input("Enter your name: ")
    print(display(name))
    do_something()
