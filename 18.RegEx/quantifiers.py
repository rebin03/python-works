from re import finditer

text = "ab12xyz678#$pqr123cdef"

pattern1 = "[a-z]{3}" # [a-z]{3} will check with the given limit. ie, here with 3 consecutive occuring alphabet patterns.

pattern2 = "([c-h]|[t-z])" # chech for the alphabets in the range c-h or t-z

pattern3 = "([a-z]{3}|[0-9]{3})" # Check for 3 consecutive digit ot alphabets in the given text

matcher = finditer(pattern3, text)

for m in matcher:
    print(m.start(),"=>",m.group())