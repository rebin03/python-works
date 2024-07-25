# user_input = "({[]})" => valid
# user_input = "([)]" => invalid

# use dict,stack

text = "[]"
parenthesis = {")":"(","]":"[","}":"{",">":"<"}
stack = []

is_valid = True
for c in text:
    if c in parenthesis.values():
        stack.append(c)
    elif c in parenthesis.keys():
        if stack == [] or parenthesis[c] != stack.pop():
            is_valid = False
            break
        

if is_valid and stack == []:
    print("valid")
else:
    print("invalid")