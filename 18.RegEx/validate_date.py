from re import fullmatch

date = input("Enter date: ")

pattern = "(0?[1-9]|(1|2)[0-9]|3[0-1])"

matcher = fullmatch(pattern, date)

print("Valid" if matcher != None else "Invalid")