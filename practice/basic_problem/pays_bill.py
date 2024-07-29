import random

names = input("Enter everybody's name seperated by comma: ").split(",")
print(names)

index = random.randrange(0,len(names))
print(index)

print(f"{names[index]} will pay the bill")