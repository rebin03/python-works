
def sum(n1,n2):     #remove def, function name, brackets
    return n1+n2    #remove return keyword

# Lambda function
add = lambda n1,n2: n1+n2
print(add(20,30))

sub = lambda n1,n2: n1-n2
print(sub(30,20))

cube = lambda n: n**3
print(cube(3))

max_two = lambda n1,n2: n1 if n1 > n2 else n2
print(max_two(70,80))

min_two = lambda n1,n2: n1 if n1 < n2 else n2
print(min_two(3,7))

