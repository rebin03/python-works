num = int(input("Enter number: "))

result = ""

if num % 3 == 0:
    result += "Fizz"
if num % 5 == 0:
    result += "Buzz"
    
print(result)