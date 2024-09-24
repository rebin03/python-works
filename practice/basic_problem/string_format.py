quantity = 5
product = "Apple"
price = 120

newOrder = "I want {} {} for {:.2f} rupees"

print(newOrder.format(quantity, product, price))


# We can also use index value in {} to change order

string = "{1} {0} {2}"
print(string.format(quantity, product, price))


# Adding same value more than once.
age = 20
name = "Joe"
new_text = "The player name is {1}. {1} is {0} year old!"
print(new_text.format(age, name))


# Adding named index inside {}
text = "I have a {car}, it is a {model}."
print(text.format(car = "BMW", model = "X5"))