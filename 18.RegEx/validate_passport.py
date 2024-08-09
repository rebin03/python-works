# It should be eight characters long.
# The first character should be an uppercase alphabet.
# The next two characters should be a number, but the first character should be any number from 1-9 and the second character should be any number from 0-9.
# It should be zero or one white space character.
# The next four characters should be any number from 0-9.
# The last character should be any number from 1-9.

from re import fullmatch

pattern = "[A-Z][1-9][0-9](\\s|0)?[0-9]{4}[1-9]"

pass_no = input()

matcher = fullmatch(pattern, pass_no)

print("Invalid" if matcher == None else "Valid")