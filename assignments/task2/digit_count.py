def get_digit_count(num):
    
    count = 0
    
    while num != 0:
        
        num = num//10
        count += 1
        
    return count

num = int(input("Enter the number: "))
print(get_digit_count(num))