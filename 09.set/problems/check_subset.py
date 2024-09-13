n = int(input())

while n != 0:
    
    no_a = int(input())
    A = set(map(int, input().split()))
    no_b = int(input())
    B = set(map(int, input().split()))
    
    print(A.intersection(B) == A)
    
    n -= 1