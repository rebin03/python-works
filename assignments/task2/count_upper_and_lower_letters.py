def count_upper_and_lower(string):
    
    upper_count = 0
    lower_count = 0
    
    for ch in string:
        
        if ch.isupper():
            upper_count += 1
        elif ch.islower():
            lower_count += 1
            
    return upper_count, lower_count



string = input("Enter your string: ")

upper, lower = count_upper_and_lower(string)

print(f"upper case: {upper}\nlower case: {lower}")