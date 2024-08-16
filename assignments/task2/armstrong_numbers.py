def is_armstrong(num):
    
    exp = len(str(num))
    val = num
    total = 0
    
    while num != 0:
            
            digit = num%10
            total += digit**exp
            num = num//10
    
    return total == val

def armstrong_num(n1,n2):
    
    arr = [str(num) for num in range(n1,n2) if is_armstrong(num)]
    
    return " ".join(arr)

start, end = map(int, input("Enter start and end: ").split())
print(armstrong_num(start, end))