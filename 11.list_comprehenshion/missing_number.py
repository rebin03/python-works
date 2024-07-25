arr = [0,1,3,4]

n = len(arr)

sum_of_n = n*(n+1)//2
current_sum = sum(arr)
missing_num = sum_of_n - current_sum

print(missing_num)