def get_hcf(x, y):
    
    smallest = min(x,y)
    
    for i in range(1, smallest + 1):
        
        if x%i == 0 and y%i == 0:
            hcf = i
    
    return hcf

n1, n2 = map(int, input("Enter two number: ").split())

print(get_hcf(n1, n2))