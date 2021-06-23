row1 = ["O","O","O"]
row2 = ["O","O","O"]
row3 = ["O","O","O"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where would you like to put the treasure? ")

row = int(position[0])
column = int(position[1])

map[column-1][row-1] = "X"

print(f"{row1}\n{row2}\n{row3}")