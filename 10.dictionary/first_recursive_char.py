text = "ABCADD"

recursive_char = {}

for ch in text:
    
    if ch in recursive_char:
        print("First recursive charecter is",ch)
        break
    else:
        recursive_char[ch] = 1