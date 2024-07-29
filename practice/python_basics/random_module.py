import random

# randint(a,b) - return integer number in a given range (a,b) where a and b included
a = random.randint(1,5)
print(a)

# randrange(a,b) - return integer number in a given range (a,b) where a included and b excluded
a = random.randrange(1,5)
print(a)

# random(a,b) - return floating number in the range (0,1) where 0 included and 1 excluded
a = random.random()
print(a)

# uniform(a,b) - return floating number in a given range (a,b) where a included and b excluded
a = random.uniform(1,5)
print(a)

# choice(list) - return random object from the given list
l = [30,21,56,-1,4,60,45,-5]
a = random.choice(l)
print(a)

# choices(list, k=3) - Return a k sized list of random elements from the given list
l = [30,21,56,-1,4,60,45,-5]
a = random.choices(l,k=2)
print(a)

# shuffle(list) - Return a k sized list of random elements from the given list
lst = [30,21,56,-1,4,60,45,-5]
random.shuffle(lst)
print(lst)
