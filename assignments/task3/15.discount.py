def get_cost(quantity):
    
    cost = 100 * quantity
    if cost > 1000:
        discount = 0.1 * cost
        cost -= discount
        
    return cost


quantity = int(input("Enter the quantity(units) of product purchased: "))
print(f"The cost is: {get_cost(quantity)}")