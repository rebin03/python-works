from re import fullmatch

f_read = open("E:\\LUMINAR\\PythonJuneWorks\\18.RegEx\\vehicle_no.txt","r")
f_write = open("E:\\LUMINAR\\PythonJuneWorks\\18.RegEx\\valid_vehicle_no.txt","w")

pattern = "(KL)\\s?[0-9]?[1-9]\\s?[A-Z]{1,2}\\s?[0-9]{4}"

for line in f_read:
    
    vehicle_no = line.rstrip("\n")
    
    matcher = fullmatch(pattern, vehicle_no)
    
    if matcher != None:
        f_write.write(vehicle_no + "\n")