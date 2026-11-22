import random

grid = [
    ["x"], ["x"], ["x"], ["x"], ["x"], ["x"],
    ["x"], ["."], ["."], ["."], ["."], ["x"],
    ["x"], ["."], ["."], ["."], ["."], ["x"],
    ["x"], ["."], ["."], ["."], ["."], ["x"],
    ["x"], ["."], ["."], ["."], ["."], ["x"],
    ["x"], ["x"], ["x"], ["x"], ["x"], ["x"]
]

def printgrid():
    for i in range(0, 36, 6):
        row = [cell[0] for cell in grid[i:i+6]]

        print(" ".join(row))

openpos = [i for i in range(len(grid)) if grid[i] == ["."]]
pos = random.choice(openpos)
x = (pos % 6) + 1   # Column (1 to 6)
y = (pos // 6) + 1  # Row (1 to 6)
gpos = random.choice(openpos)
while gpos == pos:
        gpos = random.choice(openpos)
grid[gpos] = ["G"]
grid[pos] = ["R"]  
printgrid()
print(f"Position: ({x}, {y})")

cont = int(input('Continue? 1 yes 2 no: '))

while cont == 1:
    # 2. Reset temporary coordinates to current (x, y) at the start of every turn
    new_x, new_y = x, y
    movement = int(input('Enter number from 1-4 (1 is up, 2 is down, 3 is right, 4 is left): '))
    if movement == 1:
        new_y -= 1
        printgrid()
    elif movement == 2:
        new_y += 1
        printgrid()
    elif movement == 3:
        new_x += 1
        printgrid()
    elif movement == 4:
        new_x -= 1
        printgrid()
    else:
        print('Error')
        printgrid()
        continue  # Indented inside else: so it only skips when there's an invalid number!

    # 3. Calculate new_pos and update the grid INSIDE the while loop
    new_pos = (new_y - 1) * 6 + (new_x - 1)

    if grid[new_pos] == ["x"]:
        print("Blocked by a wall!")
    else:
        grid[pos] = ["."]      # Erase old "R"
        pos = new_pos          # Update index
        x, y = new_x, new_y    # Update x and y
        grid[pos] = ["R"]      # Place new "R"
        if pos == gpos:
            printgrid()
            print("You reached the goal! You win!")
            break

    printgrid()
    print(f"Position: ({x}, {y})")
    cont = int(input('Continue? 1 yes 2 no: '))

