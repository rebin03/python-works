f = open("E:\\LUMINAR\\PythonJuneWorks\\15.file_programs\\land_slide.txt","r")

land_slide = {}

for line in f:
    
    lst = line.split()
    state = lst[0]
    year = int(lst[1])
    dead_count = int(lst[2])
    
    if state not in land_slide:
        land_slide[state] = {}
    
    land_slide[state][year] = dead_count

# print(land_slide)



#-------------------------------------------------------------------------------------------------------------------------------------------
# 1) What is the total dead count

total_dead_count = 0

for state in land_slide:
    for year in land_slide[state]:
        total_dead_count += land_slide[state][year]
        
# print(total_dead_count)

#-------------------------------------------------------------------------------------------------------------------------------------------
# 2) Which state has the most dead count

larger_count = 0
for state in land_slide:
    state_total = sum(land_slide[state].values())
    
    if state_total > larger_count:
        larger_count = state_total
        larger_count_state = state
        
# print(larger_count_state)
        

#-------------------------------------------------------------------------------------------------------------------------------------------
# 3) which year has the most dead count

year_count = {}

for state in land_slide:
    for year in land_slide[state]:
        
        if year in year_count:
            year_count[year] += land_slide[state][year]
        else:
            year_count[year] = 0

most_count_year = max(year_count, key=year_count.get)
# print(most_count_year)
    

#-------------------------------------------------------------------------------------------------------------------------------------------
# 4) What is the total dead count for each state across all years?

for state in land_slide:
    state_total1 = sum(land_slide[state].values())
    # print(f"{state}: {state_total1}")

#-------------------------------------------------------------------------------------------------------------------------------------------
# 5) What is the total dead count for each year across all states?

year_dead_count = {}

for state in land_slide:
    for year in land_slide[state]:
        
        if year in year_dead_count:
            year_dead_count[year] += land_slide[state][year]
        else:
            year_dead_count[year] = 0

# print(year_dead_count)

#-------------------------------------------------------------------------------------------------------------------------------------------
# 6) Which state has the least dead count in 2020?

least_count = 10000

for state in land_slide:
    for year in land_slide[state]:
        
        if year == 2020 and land_slide[state][year] < least_count:
            least_count = land_slide[state][year]
            least_count_state = state
                
# print(least_count_state)

#-------------------------------------------------------------------------------------------------------------------------------------------
# 7) How many states have a dead count greater than 10 in 2021?

for state in land_slide:
    for year in land_slide[state]:
        
        if year == 2021 and land_slide[state][year] > 10:
            # print(state)
            pass

#-------------------------------------------------------------------------------------------------------------------------------------------
# 8) What is the average dead count per year for Kerala?



#-------------------------------------------------------------------------------------------------------------------------------------------
# 9) In which year did HimachalPradesh have the highest dead count?

highest_cnt = 0

for state in land_slide:
    for year in land_slide[state]:
        
        if state == "HimachalPradesh" and land_slide[state][year] > highest_cnt:
            highest_cnt = land_slide[state][year]
            highest_cnt_year = year

print(highest_cnt_year)

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