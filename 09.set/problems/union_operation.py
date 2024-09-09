n = int(input())
set1 = set(map(int, input().split()))
b = int(input())
set2 = set(map(int, input().split()))


read_atleast_one = len(set1.union(set2))
print(read_atleast_one)
