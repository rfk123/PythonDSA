
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def is_balanced(root: TreeNode) -> bool:
    def height(root):
        if not root:
            return 0

        left_height = height(root.left)
        if left_height == -1:
            return -1

        right_height = height(root.right)
        if right_height == -1:
            return -1

        if abs(right_height - left_height) > 1:
            return -1

        return 1 + max(right_height, left_height)

    return height(root) != -1

# The time complexity is O(n) and the space complexity is O(1)


def min_depth(node: TreeNode) -> int:
    if not node:
        return 0

    if not node.left:
        return 1 + min_depth(node.right)

    if not node.right:
        return 1 + min_depth(node.left)

    return 1 + min(min_depth(node.left), min_depth(node.right))


# Print Nodes in reversed order given the head of a linked list

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# Use recursion to print the linked list in reverse order
# base case is going to be when node == None


def reverse(head: Node) -> None:
    if not head:
        return

    reverse(head.next)
    print(head.val)


# reverse(head)


def f(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0

    return f(n-1) + f(n-2)


print(f(4))


def find_diameter(node: TreeNode) -> int:
    max_diameter = 0

    def height(node: TreeNode) -> int:
        nonlocal max_diameter

        if not node:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)
        max_diameter = max(max_diameter, left_height + right_height)

        return 1 + max(left_height, right_height)
    height(node)
    return max_diameter
