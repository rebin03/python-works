nums = [3,2,5,7,9,1,10,4,]

smallest_num = nums[0]

for num in nums:
    
    if num < smallest_num:
        smallest_num = num
        
print(f"Smallest number is: {smallest_num}")