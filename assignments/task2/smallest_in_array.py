def get_smallest(arr):
    
    smallest = float('inf')
    
    for n in arr:
        
        if n < smallest:
            smallest = n
            
    return smallest

numbers = list(map(int, input().split()))
print(get_smallest(numbers))