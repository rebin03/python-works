# using pointers

arr = [0,1,2,3,4]

n = len(arr)

pr = 0
cr = 1

for i in range(1,len(arr)):
    
    cr = arr[i]
    pr = arr[i-1]
    
    if cr - pr != 1:
        print(pr+1)
        break
    elif cr == arr[len(arr)-1] and arr[0] == 0:
        print(cr+1)
        break
    elif arr[0] != 0:
        print(0)
        break