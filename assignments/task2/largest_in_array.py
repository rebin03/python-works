def get_largest(arr):
    
    largest = 0
    
    for n in arr:
        
        if n > largest:
            largest = n
            
    return largest

numbers = list(map(int, input().split()))
print(get_largest(numbers))