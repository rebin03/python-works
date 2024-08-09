# Validate pan card

# First 3 char are alphabets
# 4th place PCAFHT
# 5th place alphabets
# 4 digits
# 1 alphabet

from re import fullmatch

pan = input()

pattern = "[A-Z]{3}[PCAFHT][A-Z]\\d{4}[A-Z]"

matcher = fullmatch(pattern, pan)

print("Valid" if matcher != None else "Invalid")