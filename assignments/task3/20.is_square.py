def is_square(l, b):
    return l == b


length, breadth = map(int, input("Enter length and breadth of rectangle: ").split())
print("It's a square" if is_square(length, breadth) else "Not a square")