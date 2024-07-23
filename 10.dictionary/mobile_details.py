mobile = {"name":"realme7pro","brand":"realme","price":25000,"is_available":True, "offer":500}

if "offer" in mobile:
    
    selling_price = mobile.get("price") - mobile.get("offer")
    print(selling_price)
    
else:
    
    selling_price = mobile.get("price")
    print(selling_price)
