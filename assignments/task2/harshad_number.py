def is_harshad(num):
    
    val = num
    digit_sum = 0
    
    while num != 0:
        
        digit = num%10
        digit_sum += digit
        num = num//10
        
    return val % digit_sum == 0

num = int(input("Enter a number: "))
print(is_harshad(num))
        