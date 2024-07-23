numbers = [10,11,12,13,14,20,21]

def is_prime(num):
    
    for i in range(2,num):
        if num%i==0:
            return False
        return True
    
    return True if num == 2 else False

for i in range(0,len(numbers)):
    if is_prime(numbers[i]):
        print(numbers[i])