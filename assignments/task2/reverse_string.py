def reverse_string1(string): # Using string slicing
    
    return string[::-1]

def reverse_string2(string): # Iterating through each char
    
    res = ""
    
    for ch in string:
        res = ch + res
        
    return res

string = input("Enter the string: ")
print(reverse_string1(string))
print(reverse_string2(string))