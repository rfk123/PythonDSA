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

print(count_reachable(grid))
