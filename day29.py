
# queues and BFS

from collections import deque


def process_queue(nums: list[int]) -> list[int]:
    """
    Put all nums into a queue.
    Then remove them one by one from the front
    and return the removal order.
    """
    queue = deque(nums)
    result = []
    while queue:
        result.append(queue.popleft())
    return result


print(process_queue([10, 20, 30]))


def shortest_path(grid: list[list[int]]) -> int:
    """
    0 = open
    1 = blocked

    Start at (0, 0)
    End at (rows - 1, cols - 1)

    Move up, down, left, right.

    Return minimum number of moves,
    or -1 if impossible.
    """
    rows = len(grid)
    columns = len(grid[0])

    queue = deque()
    queue.append((0, 0, 0))

    visited = set((0, 0))
    directions = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
    ]
    # at each direction we will check: is it within the grid, is it open, have we seen it before
    while queue:
        row, column, distance = queue.popleft()
        print(row, column, distance)
        if row == rows - 1 and column == columns - 1:
            return distance

        # if we're not at our target (row,col) do our checks and append its valid directions
        for dr, dc in directions:
            new_row = row + dr
            new_column = column + dc

            # check if it is within the grid
            if 0 > new_row or new_row >= rows or 0 > new_column or new_column >= columns:
                continue
            if (new_row, new_column) in visited:
                continue
            if grid[new_row][new_column] != 0:
                continue
            visited.add((new_row, new_column))
            queue.append((new_row, new_column, distance + 1))
    return -1


grid = [
    [0, 0, 1],
    [1, 0, 0],
    [1, 1, 0]
]

print(shortest_path(grid))

# BFS practice


def bfs():
    # Bfs is a search through a tree structure that goes row by row starting at the starting node and going left to right on each row
    # Essentially you pop a node from the queue and append its child nodes until the queue is empty or until you have found what you're looking for sometimes.
    pass
