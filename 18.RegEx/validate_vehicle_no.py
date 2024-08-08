# Validating vehicle number in Kerala

# Starting with KL
# Then 2 digits
# followed by alphabets (one or two)
# lastly 4 digits


from re import fullmatch

vehicle_no = "KL-08-AB-6547"

pattern = "(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"

matcher = fullmatch(pattern, vehicle_no)

print("Valid" if matcher != None else "Invalid")