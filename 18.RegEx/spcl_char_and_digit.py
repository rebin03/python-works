from re import finditer

text = "abc 7Klefg@#"

pattern1 = "\d" # Same as [0-9], which check for digits

pattern2 = "\D" # Same as ^[0-9], which exclude digits

pattern3 = "\w" # Same as [a-zA-Z0-9], which check for alphanumeric chars

pattern4 = "\W" # Same as [^a-zA-Z0-9], which exclude alphanumeric chars


matcher = finditer(pattern4, text)

for m in matcher:
    print(m.start(), "=>", m.group())