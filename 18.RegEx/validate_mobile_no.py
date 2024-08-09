from re import fullmatch

number = input("Enter mobile number: ")

pattern = "(91)(-|\\s)?[6-9]\\d{9}"

matcher = fullmatch(pattern, number)

print("Valid" if matcher != None else "Invalid")