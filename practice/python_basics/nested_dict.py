studend_data = {
    "Ram":{"roll_no":10, "age":20,"course":"Python"},
    "Mohan":{"roll_no":20, "age":22,"course":"Java"},
    "rebin":[35, 22, "Python"]
}

print(studend_data)
print(studend_data["Mohan"])

print(studend_data["Mohan"]["course"])

studend_data["Ram"]["phone_no"] = 3234567544
print(studend_data["Ram"])

del studend_data["Ram"]["phone_no"]
print(studend_data["Ram"])

studend_data["Mohan"]["phone_no"] = 8786543886
print(studend_data["Mohan"])

print(f"Popped value = {studend_data["Mohan"].pop("phone_no")}")
print(studend_data["Mohan"])

print(studend_data["rebin"][2])