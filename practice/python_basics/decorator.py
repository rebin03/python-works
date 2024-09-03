# Decorators are used to define additional functionalities to an already defined functions.

def div(a, b):
    print(a/b)
    

def smart_div(func):
    
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    
    return inner

new_div = smart_div(div)

new_div(2, 4)