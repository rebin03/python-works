class Human():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print("I can eat")
        
    def work(self):
        print("I can work")
        
class Male(Human):
    
    def __init__(self, name, age, place):
        super().__init__(name, age)
        self.place = place
    
    def run(self):
        print("I can run")
        
    def work(self):
        super().work()
        print("I can code")
        
    def display(self):
        print(f"Hi, I'm {self.name}. {self.age} year old, from {self.place}")

person = Male("Alen", 23, "Delhi")

person.eat()
person.work()
print(person.name, person.age, person.place)
person.run()

person.display()