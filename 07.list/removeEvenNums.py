nums = [1,2,3,4,5,6,7,8]


for num in nums:
    if num%2 == 0:
        nums.remove(num)
        
print(nums)