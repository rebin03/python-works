nums = input("Enter the numbers seperated by space: ").split(" ")
large_num = 0

for i in range(len(nums)):
    n = int(nums[i])
    if n > large_num:
        large_num = n
        
print(f"Largest number: {large_num}")