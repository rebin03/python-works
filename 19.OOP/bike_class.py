class Bike:
    
    name:str
    brand:str
    price:int
    
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price
        
    def __str__(self):
        return self.name
    
class ShowRoom:
    
    name:str
    place:str
    bikes:list
    
    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.bikes = []
        
    def add_vehicle(self, bike):
        self.bikes.append(bike)
        
    def list_vehicle(self):
        
        for b in self.bikes:
            print(b)
            
            
activa = Bike("Activa", "Honda", 100000)
himalaya = Bike("Himalaya", "RE", 100000)
dominar = Bike("Dominar", "Bajaj", 100000)


showroom = ShowRoom("popular", "Ernakulam")

showroom.add_vehicle(activa)
showroom.add_vehicle(himalaya)
showroom.add_vehicle(dominar)

showroom.list_vehicle()