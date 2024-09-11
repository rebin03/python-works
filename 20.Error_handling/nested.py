num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))


try:
    result = num1/num2
    print("Division result: ", result)
    
except Exception as e:
    
    print("Error:", e)
    num2 = int(input("Enter number 2: "))
    try:
        result = num1/num2
        print("Division result: ", result)
    except Exception as e:
        print("Error:", e)

finally:
    print("Database commit")
    print("File transfer")