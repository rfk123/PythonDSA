from collections import deque

# Now lets work with DFS

# The first problem will be to solve the number of islands problem again but instead of BFS I'll use DFS and no queue
# BFS is breadth first search that goes level by level left to right
# DFS is depth first search that goes all the way down and backtracks from the furthest node


def number_of_islands(grid: list[list[str]]) -> int:
    row_count = len(grid)
    col_count = len(grid[0])
    count = 0
    visited = set()

    def dfs(row: int, col: int):
        if not (0 <= row < row_count and 0 <= col < col_count):
            return
        if grid[row][col] != '1':
            return
        if (row, col) in visited:
            return

        visited.add((row, col))

        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)

    for row in range(row_count):
        for col in range(col_count):
            if grid[row][col] != '1' or (row, col) in visited:
                continue
            dfs(row, col)
            count += 1
    return count


grid = [
    ["1", "1", "0", "0"],
    ["1", "0", "0", "1"],
    ["0", "0", "1", "1"],
    ["1", "0", "0", "0"]
]

print(number_of_islands(grid))
