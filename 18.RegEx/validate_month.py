from re import fullmatch

month = input("Enter month: ")

pattern = "(0?[1-9]|1[0-2])"

matcher = fullmatch(pattern, month)

print("Valid" if matcher != None else "Invalid")