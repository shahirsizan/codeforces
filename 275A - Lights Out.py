grid = [list(map(int, input().split()[:3])) for _ in range(3)]

def toggle_lights(x):
    return 1 - x  # Toggles 1 to 0 and 0 to 1

for i in range(3):
    for j in range(3):
        # Calculate the sum of the current cell and its adjacent cells
        total_presses = grid[i][j]
        if i > 0:
            total_presses += grid[i-1][j]  # Upper cell
        if i < 2:
            total_presses += grid[i+1][j]  # Lower cell
        if j > 0:
            total_presses += grid[i][j-1]  # Left cell
        if j < 2:
            total_presses += grid[i][j+1]  # Right cell

        # Determine the state of the light based on the total presses
        result = toggle_lights(total_presses % 2)
        print(result, end="")
    print()