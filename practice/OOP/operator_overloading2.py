class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __gt__(self, other):
        return self.age > other.age


p1 = Person("Shan", 33)
p2 = Person("Salman", 28)

if p1 > p2:
    print(f"{p1.name} pays the bill")
else:
    print(f"{p2.name} pays the bill")