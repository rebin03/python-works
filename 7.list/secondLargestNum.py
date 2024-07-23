nums = [33,2,5,7,11,1,10,4,]

largest_num = nums[0]
second_largest_num = nums[1]

for num in nums:
    
    if num > largest_num:
        
        second_largest_num = largest_num
        largest_num = num
        
    elif num > second_largest_num and num < largest_num:
        
        second_largest_num = num
        
print(f"Second largest number is: {second_largest_num}")