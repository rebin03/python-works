def is_even(num):
    if num%2 == 0:
        return True
    
    
num = int(input("Enter number: "))

print("Even number" if is_even(num) else "Odd number")