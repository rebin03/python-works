def find_happiness(arr, A, B):
    
    happiness = 0
    
    for num in arr:
        if num in A:
            happiness += 1
        elif num in B:
            happiness -= 1
    return happiness
    
n, m = input().split()
arr = input().split()
A = set(input().split())
B = set(input().split())

result = find_happiness(arr, A, B)
print(result)