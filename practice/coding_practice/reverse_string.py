def reverseString(s):
    
        left = 0
        right = len(s)-1

        while left <= right:

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return s
    
    
lst = ["h","e","l","l","o"]

result = reverseString(lst)
print(result)