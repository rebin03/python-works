num = int(input("Enter number: "))

prev = 0
current = 1

print(f"{prev} {current}", end=" ")

for i in range(0, num):
    
    next = prev + current
    prev = current
    current = next
    
    print(next, end=" ")
    
    # 0 1 1 2 3 5 8 13 21