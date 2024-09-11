# Syntax:
# -------
# try:
#     The try block lets you test a block of code for errors.
# except:
#     The except block lets you handle the error.
# finally:
#     The finally block lets you execute code, regardless of the result of the try- and except blocks.
#     -clean up processing(like closing file.)


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))


try:
    result = num1/num2
    print("Division result: ", result)
except Exception as e:
    print("Error:", e)
    
print("Database commit")
print("File transfer")