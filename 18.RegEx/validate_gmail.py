from re import fullmatch

pattern = "\\w[\\w._]*@gmail.com"

email_id = input()

matcher = fullmatch(pattern, email_id)

print("Invalid" if matcher == None else "Valid")