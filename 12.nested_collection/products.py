mobiles=[
    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]

mobile_names = [dict.get("title") for dict in mobiles]
print(mobile_names)

brand_names = {dict.get("brand") for dict in mobiles}
print(brand_names)

samsung_mobile_name = [dict.get("title") for dict in mobiles if dict.get("brand") == "samsung"]
print(samsung_mobile_name)

price_filter = [dict.get("title") for dict in mobiles if dict.get("price") in range(23000,40001)]
print(price_filter)

max_price = 0
for dict in mobiles:
    if dict.get("price") > max_price:
        max_price = dict.get("price")
print(max_price)
costly_mobile = [dict.get("title") for dict in mobiles if dict.get("price") == max_price]
print(costly_mobile)