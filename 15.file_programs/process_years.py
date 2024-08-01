f_read = open("E:\\LUMINAR\\PythonJuneWorks\\15.file_programs\\years.txt","r")
f_centuary = open("E:\\LUMINAR\\PythonJuneWorks\\15.file_programs\\centuary.txt","w")
f_non_centuary = open("E:\\LUMINAR\\PythonJuneWorks\\15.file_programs\\non_centuary.txt","w")


for year in f_read:
    
    y = int(year.rstrip("\n"))
    
    if y%100 == 0:
        
        f_centuary.write(str(y) + "\n")
        
    else:
        
        f_non_centuary.write(str(y) + "\n")