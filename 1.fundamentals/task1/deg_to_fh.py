# program to convert temperature in degreecelsius to fh

# °F = ((9/5) * °C ) + 32

tem_in_deg = int(input("Enter temperature in °C: "))

tem_in_fh = ((9/5) * tem_in_deg) + 32

print(f"{tem_in_deg}°C is equal to {tem_in_fh}°F")