n = int(input())
A = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    op = input()
    S = set(map(int, input().split()))
    command, length = op.split()
    
    if command == "update":
        A.update(S)
    elif command == "intersection_update":
        A.intersection_update(S)
    elif command == "difference_update":
        A.difference_update(S)
    elif command == "symmetric_difference_update":
        A.symmetric_difference_update(S)
        
print(sum(A))