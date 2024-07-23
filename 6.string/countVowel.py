text = "pneumonoultramicroscopicsilicovolcanoconiosis"

vowels = "aeiou"
v_count = 0
c_count = 0
text = text.casefold()

for letter in text:
    if vowels.count(letter) != 0:
        v_count += 1
    else:
        c_count += 1

print(f"Vowel count: {v_count}")
print(f"Consonants count: {c_count}")


# another logic
count =0
for ch in vowels:

    count += text.count(ch)

print(count)