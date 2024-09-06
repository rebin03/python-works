class Vehicle:
    
    def start(self):
        print("Vehicle start method")
        
    def accelerate(self):
        print("Vehicle accelerate method")
        
class Car(Vehicle):
    
    pass

swift = Car()

swift.start()
swift.accelerate()