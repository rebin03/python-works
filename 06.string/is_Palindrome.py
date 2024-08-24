def is_palindrome(word):
    reversed_str = word[::-1]
    return reversed_str == word


print(is_palindrome("malayalam"))