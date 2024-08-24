arr = [2,3,4,5]

result = 7

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == result:
            print(f"{arr[i],arr[j]}")