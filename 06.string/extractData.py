email = "rebin@gmail.com"

at_index = email.index("@")

username = email[:at_index]
domain = email[at_index + 1:]

print(username)
print(domain)