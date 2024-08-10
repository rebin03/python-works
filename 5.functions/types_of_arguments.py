# 1) Positional argument
#-----------------------

# -> During a function call, values passed through arguments should be in the order of parameters in the function definition.

def greet(name, dept):
    print(f"Hi, {name}")
    print(f"Are you from {dept} department?")
    
greet("John","CSE") # This will give expected output

greet("CSE","John") # Here, the order is not correct. so the output will not be as expected ( to solve this, we can use keyword argument.)

#-----------------------------------------------------------------------------------------------------------------------------------------------
# 2) Keyword Arguments
#---------------------

# -> Functions can also be called using keyword arguments of the form kwarg=value.
# -> During a function call, values passed through arguments don’t need to be in the order of parameters in the function definition. 
# -> But all the keyword arguments should match the parameters in the function definition.

def add(a,b=5,c=10):
    return (a+b+c)

print (add(b=10,c=15,a=20)) #Output:45


#-----------------------------------------------------------------------------------------------------------------------------------------------

# NB: -> We can use mix of positional and keyword arguments.
#     -> But, Keyword arguments should always follow positional arguments.

def greet1(name, dept):
    print(f"Hi, {name}")
    print(f"Are you from {dept} department?")
    
greet1("John",dept = "CSE")

#-----------------------------------------------------------------------------------------------------------------------------------------------
# 3) Default argument
#--------------------

# -> Default arguments are values that are provided while defining functions.
# -> The assignment operator '=' is used to assign a default value to the argument.
# -> Default arguments become optional during the function calls.
# -> If we provide a value to the default arguments during function calls, it overrides the default value.
# -> The function can have any number of default arguments.
# -> Default arguments should follow non-default arguments.

def greet2(name, subject, dept="CS"):
    print(f"Hi, {name}")
    print(f"Do you teach {subject}?")
    print(f"Are you from {dept} department?")
    
greet2("John","Python")
greet2("Maya","Maths","Mathematics") # This will overrite the default value (ie, dept = "CS" will be overrite to "Mathematics")

#-----------------------------------------------------------------------------------------------------------------------------------------------
# 4) Arbitrary argument
#----------------------

# -> If we don’t know the number of arguments needed for the function in advance, we can use arbitrary arguments

# a) Arbitrary positional argument:
#----------------------------------

#   - In this, an asterisk (*) is placed before a parameter in function definition 
#     which can hold non-keyword variable-length arguments. 
#   - These arguments will be wrapped up in a tuple. 
#   - Before the variable number of arguments, zero or more normal arguments may occur.

def add(*args):
    result=0
    for i in args:
         result=result+i
    return result

print (add(1,2,3,4,5)) #Output:15
print (add(10,20)) #Output:30

# b) Arbitrary keyword argument:
#-------------------------------

#   - For arbitrary positional argument, a double asterisk (**) is placed before a parameter 
#     in a function which can hold keyword variable-length arguments.

def fn(**kwargs):
    print(kwargs)
    for i in kwargs.items():
        print (i)
        
fn(numbers=5,colors="blue",fruits="apple")

'''
Output:
('numbers', 5)
('colors', 'blue')
('fruits', 'apple')
'''