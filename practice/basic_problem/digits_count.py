num = 12356
count = 0

while num != 0:
    
    digit = num%10
    count += 1
    num = num//10

print(count)