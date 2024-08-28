from re import fullmatch

# An identifier is valid if it starts with a letter (a-z, A-Z) or an underscore (_) followed by zero or more letters, underscores, or digits (0-9).

pattern = "[a-zA-Z_]\\w*"

id = input("Enter identifier name: ")

matcher = fullmatch(pattern, id)

print("Valid" if matcher!= None else "Invalid")