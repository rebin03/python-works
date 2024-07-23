numbers = [10,11,12,13,14,15,16,17,18,19,20]

total = 0
odd_total = 0

for i in range(0,len(numbers)):
    if numbers[i]%2 == 0:
        print(numbers[i], end=" ")
    else:
        odd_total += numbers[i]
    
    total += numbers[i]

print(f"\nSum of total numberss = {total}")
print(f"Sum of odd numberss = {odd_total}")
    
