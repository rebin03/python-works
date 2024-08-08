from re import fullmatch

number = input("Enter mobile number: ")

pattern = "(91)[0-9]{10}"

matcher = fullmatch(pattern, number)

print("Valid" if matcher != None else "Invalid")