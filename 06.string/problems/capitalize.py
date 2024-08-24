def solve(s):
    result = ""
    capitalization = True
    for ch in s:
        if ch == ' ':
            result += ch
            capitalization = True
        elif capitalization:
            result += ch.upper()
            capitalization = False
        else:
            result += ch
    return result

s = input()

result = solve(s)
print(result)
