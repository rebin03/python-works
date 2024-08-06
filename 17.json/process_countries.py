from json import load

f = open("E:\\LUMINAR\\PythonJuneWorks\\17.json\\countries.json","r",encoding="UTF-8")

country_data = load(f)
# print(country_data)
# print(len(country_data))


#--------------------------------------------------------------------------------------------------------------------------------------------
# 1. Find the largest populated country.    

# def get_population(c):
#     return c.get("population")

largest_populated_country = max(country_data, key=lambda c:c.get("population"))
# print(f"{largest_populated_country.get("name")} : {largest_populated_country.get("population")}")

#--------------------------------------------------------------------------------------------------------------------------------------------
# 2. How many countries are independent?

count = 0
for c in country_data:
    if c.get("independent"):
        count += 1
# print(count)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 3. List out the countries in the subregion Western Asia.

countries_western_asia = [c.get("name") for c in country_data if c.get("subregion") == "Western Asia"]
# print(countries_western_asia)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 4. Find all countries where the currency is Euro (EUR) and not in the region Europe.
        
def is_euro(c):
    if c.get("currencies") != None:
        for curr in c.get("currencies"):
            return curr.get("code") == "EUR" 

country_currency_filter = [c.get("name") for c in country_data if is_euro(c) and c.get("region") != "Europe"]
# print(country_currency_filter)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 5. Which countries have more than one official language?

country_language_filter = [c.get("name") for c in country_data if len(c.get("languages")) > 1]
# print(country_language_filter)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 6. List all countries that share a border with more than five other countries.

def get_border_count(c):
    if c.get("borders") != None:
        return len(c.get("borders"))
    else:
        return 0

country_border_filter = [c.get("name") for c in country_data if get_border_count(c) > 5]
# print(country_border_filter)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 7. Find the country with the smallest area.

def get_area(c):
    return c.get("area") if c.get("area") is not None else float('inf')

smallest_country = min(country_data, key=get_area)
# print(smallest_country.get("name"))

#--------------------------------------------------------------------------------------------------------------------------------------------
# 8. Which countries have a Gini index above 40?

countries_gini_filter = [c.get("name") for c in country_data if c.get("gini") != None and c.get("gini") > 40]
# print(countries_gini_filter)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 9. List all countries in the region Africa with a population density greater than 100 people per square kilometer.

filtered_country = [c.get("name") for c in country_data if c.get("region") == "Africa" and c.get("area") is not None and (c.get("population")/c.get("area")) > 100]
# print(filtered_country)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 11. Which countries have timezones that include UTC+00:00?

country_timezone = [c.get("name") for c in country_data if "UTC+00:00" in c.get("timezones")]
# print(country_timezone)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 12. List all countries with a capital that starts with the letter 'A'.

country_capitalA = [c.get("name") for c in country_data if c.get("capital") is not None and c.get("capital").startswith("A")]
# print(country_capitalA)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 13. Find countries where the demonym is the same as the country name.

country_demonym_filter = [c.get("name") for c in country_data if c.get("demonym") == c.get("name")]
# print(country_demonym_filter)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 14. Which countries are part of the South Asian Association for Regional Cooperation (SAARC)?

def get_regional_blocs(c):
    if c.get("regionalBlocs") is not None:
        for rb in c.get("regionalBlocs"):
            return rb.get("acronym")
        
countries_rb_filter = [c.get("name") for c in country_data if get_regional_blocs(c) == "SAARC"]
# print(countries_rb_filter)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 15. List countries that have more than one timezone.

country_timezone_filter = [c.get("name") for c in country_data if len(c.get("timezones")) > 1]
# print(country_timezone_filter)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 16. Find the country with the highest latitude.

def get_latitude(c):
    return c.get("latlng")[0] if c.get("latlng") is not None else 0

highest_lat_country = max(country_data, key=get_latitude)
# print(highest_lat_country.get("name"))

#--------------------------------------------------------------------------------------------------------------------------------------------
# 17. Which countries have numeric codes that start with the digit '0'?

countries_numericode_startswith0 = [c.get("name") for c in country_data if c.get("numericCode").startswith("0")]
# print(countries_numericode_startswith0)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 18. List countries where the top-level domain (TLD) is '.co'.

countries_toplevelDomain_filter = [c.get("name") for c in country_data if ".co" in c.get("topLevelDomain")]
# print(countries_toplevelDomain_filter)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 19. Find all countries with a calling code that starts with '3'.

countries_callingcode_filter = [c.get("name") for c in country_data for cc in c.get("callingCodes") if cc.startswith("3")]
# print(countries_callingcode_filter)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 20. Find the countries that are located in the region Asia and have a border with India.

def is_border_with_ind(c):
    if c.get("borders") is not None:
        if "IND" in c.get("borders"):
            return True

countries_region_filter = [c.get("name") for c in country_data if is_border_with_ind(c) and c.get("region") == "Asia"]
# print(countries_region_filter)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 21. Which countries have alternate spellings that include the word 'Republic'?

def is_altSpelling_with_republic(c):
    if c.get("altSpellings") is not None:
        for w in c.get("altSpellings"):
            if "Republic" in w:
                return True

countries_altSpelling_filter = [c.get("name") for c in country_data if is_altSpelling_with_republic(c)]
# print(countries_altSpelling_filter)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 22. List countries that are part of the African Union (AU).

countries_AU = [c.get("name") for c in country_data if get_regional_blocs(c) == "AU"]
# print(countries_AU)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 23. List all countries with a population less than 1 million.

countries_population_filter = [c.get("name") for c in country_data if c.get("population") < 1000000]
# print(countries_population_filter)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 24. Find countries where the capital city's name is the same as the country's name.

countries_capital_filter = [c.get("name") for c in country_data if c.get("capital") == c.get("name")]
# print(countries_capital_filter)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 25. Which countries have regional blocs that include 'European Union'?

countries_EU = [c.get("name") for c in country_data if get_regional_blocs(c) == "EU"]
# print(countries_EU)

#--------------------------------------------------------------------------------------------------------------------------------------------
# 26. Find the otherNames of given country if no otherNames print country name

def fetch_country_by_name(name):
    return [c for c in country_data if c.get("name") == name][0]

country_data_by_name = fetch_country_by_name("Ivory Coast")

if "regionalBlocs" in country_data_by_name:
    bloc_data = country_data_by_name.get("regionalBlocs")[0]
    
    # if "otherNames" in bloc_data:
    #     print(bloc_data.get("otherNames"))
    # else:
    #     print(country_data_by_name.get("name"))
        
#--------------------------------------------------------------------------------------------------------------------------------------------
# 27. largest region by area

all_region = list({c.get("region") for c in country_data})
region_dict = {}

for c in country_data:
    
    r = c.get("region")
    
    if r in region_dict :
        region_dict[r] += c.get("area", 0)
    else:
        region_dict[r] = c.get("area", 0)


value_key = [(v,k) for k,v in region_dict.items()]
largest_region = max(value_key)       
print(largest_region)
        