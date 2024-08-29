class Duck:
    
    def swim(self):
        print("I'm a duck and I can swim.")
        
    def speaks(self):
        print("Quack Quack!")

class Dog:
    
    def swim(self):
        print("I'm a dog and I can swim.")
        
    def speaks(self):
        print("Woof Woof!")
        
class Person:
    
    def speaks(self):
        print("Blah Blah Blah")

class Display:
    
    def display(obj):
        obj.swim()
        obj.speaks()

duck = Duck()
dog = Dog()
person = Person()
d = Display
d.display(duck)
d.display(dog)
# d.display(person) # This will show error as the Person class don't have method speaks
