import random

names = input("Enter everybody's name seperated by comma: ").split(",")
print(names)

name = random.choice(names)
print(f"{name} will pay the bill")