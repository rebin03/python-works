from re import fullmatch

pattern = "[a-zA-Z_]\\w*"

text = "var _name hello 0age is_true 3hello"

valid_ids = [txt for txt in text.split() if fullmatch(pattern, txt) != None]
print(valid_ids)