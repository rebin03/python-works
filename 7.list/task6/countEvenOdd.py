nums = [1,2,3,4,5,6,7,8,9,10,11]

count_odd = 0
count_even = 0

for num in nums:
    if num%2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f"Count of odd number: {count_odd}\nCount of even number: {count_even}")