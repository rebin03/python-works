from re import finditer

text = "abc123 @K#7LM!&def"

pattern1 = "[abf]" # [abf] will check for either a,b or f ("abf" will check for the pattern abf in text)

pattern2 = "[a-k]" # [a-k] Check for alphabets from a to k

pattern3 = "[a-z]" # [a-z] Check for all lower case alphabets

pattern4 = "[A-Z]" # [A-Z] Check for all upper case alphabets

pattern5 = "[a-zA-Z]" # [a-zA-Z] Check for all alphabets

pattern6 = "[0-9]" # [0-9] or "\d" Check for digits

pattern7 = "[a-zA-Z0-9]" # [a-zA-Z0-9] or "\w" Check for alphanumeric characters

pattern8 = "[^0-9]" # [^0-9] or "\D" Check for all charecters other than digits (^ symbol exclude the specified patterns)

pattern9 = "[^a-zA-Z0-9]" # [^a-zA-Z0-9] or "\W" Check for special charecters and space

pattern10 = "[\s]" # Check for space

pattern11 = "[^a-zA-Z0-9\s]" # Check only for special charecters

matcher = finditer(pattern11, text)

for m in matcher:
    print(m.start(), "=>", m.group())