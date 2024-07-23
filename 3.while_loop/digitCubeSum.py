num = int(input("Enter the number: "))
sum = 0
while(num != 0):
    
    digit = num%10
    cube = digit**3
    sum = sum + cube
    num = num//10
    
print(sum)