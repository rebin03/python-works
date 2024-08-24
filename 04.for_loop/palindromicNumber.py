num = int(input("Enter number: "))
value = num
length = len(str(num))
result = 0
for i in range(1,length+1):
    
    digit = num%10
    result = result*10 + digit
    num = num//10
    
if result == value:
    print("Palindrome")
else:
    print("Not Palindrome")
