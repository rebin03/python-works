#program to find GCD of two numbers 

num1 = int(input("Enter num1: "))
num2= int(input("Enter num2: "))
gcd = 1

num = max(num1, num2)

for i in range(1, num+1):
    if num1%i==0 and num2%i==0:
        gcd = i
        
print(f"GCD of {num1} and {num2} is {gcd}")