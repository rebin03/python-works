class Human:
    # We can also define a class variable apart from the attributs inside the init method and access using it's object of itself or derived classes
    scientific_name = "Homo sapiens"  
    
    def __init__(self, num_heart):
        print("Calling init from Human class")
        self.num_heart = num_heart
        self.num_eyes = 2
        
    def eat(self):
        print("I can eat")
        
    def work(self):
        print("I can work")
        
class Male(Human):
    
    def __init__(self, name):
        print("Calling init from Male class")
        self.name = name
        
    def sleep(self):
        print("I can sleep")
    
    def work(self):
        print("I can code")
        
class Boy(Male):
    
    def __init__(self, heart, name, can_sing):
        Human.__init__(self, heart)
        Male.__init__(self, name)
        self.sing = can_sing
        
    
    def run(self):
        print("I can run")
    
    # Accessing all work methods from the base class and super base class into derived child's work method 
    def work(self):
        Human.work(self)
        Male.work(self)
        print("I can write program")
        
boy1 = Boy(1, "Alen", True)

# accessing methods
boy1.eat() # Calling method from parent class with derived class object
boy1.work()

# accessing attributes
print(boy1.num_heart)
print(boy1.num_eyes)
print(boy1.name)
print(boy1.sing)

# accessinf class variable
print(boy1.scientific_name)

# checking the MRO
print(Boy.mro())