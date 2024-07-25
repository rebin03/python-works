arr = [6,7,3,4,8,9,10]

mapped_list = [num+1 if num>5 else num-1 for num in arr]
print(mapped_list)