from re import finditer

text = "hellopythonhellopythonhellopython"

count = 0

matcher = finditer("python", text) # Return object (start,group) ie, start:start index, group: pattern

for m in matcher:
    print(m.start(), "=>", m.group())
    count += 1

print("Count:", count)