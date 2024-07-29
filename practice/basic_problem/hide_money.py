matrix = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
]

print("""
      [1,1,1]
      [1,1,1]
      [1,1,1]
      """)

num = int(input("Enter the position(row and column): "))

j = num % 10 - 1
num = num//10
i = num - 1

matrix[i][j] = "X"

print(f"""
      [{matrix[0][0]},{matrix[0][1]},{matrix[0][2]}]
      [{matrix[1][0]},{matrix[1][1]},{matrix[1][2]}]
      [{matrix[2][0]},{matrix[2][1]},{matrix[2][2]}]
      """)


