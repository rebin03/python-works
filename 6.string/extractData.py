email = "rebin@gmail.com"

at_index = email.index("@")

username = email[:at_index]
domain = email[at_index:]

print(username)
print(domain)