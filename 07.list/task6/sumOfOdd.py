nums = [1,2,3,4,5,6,7,8,9]
total = 0

for num in nums:
    
    if num%2 != 0:
        total += num

print(f"Sum of odd numbers: {total}")