mobile = {"name":"realme7pro","brand":"realme","price":25000,"is_available":True}

print(mobile.get("name")) # return None if the key is not available
print(mobile["name"]) # return key error if key is not available

print(mobile.keys())
print(mobile.values())

popped_item = mobile.pop("brand")
print(popped_item)

mobile["offer"] = 500
print(mobile)

# print("\n")
# for k,v in mobile.items():
#     print(k, end=" => ")
#     print(v)