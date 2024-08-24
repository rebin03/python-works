nums = [1,2,2,3,4,5,3,6,4,7]
unique_values = []

for num in nums:
    if nums.count(num) == 1:
        unique_values.append(num)
        
print(unique_values)