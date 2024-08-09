import random

num_list = [0,1,2,3,4,5,6,7,8,9]
alph_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbol_list = ["~","!","@","#","$","%","^","&","*","(",")","+"]

print("Welcome to Password Generator!")
letter_no = int(input("How many letters would you like in your password?\n"))
symbol_no = int(input("How many symbols would you like?\n"))
number_no = int(input("How many number would you like?\n"))

password = ""

for i in range(letter_no):
    password += random.choice(alph_list)
    
for i in range(symbol_no):
    password += random.choice(symbol_list)

for i in range(number_no):
    password += str(random.choice(num_list))

password = list(password)
random.shuffle(password)
password = "".join(password)
print(password)