# Disarium number:
# when the sum of its digit raised to the power of their respective positions becomes equal to the number itself.
# For example, 175 is a Disarium number as follows: 11+ 72 + 53 = 1+ 49 + 125 = 175.

def is_disarium(num):
    
    exp = len(str(num))
    val = num
    res = 0
    
    while num != 0:
        
        digit = num%10
        res += digit ** exp
        num = num//10
        exp -= 1
        
    return res == val


num = int(input("Enter a number: "))
print(is_disarium(num))