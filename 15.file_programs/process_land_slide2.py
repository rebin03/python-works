f = open("E:\\LUMINAR\\PythonJuneWorks\\15.file_programs\\land_slide.txt","r")

data = []

for l in f:
    
    lst = l.rstrip("\n").split(" ")
    dic = {"state":lst[0], "year":lst[1], "deaths":int(lst[2])}
    data.append(dic)
    
# print(data)



#-------------------------------------------------------------------------------------------------------------------------------------------
# 1) What is the total dead count



#-------------------------------------------------------------------------------------------------------------------------------------------
# 2) Which state has the most dead count



#-------------------------------------------------------------------------------------------------------------------------------------------
# 3) which year has the most dead count

    

#-------------------------------------------------------------------------------------------------------------------------------------------
# 4) What is the total dead count for each state across all years?

state_summary = {}

for dic in data:
    
    state = dic.get("state")
    death_count = dic.get("deaths")
    
    if state in state_summary:
        state_summary[state] += death_count
    else:
        state_summary[state] = death_count
print(state_summary)

#-------------------------------------------------------------------------------------------------------------------------------------------
# 5) What is the total dead count for each year across all states?

year_summary = {}

for dic in data:
    
    year = dic.get("year")
    death_count = dic.get("deaths")
    
    if year in year_summary:
        year_summary[year] += death_count
    else:
        year_summary[year] = death_count
print(year_summary)

#-------------------------------------------------------------------------------------------------------------------------------------------
# 6) Which state has the least dead count in 2020?



#-------------------------------------------------------------------------------------------------------------------------------------------
# 7) How many states have a dead count greater than 10 in 2021?



#-------------------------------------------------------------------------------------------------------------------------------------------
# 8) What is the average dead count per year for Kerala?



#-------------------------------------------------------------------------------------------------------------------------------------------
# 9) In which year did HimachalPradesh have the highest dead count?



#-------------------------------------------------------------------------------------------------------------------------------------------
# 10) How many times did the dead count exceed 50 in any state?



#-------------------------------------------------------------------------------------------------------------------------------------------
# 11) What is the combined dead count of Karnataka and Maharashtra in 2021?



#-------------------------------------------------------------------------------------------------------------------------------------------
# 12) Which state had zero deaths in any year?



#-------------------------------------------------------------------------------------------------------------------------------------------
# 13) How many years had a dead count of less than 5 across all states?



#-------------------------------------------------------------------------------------------------------------------------------------------
# 14) What is the difference in dead count between Kerala and Uttarakhand in 2021?



#-------------------------------------------------------------------------------------------------------------------------------------------
# 15) How many states have a cumulative dead count of less than 10 across all years?