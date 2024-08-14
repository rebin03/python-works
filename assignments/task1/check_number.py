def check_number(num):
    if num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negetive")
    else:
        print("Number is zero")


        
number = int(input("Enter the number: "))
check_number(number)