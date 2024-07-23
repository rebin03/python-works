# syntax:
# list1 = [return  iteration  condition]

lst = [1,2,3,4,5,6,7,8,9]

squares = [n**2 for n in lst ]
print(squares)

cubes = [n**3 for n in lst if n<7]
print(cubes)