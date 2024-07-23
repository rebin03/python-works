words = ["madam","aba","bcb","hello","python"]

def is_palindrome(word):
    reversed_str = word[::-1]
    return reversed_str == word

for i in range(0,len(words)):
    if is_palindrome(words[i]):
        print(words[i])