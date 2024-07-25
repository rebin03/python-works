
arr = [
    [10,20],
    [12,25],
    [35,30]
]

nums_gt_15 = [num for lst in arr for num in lst if num > 15]
print(nums_gt_15)