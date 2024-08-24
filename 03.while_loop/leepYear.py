# print all leep years from 1800 to 2024

year = 1800

while(year <= 2024):
    if (year%4==0 and year%100 != 0 or year%400 ==0):
        print(year, end=" ")
    
    year += 1