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

# print(number_of_islands(grid))


# LINKED LISTS YIPPIE

class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


def linked_list_values(head: ListNode | None) -> list[int]:
    """
    Return all values in the linked list in order.
    """
    node = head
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

print(linked_list_values(head))


def reverse_list(head: ListNode | None) -> ListNode | None:
    node = head
    prev = None
    while node:
        tmp = node.next
        node.next = prev
        prev = node
        node = tmp
    head = prev
    print(linked_list_values(head))


reverse_list(head)


def middle_node(head: ListNode | None) -> ListNode | None:
    """
    Return the middle node of the linked list.
    If there are two middle nodes, return the second one.
    """
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


print(middle_node(head))


def has_cycle(head: ListNode | None) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


def detect_cycle_start(head: ListNode) -> ListNode | None:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
