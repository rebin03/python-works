from abc import ABC, abstractmethod

class Car(ABC):
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    
class Swift(Car):
    
    def start(self):
        print("Swift start method")
    
    def accelerate(self):
        print("Swift accelerate method")
    
    def stop(self):
        print("Swift stop method")
        
        
car = Swift()
car.start()