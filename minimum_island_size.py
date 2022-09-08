def minimum_island(grid):
    # breadht first is more interesting to traverse the island

    visited = set()  # A set is O(1) read and write
    minimum_island_size = float("inf")

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = island_size_count(grid, r, c, visited)
            if 0 < size < minimum_island_size:
                minimum_island_size = size

    return minimum_island_size


def island_size_count(grid, r, c, visited):
    # Check if the row and column position do not exceed the grid inbounds

    inbound_r = 0 <= r and r < len(grid)
    inbound_c = 0 <= c and c < len(grid[0])

    if not inbound_c or not inbound_r:
        return 0  # Returning 0 based on how I plan to use it in my main funtion

    pos = str(r) + "," + str(c)

    if pos in visited:
        return 0

    visited.add(pos)

    if grid[r][c] != "L":
        return 0

    count = 1

    count += island_size_count(grid, r + 1, c, visited)
    count += island_size_count(grid, r, c + 1, visited)
    count += island_size_count(grid, r - 1, c, visited)
    count += island_size_count(grid, r, c - 1, visited)

    return count


if __name__ == "__main__":
    grid = [["W", "W"], ["L", "L"], ["W", "W"], ["W", "L"]]

print(minimum_island(grid))  # -> 1
