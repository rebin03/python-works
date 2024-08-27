from abstract_class import Vehicle

class Bike(Vehicle):
    
    def __init__(self, number_tyres, color):
        super().__init__(number_tyres)
        self.color = color
        
    def start(self):
        print("Start with kick")

    def display(self):
        print(f"My color is {self.color} and I have {self.number_tyres} tyeres")
        
class Scooter(Vehicle):
    
    def __init__(self, number_tyres):
        super().__init__(number_tyres)
    
    def start(self):
        print("Start with self")
        
class Car(Vehicle):
    
    def __init__(self, number_tyres):
        super().__init__(number_tyres)
        
    def start(self):
        print("Start with key")