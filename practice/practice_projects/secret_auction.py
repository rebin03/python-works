import os

bidding_data = {}
highest_bid = 0

while(True):
    
    name = input("What id your name?: ")
    bid = int(input("What id your bid?: "))
    
    if bid > highest_bid:
        
        highest_bid = bid
    
    bidding_data[name] = bid
    
    print("Are there any other bidders? Type 'yes' or 'no'")
    
    decision = input()
    
    if decision == "yes":
        os.system('cls')
    elif decision == "no":
        for name in bidding_data:
            if bidding_data[name] == highest_bid:
                print(f"The winner is {name} with a bid of {highest_bid}")
        break
    else:
        print("invelid option")
        
        
 
        
    