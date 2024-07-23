def is_fibonacci(num):

    prev = 0
    current = 1
    next = prev + current
    isFibonacci = False

    if num == 0 or num == 1:
        isFibonacci = True
    else:
        while(next <= num):
            
            next = prev + current
            prev = current
            current = next
            
            if num == next or num == 0:
                isFibonacci = True
                break
        
    if isFibonacci:
        return True
    else:
        return False
    
print(is_fibonacci(5))