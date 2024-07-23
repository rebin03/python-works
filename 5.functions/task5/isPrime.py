def is_prime(num):
    
    for i in range(2,num):
        if num%i==0:
            return False
        return True
    
    return True if num == 2 else False

    

print(is_prime(5))