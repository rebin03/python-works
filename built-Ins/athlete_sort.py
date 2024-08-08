def get_k(x):    
    return x[k]


nm = input().split()

n = int(nm[0])

m = int(nm[1])

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

result = sorted(arr, key=get_k)

for attr in result:
    print(*attr)