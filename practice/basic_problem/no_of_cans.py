import math

def paint_can_cal(height, width, cover):
    
    can_numbers = (height*width)/cover
    
    return math.ceil(can_numbers)

h = int(input("Enter the height of wall: "))
w = int(input("Enter the width of wall: "))
coverage = 7

result = paint_can_cal(width=w, height=h, cover=coverage)
print(f"You will need {result} cans of paint.")