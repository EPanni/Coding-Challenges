def island_count(grid):
    visited = set()
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited):
                count += 1

    return count


def explore(grid, row, column, visited):
    # In order to prevent if the positions are within the grid
    inbound_row = 0 <= row and row < len(grid)
    inbound_column = 0 <= column and column < len(grid[0])

    if not inbound_column or not inbound_row:
        return False

    if grid[row][column] != "L":
        return False

    pos = str(row) + "," + str(column)

    if pos in visited:
        return False
    visited.add(pos)

    explore(grid, row + 1, column, visited)
    explore(grid, row - 1, column, visited)
    explore(grid, row, column + 1, visited)
    explore(grid, row, column - 1, visited)

    return True


grid = [
    ["L", "L", "L"],
    ["L", "L", "L"],
    ["L", "L", "L"],
]

print(island_count(grid))  # -> 1
