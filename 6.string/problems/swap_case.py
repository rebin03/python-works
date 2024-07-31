def swap_case(s):
    rev = ""
    for i in range(len(s)):
        if s[i].isupper():
            rev += s[i].lower()
        elif s[i].islower():
            rev += s[i].upper()
        else:
            rev += s[i]
    return rev

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)