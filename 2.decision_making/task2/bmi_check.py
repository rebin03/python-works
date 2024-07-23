weight_in_kg = int(input("Enter weight in Kg: "))
height_in_cm = int(input("Enter height in cm: "))

height_in_m = height_in_cm/100

height_in_m_sqr = height_in_m ** 2

bmi = weight_in_kg / height_in_m_sqr

if bmi<19:
    print("Under weight")
elif bmi<25:
    print("Normal weight")
elif bmi<35:
    print("Over weight")
else:
    print("Obesity")
