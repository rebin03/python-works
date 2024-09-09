n = int(input())
english_set = set(map(int, input().split()))
b = int(input())
french_set = set(map(int, input().split()))


subscribe_both = len(english_set.intersection(french_set))
print(subscribe_both)