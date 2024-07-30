# Define:
# 1) set_obj = {obj1, obj2, obj3, ......}
# 2) set_obj = set()


# We can store same and different types of object
# order is not preserved
# cannot fetch a object using index position (does not have index position)
# duplicate value is not allowed
# set is mutable: we can add elements in the set.


# set Methods
# -----------
# add() - add element in the set
# remove() - remove element from the set (This will show error if the specified element to remove is not in the set)
# discard() - remove element from the set if it is present in the set
# clear() - remove all elements from the set
# pop() - remove and return an arbitary element from the set
# union() - return a new set with all elements from the both sets
# intersection() - return a new set with elements that are common in both sets
# difference() - return a new set with elements that are not common in both sets
# isdisjoint() - return True if two sets have a null intersection
# issubset() - return True if all elements in the set are present in another set
# issuperset() - return True if all elements in another set are present in the set
# update() - update the set with the union of itself and others (add element from any collection to the set.)
# copy() - return a shallow copy of the set
# len() - return the length of the set
# symmetric_difference() - combine all element from 2 set and remove common elements


names = {"hari","hello","sukumar","hello",3,True}

new_name = {"hp","dell","lenovo","hari"}

names.add("Kochi")

# names.update(new_name)

names.pop()
print(names)

names.discard("hello")
print(names)

# names.clear()
# print(names)

new_set1 = names.union(new_name)
print(new_set1)

new_set2 = names.intersection(new_name)
print(new_set2)

new_set3 = names.difference(new_name)
print(new_set3)

new_set4 = names.symmetric_difference(new_name)
print(new_set4)