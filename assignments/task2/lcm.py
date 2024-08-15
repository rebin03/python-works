def get_lcm(n1, n2):
    
    greater = max(n1,n2)
    
    while True:
        
        if greater%n1 == 0 and greater%n2 == 0:
            lcm = greater
            break
        else:
            greater += 1
    return lcm



num1, num2 = map(int, input("Enter two numbers: ").split())
print(get_lcm(num1, num2))