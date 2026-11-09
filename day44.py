from collections import deque


class TreeNode:
    def __init__(self, val, r_child=None, l_child=None):
        self.val = val
        self.r_child = r_child
        self.l_child = l_child


tree = TreeNode(1)
tree.l_child = TreeNode(2)
tree.r_child = TreeNode(3)
tree.l_child.l_child = TreeNode(4)
tree.l_child.r_child = TreeNode(5)
tree.r_child.l_child = TreeNode(10)


def contains(root: TreeNode, value: int) -> bool:
    if not root:
        return False
    queue = deque()
    queue.append(root)
    while queue:
        popped = queue.popleft()
        if popped.val == value:
            return True
        if popped.l_child != None:
            queue.append(popped.l_child)
        if popped.r_child != None:
            queue.append(popped.r_child)
    return False


def in_order(root) -> None:
    if not root:
        return
    print(root.val)
    in_order(root.l_child)
    in_order(root.r_child)


in_order(tree)

print("****************")


def pre_order_iterative(root) -> None:
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.r_child:
            stack.append(node.r_child)
        if node.l_child:
            stack.append(node.l_child)


pre_order_iterative(tree)
