text ="ABABCDE"

char_count = {}

for char in text:
    
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Non recursive charecter are: ", end="")
for key,value in char_count.items():

    if value == 1:
        print(key, end=" ")