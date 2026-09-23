# more queues
from collections import deque


def count_reachable(grid: list[list[int]]) -> int:
    """
    0 = open cell
    1 = blocked cell

    Start at (0, 0).

    You may move up, down, left, or right.

    Return how many open cells can be reached
    from (0, 0).
    """
    if grid[0][0] != 0:
        return 0

    rows = len(grid)
    columns = len(grid[0])

    queue = deque()
    queue.append((0, 0))

    visited = {(0, 0)}
    count = 1

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    while queue:
        row, column = queue.popleft()
        # move in the four directions and perform checks
        for dr, dc in directions:
            new_row = row + dr
            new_column = column + dc
            # perform our three checks which include: is it in range, is it open, has it been seen before
            if not (0 <= new_row < rows and 0 <= new_column < columns):
                continue
            if (new_row, new_column) in visited:
                continue
            if grid[new_row][new_column] != 0:
                continue

            visited.add((new_row, new_column))
            queue.append((new_row, new_column))
            count += 1
    return count


grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
]

# print(count_reachable(grid))


def num_islands(grid: list[list[str]]) -> int:
    """
    "1" = land
    "0" = water

    Land is connected up, down, left, and right.

    Return the number of separate islands.
    """
    rows = len(grid)
    columns = len(grid[0])

    visited = set()
    queue = deque()

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    count = 0
    for r in range(rows):
        for c in range(columns):
            if (r, c) in visited or grid[r][c] != '1':
                continue
            count += 1
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                row, column = queue.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_column = column + dc

                    if not (0 <= new_row < rows and 0 <= new_column < columns):
                        continue
                    if (new_row, new_column) in visited:
                        continue
                    if grid[new_row][new_column] != '1':
                        continue

                    visited.add((new_row, new_column))
                    queue.append((new_row, new_column))

    return count


grid = [
    ["1", "1", "0", "0"],
    ["1", "0", "0", "1"],
    ["0", "0", "1", "1"],
    ["1", "0", "0", "0"]
]

print(num_islands(grid))
