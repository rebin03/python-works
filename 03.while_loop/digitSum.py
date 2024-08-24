num = int(input("Enter the number: "))
sum = 0

while(num != 0):
    
    digit = num%10
    sum = sum + digit
    num = num//10

print(sum)