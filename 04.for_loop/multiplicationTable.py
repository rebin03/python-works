# print multiplication table of a number


number = int(input("Enter number: "))

for i in range(1,11):
    print(f"{i} x {number} = {i*number}")