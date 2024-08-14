class Circle():
    pi = 3.14 # class object attribute
    
    def __init__(self, radius):
        self.radius = radius
        self.area = self.pi * self.radius ** 2 # Attribute of an object can be more despite of the parameter in the function
    
    def get_area(self):
        res = self.pi * self.radius ** 2
        return res
    
    def circumference(self):
        res = 2 * Circle.pi * self.radius # we can write class obj attribute with ClassName or self (ie, Circle.pi or self.pi)
        return res
    
    
circle = Circle(4)

print(circle.circumference())
print(circle.get_area()) # Area calculated using get_area() method of class Circle
print(circle.area) # Area as the attribute of the circle object
