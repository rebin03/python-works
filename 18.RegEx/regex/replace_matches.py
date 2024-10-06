# Replacing matches with the text of your choice.

import re

text = "Python is an dynamicaly typed language. Python is object oriented language"

new_text = re.sub("Python", "JavaScript", text)

print(new_text)

# we can control the number of replacement

new_text2 = re.sub("Python", "JavaScript", text, 1)

print(new_text2)