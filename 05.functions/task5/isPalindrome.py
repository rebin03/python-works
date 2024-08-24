def is_palindrome(num):
    value = num
    length = len(str(num))
    result = 0
    for i in range(1,length+1):
        
        digit = num%10
        result = result*10 + digit
        num = num//10
        
    if result == value:
        return True
    else:
        return False

print(is_palindrome(121))