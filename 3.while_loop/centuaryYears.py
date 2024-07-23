# print all centuary years from 1800 to 2024

year = 1800

while(year <= 2024):
    if year%100 == 0:
        print(year, end=" ")
        
    year += 1