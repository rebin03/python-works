numbers = [14,23,11,25,9,4,14,11,1,3,4,9,9,8,11,3]

number_count = {}

for num in numbers:
    
    if num in number_count:
        
        number_count[num] += 1
        
    else:
        
        number_count[num] = 1
        
print(number_count)