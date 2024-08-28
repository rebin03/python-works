def is_leap_year(year):
    
    if year%400 == 0 or year%4 == 0 and year%100 != 0:
        return True
    else:
        return False
    


year = int(input("Enter year: "))
print("Leap year" if is_leap_year(year) else "Not a leap year")