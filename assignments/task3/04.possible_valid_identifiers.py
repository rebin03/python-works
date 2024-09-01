from re import fullmatch, finditer
import itertools


def generate_combinations(chars, n):
    
    combinations = itertools.permutations(chars, r=n)
    combinations = [''.join(comb) for comb in combinations]
    return combinations
    
    

length = int(input("Enter the length of identifier: "))
chars = input(f"Enter {length} charecters(seperated by space): ").split()

if length != len(chars):
    exit(f"Must have exactly {length} charecters")

pattern = "[a-zA-Z_]\\w*"
combinations = generate_combinations(chars, length)

identifiers = []

for comb in combinations:
     
    matcher = fullmatch(pattern, comb)
    
    if matcher != None:
        identifiers.append(comb)
        
print(f"Possible identifiers are: ")
for id in identifiers:
    print(id, end=", ")