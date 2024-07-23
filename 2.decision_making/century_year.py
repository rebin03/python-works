# read a year from user and print century if year ends with two zeros
# else print no century year

year = int(input("Enter year: "))

if year%100 == 0:
    print("Century year")
else:
    print("Not century year")