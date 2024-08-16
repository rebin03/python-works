def product(lst):
    
    res = 1
    
    for num in lst:
        res *= num
        
    return res

nums = list(map(int, input("Enter the list of numbers: ").split()))
print(product(nums))