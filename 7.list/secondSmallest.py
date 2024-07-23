nums = [-22,-22,-22,4]

smallest_num = nums[0]
second_smallest_num = nums[1]

for num in nums:
    
    if num < smallest_num:
        
        second_smallest_num = smallest_num
        smallest_num = num
        
    elif num < second_smallest_num and num > smallest_num:
        
        second_smallest_num = num
        
print(f"Second smallest number is: {second_smallest_num}")