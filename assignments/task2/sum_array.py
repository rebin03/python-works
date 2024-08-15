def get_sum(arr):
    
    total = 0
    
    for num in arr:
        
        total += num
        
    return total

nums = list(map(int, input().split()))
print(get_sum(nums))