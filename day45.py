
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
