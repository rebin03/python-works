import re

text = "The match in Germany"

x = re.search("^The.*Germany$", text)
# print(x)

if x:
    print('Yes! We have a match')
else:
    print('No match')