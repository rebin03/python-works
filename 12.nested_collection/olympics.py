olympic_medal_count = [
    {"country": "United States", "gold": 39, "silver": 41, "bronze": 33},
    {"country": "China", "gold": 38, "silver": 32, "bronze": 18},
    {"country": "Japan", "gold": 27, "silver": 14, "bronze": 17},
    {"country": "Great Britain", "gold": 22, "silver": 21, "bronze": 22},
    {"country": "Russia", "gold": 20, "silver": 28, "bronze": 23},
    {"country": "Australia", "gold": 17, "silver": 7, "bronze": 22},
    {"country": "Netherlands", "gold": 10, "silver": 12, "bronze": 14},
    {"country": "France", "gold": 10, "silver": 12, "bronze": 11},
    {"country": "Germany", "gold": 10, "silver": 11, "bronze": 16},
    {"country": "Italy", "gold": 10, "silver": 10, "bronze": 20}
]

#------------------------------------------------------------------------------------------------------------------------------------------ 
# 1) country with most number of gold medals

def get_gold_medel(country):
    return country.get("gold")

country_name = max(olympic_medal_count, key=get_gold_medel)
# print(country_name)

#------------------------------------------------------------------------------------------------------------------------------------------
# 2) medal count of each countries 

def get_total_medal(c):
    return c.get("gold") + c.get("silver") + c.get("bronze")

medel_count = {c.get("country"): get_total_medal(c) for c in olympic_medal_count}
# print(medel_count)

#------------------------------------------------------------------------------------------------------------------------------------------
# 3) country with least number of medals

least_medel_country = min(olympic_medal_count, key=get_total_medal) #(get_total_medel is already defined above)
# print(least_medel_country)

#------------------------------------------------------------------------------------------------------------------------------------------
# 4) sort countries with medal count

sorted_countries = sorted(olympic_medal_count, key=get_total_medal, reverse=True) #(get_total_medel is already defined above)
# print(sorted_countries)

#------------------------------------------------------------------------------------------------------------------------------------------
# 5) Which country has the highest total number of medals (sum of gold, silver, and bronze)?

highest_medel_country = max(olympic_medal_count, key=get_gold_medel)
# print(highest_medel_country)

#------------------------------------------------------------------------------------------------------------------------------------------
# 6) What is the average number of gold medals won by the countries listed?

gold_medels = [get_gold_medel(c) for c in olympic_medal_count]
# total_gold_medels = sum(gold_medels)

#------------------------------------------------------------------------------------------------------------------------------------------
# 7) What is the total number of medals (gold, silver, bronze) won by all countries combined?

country_total_medals = [get_total_medal(c) for c in olympic_medal_count]
total_medals = sum(country_total_medals)
# print(total_medals)

#------------------------------------------------------------------------------------------------------------------------------------------
# 8) How many countries won more than 20 gold medals?

countries_list = [c.get("country") for c in olympic_medal_count if c.get("gold") > 20]
country_no = len(countries_list)
# print(country_no)

#------------------------------------------------------------------------------------------------------------------------------------------
# 9) Rank the countries based on the total number of silver medals.

def get_silver_medel(country):
    return country.get("silver")

ranked_countries = sorted(olympic_medal_count, key=get_silver_medel, reverse=True)
# print(ranked_countries)

#------------------------------------------------------------------------------------------------------------------------------------------
# 10) Which country has the highest ratio of gold to total medals?

def get_ratio(c):
    ratio = get_gold_medel(c)/get_silver_medel(c)
    return ratio

highest_ratio = max(olympic_medal_count, key=get_ratio)
print(highest_ratio)