# Function

# def function_name(param1, param2, param3,....):
#     code - function defenition
#     return value


def add(n1, n2):
    
    result = n1 + n2
    return result

# function calling
sum = add(2,3)

print(sum)

def cube(num):
    
    result = num**3
    return result

def max_two(n1,n2):
    
    result = n1 if n1>n2 else n2
    return result

def min_two(n1,n2):
    
    result = n1 if n1<n2 else n2
    return result

def is_odd(num):
    
    result = True if num%2 != 0 else False
    return result