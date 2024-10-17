def hollow_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            if j == n - i + 1 or j == n + i - 1 or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Set the number of rows for the pyramid
rows = 5
# Call the function with the specified number of rows
hollow_pyramid(rows)