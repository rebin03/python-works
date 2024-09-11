num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))


try:
    result = num1/num2
    print("Division result: ", result)
    
except Exception as e:
    
    print("Error:", e)
    num2 = int(input("Enter number 2: "))
    result = num1/num2

finally: # This block will execute even error occured or not
    print("Database commit")
    print("File transfer")