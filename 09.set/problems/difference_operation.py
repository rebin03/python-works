n = int(input())
english_set = set(map(int, input().split()))
b = int(input())
french_set = set(map(int, input().split()))

only_inglish = len(english_set.difference(french_set))
print(only_inglish)