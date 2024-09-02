def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y


def calculate(fun, x, y):
    res = fun(x,y)
    return res
    
result = calculate(add, 10, 8)
print(result)