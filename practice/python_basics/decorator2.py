def upper_decor(func):
    
    def wrapper(name):
        res = func(name)
        return res.upper()
    
    return wrapper


# adding decorator to the already existing function.
@upper_decor
def hello(name):
    return "Hello " + name


print(hello("Rebin"))