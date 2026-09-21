
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
    pass


grid = [
    [0, 0, 1],
    [1, 0, 0],
    [1, 1, 0]
]
