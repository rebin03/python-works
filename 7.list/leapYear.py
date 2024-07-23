year = [1000,1002,2000,2004,2001,2008,2016,2028,1800]

for i in range(0,len(year)):
    if year[i]%100 == 0 and year[i]%400 == 0 or year[i]%100 != 0 and year[i]%4 == 0:
        
        print(year[i])