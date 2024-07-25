# Using two pointer

arr = [10,11,12,13,14,15,16,17]

length = len(arr)-1

left = 1
right = length if length%2 != 0 else length-1

while left < right:
    
    arr[left], arr[right] = arr[right], arr[left]
    
    left += 2
    right -= 2

print(arr)