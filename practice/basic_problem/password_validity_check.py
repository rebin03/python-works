def is_valid_password(password):
    
    spcl_char = ["@","#","$","%","&","*","^","!","~"]
    
    is_char_present = False
    is_digit_present = False
    is_alpha_present = False
    is_upper_present = False

    
    for ch in password:
        
        if ch in spcl_char:
            is_char_present = True
        elif ch.isdigit():
            is_digit_present = True
        elif ch.isalpha() and ch.islower():
            is_alpha_present = True
        elif ch.isalpha() and ch.isupper():
            is_upper_present = True
        
    if is_alpha_present and is_char_present and is_digit_present and is_upper_present:
        return True
    else:
        return False
    

password = input("Enter password: ")

if len(password) < 8:
    print("Password must contain atleast 8 charecters")
elif is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")
    print("Passwprd must contain an upper case, a number and a special charecter!!!")