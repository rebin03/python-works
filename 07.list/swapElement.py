# program to swap first and last element from the list

nums = [1,2,3,4,5,6,7]

# using methods
num1 = nums.pop()
num2 = nums.pop(0)

nums.insert(0,num1)
nums.append(num2)

print(nums)

# using direct swap
nums[-1],nums[0] = nums[0],nums[-1]

print(nums)