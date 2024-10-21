# We can also create inheritance by providing parent class name to the second parameter of the type.
# The attributes are specified in the third parameter as dictionary, key-value pairs.

class Foo:
    print("hello from parent class Foo")


Test = type("Test", (Foo,), {'x':5})

print(type(Test()))
t = Test()
print(t.x)