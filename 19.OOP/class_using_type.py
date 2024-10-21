# The class in python is object of 'type'. So we can define a class using the 'type' instead of 'class'.

# Usually we create class as follows:
class Test:
    pass

# but we can also create same like this:

Demo = type('Demo', (), {}) #this will create a class named Demo

# Now let's check the type of both class name
print(type(Test))
print(type(Demo))

# the type of both class instances
print(type(Test()))
print(type(Demo()))
