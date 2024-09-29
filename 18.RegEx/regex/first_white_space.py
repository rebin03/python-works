# Searching fot first white space

import re

text = 'The rain in Germany'

searching = re.search('\\s', text)

print("The first white space is located in position: ", searching.start())