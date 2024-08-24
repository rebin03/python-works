# ababba

def longest_palindromic_subsequence(text):
    
    longest_palindrome = ""
    
    for i in range(0,len(text)):
        
        left, right = i, i
        
        while(left>=0 and right<len(text) and text[left] == text[right]):
            
            current_palindrome = text[left:right+1]
            
            if len(current_palindrome) > len(longest_palindrome):
                longest_palindrome = current_palindrome
                
            left -= 1
            right += 1
            # print(current_palindrome)
            
    return longest_palindrome


print(longest_palindromic_subsequence("racecar"))