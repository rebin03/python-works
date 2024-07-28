from math import factorial
n = int(input("Enter number of rows: "))

for i in range(n):
    
    print(" "*(n-i), end=" ")
    
    for j in range(i+1):
        
        print(factorial(i)//(factorial(i-j)*factorial(j)), end=" ")
    
    print()