# Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes.
# We can use the method mro() to find the MRO of the child class
# mro() method - it returns a list
# _mro_ attribute - it returns a tuple

class Human:
    
    def __init__(self, num_heart):
        print("Calling init from Human")
        self.num_eyes = 2
        self.num_nose = 1
        self.heart = num_heart
    
    def eat(self):
        print("I can eat")
        
    def work(self):
        print("I can work")
        

class Male:
    
    def __init__(self, name):
        self.name = name
    
    def run(self):
        print("I can run")
    
    def work(self):
        print("I can code")
        
# Child class (Multiple Inheritance)

class Boy(Human, Male):
    
    def __init__(self, name, heart, language):
        Male.__init__(self, name)
        Human.__init__(self, heart)
        self.language = language
    
    def sleep(self):
        print("I can sleep")
        
    def work(self):
        print("I can test")
        
    def display(self):
        print(f"My name is {self.name} and I'm working on {self.language}")
        

boy1 = Boy("John", 1, "Python")

boy1.work()
Male.work(boy1) # We can access the parent method with same name by specifying class name.
Human.work(boy1)
print(Boy.mro()) # This will return MRO in list: [<class '__main__.Boy'>, <class '__main__.Human'>, <class '__main__.Male'>, <class 'object'>]
print(Boy.__mro__) # This will return MRO in tuple: (<class '__main__.Boy'>, <class '__main__.Human'>, <class '__main__.Male'>, <class 'object'>)

print(boy1.num_eyes, boy1.num_nose)

boy1.display()