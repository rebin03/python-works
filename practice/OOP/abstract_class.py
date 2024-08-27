from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    def __init__(self, number_tyres):
        self.number_tyres = number_tyres
        
    @abstractmethod  
    def start(self):
        pass