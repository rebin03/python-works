# Program to calculate bmi(Body mass index)
# bmi = weight in kilograms (kg) / by height in meters (m) squared

weight_in_kg = int(input("Enter weight in Kg: "))
height_in_cm = int(input("Enter height in cm: "))

height_in_m = height_in_cm/100

height_in_m_sqr = height_in_m ** 2

bmi = weight_in_kg / height_in_m_sqr

print(f"bmi = {weight_in_kg} / {height_in_m_sqr} = {bmi}")
print(f"bmi of a person with height {height_in_cm}cm and weight {weight_in_kg}kg is {bmi}")