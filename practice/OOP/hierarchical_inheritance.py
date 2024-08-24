class Human:
    
    def __init__(self, name, age):
        print("Calling init from Human class")
        self.name = name
        self.age = age
    
    def eat(self):
        print("I can eat")
        
    def show_details(self):
        print(f"Name: {self.name}\nAge: {self.age}")
        
class Male(Human):
    
    def __init__(self, name, age, location):
        print("Calling init from Male class")
        Human.__init__(self, name, age)
        self.location = location
        
    def sleep(self):
        print("I can sleep")
        
    def show_details(self):
        super().show_details()
        print(f"Location: {self.location}")
        
class Female(Human):
    
    def __init__(self, name, age, can_dance):
        super().__init__(name, age)
        self.can_dance = can_dance
    
    def work(self):
        print("I can code")
        
    def show_details(self):
        Human.show_details(self)
        print(f"Can dance: {self.can_dance}")
        
# Initializing objects of derived classes         
male = Male("Steve", 25, "Delhi")
female = Female("Jane", 24, True)

# Accessing base class method using derived class object
male.eat()
female.eat()

# Accessing base class attributes using derived class object
print(male.name, male.age)
print(female.name, female.age)

# show_details() method is defined in both derived classes and base class. We access the base class method to the derived class method using super() function
male.show_details()
female.show_details()

# MRO
print(Male.mro())
print(Female.mro())