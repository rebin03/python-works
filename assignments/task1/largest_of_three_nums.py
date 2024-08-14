def largest_number(num1,num2,num3):
    largest = 0
    
    if num1 > num2 and num1 > num3:
        largest = num1
    elif num2 > num1 and num2 > num3:
        largest = num2
    else:
        largest = num3
    
    return largest


num1, num2, num3 = map(int, input().split())
largest_number(num1, num2, num3)