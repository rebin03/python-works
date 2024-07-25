
arr = [
    [10,20],
    [21,30],
    [40,53]
]

arr_sum = [num for lst in arr for num in lst]
print(sum(arr_sum))