# Using string

def is_armstrong(num):
    
    digits = str(num)
    length = len(digits)
    
    total = sum(int(digit)**length for digit in digits)
    
    return total == num

num = int(input("Enter the number: "))
print("Armstrong number" if is_armstrong(num) else "Not Armstrong number")