from re import fullmatch

text = "hello_hai"

matcher = fullmatch("[a-zA-Z][a-zA-Z0-9_]*", text) # fullmatch() Try to apply the pattern to all of the string, returninga Match object, or None if no match was found.

print("Valid" if matcher != None else "Invalid")