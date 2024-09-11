num1 = int(input("Enter number 1 :"))
num2 = input("Enter number 2: ")


try:
    result = num1 + num2
    
except Exception as e:
    print("Error:", e)
    result = num1 + int(num2)
    
finally:
    print(result)
    print("DB commit")