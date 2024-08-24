M = int(input())
a = set(list(map(int, input().split())))

N = int(input())
b = set(list(map(int, input().split())))

new_set = sorted(list(a.symmetric_difference(b)))



for n in new_set:
    print(n)