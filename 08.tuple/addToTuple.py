numbers = [1,2,[3,(100,200,300),4],5,6]

nums = numbers[2][1]

new_nums = list(nums)
new_nums.append(500)

numbers[2][1] = tuple(new_nums)
print(numbers)