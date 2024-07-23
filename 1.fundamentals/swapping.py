num1 = 100
num2 = 200

# Before swapping
print(f"Before swapping: num1 = {num1} num2 = {num2}")

# Logic 1: Works only for integer

# num1 = num1+num2
# num2 = num1-num2
# num1 = num1-num2

# Logic 2
# num1, num2 = num2, num1 #Only in python

#Logic 3: Using temporary variable
# temp = num1
# num1 = num2
# num2 = temp

# Logic 4: Using Division and Multiplication operator
num1 = num1*num2
num2 = num1//num2
num1 = num1//num2


# After swapping
print(f"After swapping: num1 = {num1} num2 = {num2}")
