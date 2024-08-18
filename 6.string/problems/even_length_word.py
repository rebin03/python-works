def even_length(string):
    
    arr = string.split(" ")
    res = ""
    
    for word in arr:
        if len(word) % 2 == 0:
            res += word + " "
    
    return res

string = "This is a python language"
print(even_length(string))