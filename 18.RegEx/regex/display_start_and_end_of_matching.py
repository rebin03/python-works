# display start and end position of matching string

import re

text = "Python is an dynamicaly typed language."

matcher = re.search("typed", text)

# print position
print(matcher.span())