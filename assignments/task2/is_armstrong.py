def is_armstrong(num):
    
    og_val = num
    length = len(str(num))
    total = 0
    
    while num != 0:
        
        digit = num%10
        total += digit**length
        num = num//10
        
    return og_val == total


num = int(input("Enter the number: "))
print("Armstrong number" if is_armstrong(num) else "Not Armstrong number")