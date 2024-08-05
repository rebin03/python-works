from json import load

f = open("E:\\LUMINAR\\PythonJuneWorks\\17.json\\products.json", "r", encoding="UTF-8")

products = load(f)

# print(len(products))

#-------------------------------------------------------------------------------------------------------------------------------------------
# 1) Print title of all products

product_titles = [item.get("title") for item in products]
# print(product_titles)


#-------------------------------------------------------------------------------------------------------------------------------------------
# 2) Print title of products in the category jewelery

jewelery_products = [item.get("title") for item in products if item.get("category") == "jewelery"]
# print(jewelery_products)


#-------------------------------------------------------------------------------------------------------------------------------------------
# 3) filter the products with price greater than 100

price_filter = [item.get("title") for item in products if item.get("price") > 100]
# print(price_filter)


#-------------------------------------------------------------------------------------------------------------------------------------------
# 4) filter the products with price in the range of 100 and 150

price_filter_range = [item.get("id") for item in products if item.get("price") >= 100 and item.get("price") <= 150]
# print(price_filter_range)


#-------------------------------------------------------------------------------------------------------------------------------------------
# 5) Product with most number of rating.

def get_rating_count(dic):
    return dic.get("rating").get("count")

highest_reviwed_product = max(products, key=get_rating_count)
print(f"{highest_reviwed_product.get("title")}\nCount : {highest_reviwed_product.get("rating").get("count")}")
        