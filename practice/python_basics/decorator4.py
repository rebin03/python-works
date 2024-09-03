def upper_decor(func):
    
    def wrapper(name):
        res = func(name)
        return res.upper()
    
    return wrapper


def attach_length_decor(func):
    
    def wrapper(name):
        length = len(name)
        result = func(name)
        result += str(length)
        return result
    
    return wrapper

@upper_decor
@attach_length_decor
def hello_name(name):
    return "Hello " + name

print(hello_name("Rebin"))