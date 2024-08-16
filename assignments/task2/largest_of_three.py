def get_largest(n1, n2, n3):
    
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
    

num1, num2, num3 = map(int, input("Enter 3 numbers: ").split())

print(get_largest(num1, num2, num3))