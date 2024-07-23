
def is_leap_year(year):
    if year%4 == 0 and year%100 != 0 or year%100 == 0 and year%400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    if is_leap_year(year) and month == 2:
        return 29
    else:
        return days[month-1]

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

days = days_in_month(year, month)
print(f"Number of days are {days}")
