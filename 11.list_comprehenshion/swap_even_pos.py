arr = [10,11,12,13,14,15,16,17,18]
#      0   1  2  3  4  5  6  7

even_pos_num = []
length = len(arr)

for i in range(length):
    if i%2 != 0:
        even_pos_num.append(arr[i])

print(arr)
        
even_pos_num.reverse()
print(even_pos_num)

j=0
for i in range(length):
    
    if i%2 != 0:
    
        arr[i] = even_pos_num[j]
        j+=1

print(arr)