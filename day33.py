from collections import deque


class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_intersection_node(headA: ListNode | None, headB: ListNode | None) -> ListNode:
    listA = headA
    listB = headB

    while listA != listB:
        listA = listA.next if listA else headB
        listB = listB.next if listB else headA

    return listA


# print(get_intersection_node(head1, head2))


def preorder(root: TreeNode | None) -> list[int]:
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result


def inorder(root: TreeNode | None) -> list[int]:
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    dfs(root)
    return result


def postorder(root: TreeNode | None) -> list[int]:
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    dfs(root)
    return result


def level_order(root: TreeNode | None) -> list[int]:
    result = []
    if not root:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        popped = queue.popleft()
        result.append(popped.val)
        if popped.left:
            queue.append(popped.left)
        if popped.right:
            queue.append(popped.right)
    return result


def max_depth(root: TreeNode | None) -> int:
    # Using recursive dfs
    # The idea is that each node's max depth is 1 + the max depth of its max child node depth
    if not root:
        return 0
    queue = deque()
    queue.append(root)
    level = 0
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1

    return level
