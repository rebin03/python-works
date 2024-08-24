def is_armstrong(num):
    value = num
    total = 0
    digit_count = len(str(num))
    while(num != 0):
        
        digit = num%10
        exponent = digit**digit_count
        total = total + exponent
        num = num//10

    return value == total

print(is_armstrong(153))