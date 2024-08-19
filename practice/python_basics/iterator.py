# -> An iterator is an object that contains a countable number of values.
# -> An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# -> Technically, in Python, an iterator is an object which implements the iterator protocol, 
#    which consist of the methods __iter__() and __next__().

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:

mytuple = ("apple","banana","orange")

it = iter(mytuple)

print(next(it))
print(next(it))
print(next(it))

# Strings are also iterable objects, containing a sequence of characters:

string = "banana"

strit = iter(string)

print(next(strit))
print(next(strit))
print(next(strit))
print(next(strit))
print(next(strit))
print(next(strit))