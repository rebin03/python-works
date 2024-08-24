
def nth_digit_max(num1, num2):
    
    return num1 if num1%10 > num2%10 else num2
    
    # digit1 = num1%10
    # digit2 = num2%10
    
    # if digit1 > digit2:
    #     return num1
    # else:
    #     return num2
    
print(nth_digit_max(121,330))