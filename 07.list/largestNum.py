nums = [1,3,2,5,7,9,10,4]

largest_num = nums[0]

for num in nums:
    
    if num > largest_num:
        largest_num = num 
    
        
print(f"Largest number is: {largest_num}")