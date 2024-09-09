class Parent:
    
    def bike(self):
        print("Passion Pro")
        
    def mobile(self):
        print("Samsung A20")

class Child(Parent):
    
    def bike(self):
        print("Himalaya")
        
    def mobile(self):
        print("I Phone")
        
ch = Child()

ch.bike()
ch.mobile()