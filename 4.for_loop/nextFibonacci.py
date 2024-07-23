num = int(input("Enter number: "))

prev = 0
current = 1

next = prev + current

while(next <= num):
    
    next = prev + current
    prev = current
    current = next
    
print(f"Next fibonacci number is: {next}")