numbers = [151,153,154,370,371,372,373,16341,1635]

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

for i in range(0,len(numbers)):
    if is_armstrong(numbers[i]):
        print(numbers[i])