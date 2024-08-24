nums = input().split()

N = int(nums[0])
M = int(nums[1])
c = ".|."
ch = c

for i in range(0, N//2):
    print(ch.center(M, "-"))
    ch += 2*c

print("WELCOME".center(M, "-"))

n = N
for i in range(0, N//2):
    n = n - 2
    ch = c*(n)
    print(ch.center(M, "-"))
    