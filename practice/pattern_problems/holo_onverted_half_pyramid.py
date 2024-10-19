def print_hollow_inverted_half_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(i):
            if j == 0 or j == i - 1 or i == rows:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Example usage
num_rows = 5
print("Hollow Inverted Half Pyramid:")
print_hollow_inverted_half_pyramid(num_rows)
