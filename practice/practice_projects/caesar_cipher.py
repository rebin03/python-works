
alphabets = "abcdefghijklmnopqrstuvwxyz"

def encrypt(message, shift):
    result = ""
    for ch in message:
        if ch in alphabets:
            x = alphabets.index(ch)
            index = (x+shift)%26
            result += alphabets[index]
        else:
            result += ch
    return result

def decrypt(message, shift):
    result = ""
    for ch in message:
        if ch in alphabets:
            x = alphabets.index(ch)
            i_val = x-shift
            if i_val < 0:
                index = (i_val+26)%26
            else:
                index = (x-shift)%26
            result += alphabets[index]
        else:
            result += ch
    return result

is_continue = True

while is_continue:
    
    selection = input("Type 'encrypt' for encryption, type 'decrypt' for decreption:\n")
    msg = input("Type your message:\n").lower()
    shift_no = int(input("Type the shift number:\n"))
    
    if selection == "encrypt":
        encrypted_msg = encrypt(message=msg, shift=shift_no)
        print(f"Here is the encrypted result: {encrypted_msg}")
    elif selection == "decrypt":
        deycrypted_msg = decrypt(message=msg, shift=shift_no)
        print(f"Here is the decrypted result: {deycrypted_msg}")
    else:
        print(f"Invalid command '{selection}'")
    
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    
    if go_again == "yes":
        is_continue = True
    elif go_again == "no":
        is_continue = False
        print("Good bye!")
    else:
        print(f"invalid command '{go_again}'")
        break