def is_fibonacci(num):

    prev = 0
    current = 1
    next = prev + current

    if num == 0 or num == 1:
        return True
    
    else:
        while(next <= num):
            
            next = prev + current
            prev = current
            current = next
            
            if num == next or num == 0:
                return True
            
    return False
    
print(is_fibonacci(5))