# Validate variable which has following rule:
    # first char must be alphabet from k-m
    # second number must be a number which is divisibe by 3
    # followed by any number of aphanumerics and @

from re import fullmatch

var_name = input("Enter variable name: ")


pattern = "[k-m][0369][a-zA-Z0-9@]*"

matcher = fullmatch(pattern, var_name)

print("Invalid" if matcher == None else "Valid")