class Dishes:
    
    def __init__(self, name, price, calories):
        
        self.name = name
        self.price = price
        self.calories = calories
        
    def __str__(self):
        return self.name
    
class Restaurant:
    
    def __init__(self, name, place):
        
        self.name = name
        self.place = place
        self.dishes = []
        
    def add_dish(self, dish):
        self.dishes.append(dish)
        
    def list_dishes(self):
        
        for dish in self.dishes:
            print(dish)
            

biryani = Dishes("Biryani", 110, 500)
mandi = Dishes("Mandi", 240, 100)
dosa = Dishes("Dosa", 70, 60)

restaurant1 = Restaurant("Rahmath", "Kozhikode")

restaurant1.add_dish(biryani)
restaurant1.add_dish(mandi)
restaurant1.add_dish(dosa)

restaurant1.list_dishes()