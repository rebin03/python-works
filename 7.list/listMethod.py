# list methods
# -------------

# append() - add element to the end of list
# insert() - add element to the specific position
# count() - return number of ooccurences of value
# pop() - remove and return the last element in the list (or remove an element from specific position by specifying index value.)
# remove() - remove specific element from the list and return the new list (if there's duplicate elements, remove the first occurence of element)
# extend() - to add collection of objects in to an existing list


num = [1,2,2,3,4]

num.append(5)
num.insert(1,6)

print(num)
print(num.count(2))
print(num.pop())
print(num.pop(1))
num.remove(2)
num.extend([6,7,8,9])
print(num)
