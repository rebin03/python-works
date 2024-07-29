row1 = ['🙂','🙂','🙂']
row2 = ['🙂','🙂','🙂']
row3 = ['🙂','🙂','🙂']

matrix = [row1,row2,row3]
print(f"\n{row1}\n{row2}\n{row3}\n")

position = input("Enter the position where you want to hide money: ")

row_num = int(position[0]) - 1
column_num = int(position[1]) - 1

row_selected = matrix[row_num]
row_selected[column_num] = '💵'

print(f"\n{row1}\n{row2}\n{row3}\n")
