# A metaclass in Python is a class of a class that defines how a class behaves. 
# A class is itself an instance of a metaclass. 
# A class in Python defines how the instance of the class will behave. 

class Meta(type):
    def __new__(self, class_name, bases, attrs):
        
        # Here we can define how the classes should behave. that logic goes here
        a = {}
        for name, val in attrs.items():
            if name.startswith('__'):
                a[name] = val
            
            # converts the attrs other than dunder methods to uppercase
            else:
                a[name.upper()] = val
                
        return type(class_name, bases, a)
    
    
class Test(metaclass=Meta):
    x = 5
    y = 8
    
    def hello(self):
        print('hello from test')
        
t = Test()
print(t.X)
print(t.Y)
t.HELLO()