
def is_leap_year(year):
    if year%100 == 0 and year%400 == 0 or year%100 != 0 and year%4 == 0:
        return True
    else:
        return False
    

# calling the fuction
print(is_leap_year(2021))