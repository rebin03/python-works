# short way to create generator function using expression
squared = (x*x for x in range(5))

print(next(squared))
print(next(squared))
print(next(squared))
print(next(squared))
print(next(squared))