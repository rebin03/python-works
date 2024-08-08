from re import fullmatch

variable_name = input("Enter variable name: ")

pattern = "[a-zA-Z][a-zA-Z0-9_]*"

matcher = fullmatch(pattern, variable_name)

print("Valid" if matcher != None else "Invalid")