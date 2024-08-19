# -> The yield keyword is used to return a list of values from a function.
# -> Unlike the return keyword which stops further execution of the function, the yield keyword continues to the end of the function.
# -> When you call a function with yield keyword(s), the return value will be a list of values, one for each yield.

def my_func():
    
    yield "Hello"
    yield 51
    yield "goodbye"


values = my_func()

print(next(values))

for val in values:
    print(val)