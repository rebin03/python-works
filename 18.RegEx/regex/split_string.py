# returning a list where string has been split at each match.

import re

text = "Python is a cross-platform language"

match_list = re.split("\s", text)

print(match_list)

# we can split string at first occurance by specifying number.
match_list2 = re.split("\s", text, 1)

print(match_list2)