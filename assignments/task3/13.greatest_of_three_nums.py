def greatest_num(n1, n2, n3):
    
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
    

num1, num2, num3 = map(int, input("Enter three numbers: ").split())
print(f"Greatest of 3 numbers is: {greatest_num(num1, num2, num3)}")