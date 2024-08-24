def info_person(*args, **kwargs):
    
    print(args)
    
    for k,v in kwargs.items():
        print(k, v)
        

info_person(1,2,3, name = "Ram", age=23, dept = "CSE")

#-------------------------------------------------------------------------------------------------------------------------------

def multiply(*args):
    product = 1
    
    for i in args:
        product *= i
        
    return product

result1 = multiply(2,3,-6,8)
result2 = multiply(2,5,8,9,0,6)

print(result1)
print(result2)